"""Bring LightCraft changes into LightKub's naming after `git merge upstream/main`.

  python3 packaging/sync_upstream.py

1. Renames LightCraft to LightKub in file contents and paths (library crates keep their
   lightcraft-* names), leaving the credits to upstream alone: "based on LightCraft", "LightCraft
   contributors", links to the upstream repository and the like.
   Then runs `cargo fmt --all`, since the shorter name changes line lengths.
2. Lists ArtCraft branding that came in with the merge (Discord, getartcraft.com, logos, the
   upstream company) and exits with status 1 if there is any: remove it by hand, then run again.

Safe to run more than once.
"""
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SKIP_DIRS = {".git", "target", "contributors"}
# Upstream's copyright and our own hand-written notices are never rewritten (paths from the root).
SKIP_FILES = {"LICENSE-MIT", "LICENSE-APACHE", "NOTICE", "README.md", "packaging/sync_upstream.py"}


def library_crates():
    """Crate folders, plus the planned crates named in xtask's layer table (lightcraft-testkit…)."""
    names = set(os.listdir(os.path.join(ROOT, "crates")))
    layers = os.path.join(ROOT, "xtask", "src", "layers.rs")
    if os.path.isfile(layers):
        names |= set(re.findall(r'\("([a-z0-9-]+)", Class::(?!Exempt)', open(layers, encoding="utf-8").read()))
    return sorted(names, key=len, reverse=True)


LIB_CRATES = library_crates()
LOWER = re.compile(r"lightcraft(?![-_](?:" + "|".join(c.replace("-", "[-_]") for c in LIB_CRATES) + "))")

# Credits to upstream that must keep the LightCraft name, and the lightcraft prefix shared by the
# library crates (log filters such as `lightcraft*=info`, `strip_prefix("lightcraft-")`).
PROTECTED = [
    "github.com/storytold/lightcraft",
    "Based on LightCraft",
    "based on LightCraft",
    "LightCraft contributors",
    "LightCraft by the ArtCraft team",
    # File formats shared with LightCraft: its XMP namespace and preset files stay readable both ways.
    "ns.lightcraft.app",
    '"lightcraft.preset"',
    '"lightcraft.curvePresets"',
    "lightcraft*",
    'starts_with("lightcraft")',
    '`lightcraft…=level`',
    "`lightcraft-`",
    '"lightcraft-"',
    '"lightcraft_"',
]
REPLACEMENTS = [
    (r"ai\.storyteller\.lightcraft", r"io\.github\.teh_natsu\.lightkub"),  # in regular expressions
    ("ai.storyteller.lightcraft", "io.github.teh_natsu.lightkub"),
    ("LIGHTCRAFT", "LIGHTKUB"),
    ("LightCraft", "LightKub"),
    ("Lightcraft", "Lightkub"),
]

BRANDING = re.compile(r"discord\.gg|getartcraft|artcraft[-_](mark|logo)|docs/brand|Learning Machines|storyteller\.ai|ai\.storyteller", re.I)
BRANDING_ALLOWED_FILES = {"NOTICE", "README.md", "ROADMAP.md", "LICENSE-MIT", "packaging/sync_upstream.py"}


def rename_text(text, protect=True):
    if protect:
        # A line that names ArtCraft is a credit to upstream ("based on LightCraft by the ArtCraft
        # team", in any language): leave it as it is.
        return "".join(line if "ArtCraft" in line else rename_text(line, protect=None) for line in text.splitlines(keepends=True))
    masks = {}
    if protect is None:
        protect = True
    if protect:
        for i, phrase in enumerate(PROTECTED):
            token = f"\0KEEP{i}\0"
            masks[token] = phrase
            text = text.replace(phrase, token)
    text = text.replace("storytold/lightcraft", "teh-natsu/lightkub")
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)
    text = LOWER.sub("lightkub", text)
    for token, phrase in masks.items():
        text = text.replace(token, phrase)
    return text


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=True).stdout


def rebrand():
    edited = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            path = os.path.join(dirpath, name)
            if os.path.relpath(path, ROOT).replace(os.sep, "/") in SKIP_FILES:
                continue
            raw = open(path, "rb").read()
            if b"\0" in raw:
                continue
            try:
                text = raw.decode("utf-8")
            except UnicodeDecodeError:
                continue
            new = rename_text(text)
            if new != text:
                open(path, "wb").write(new.encode("utf-8"))
                edited.append(os.path.relpath(path, ROOT).replace(os.sep, "/"))
    moves = {}
    for rel in git("ls-files").split("\n"):
        if not rel or rel.startswith("contributors/"):
            continue
        parts = rel.split("/")
        for i in range(len(parts)):
            new = rename_text(parts[i], protect=False)
            if new != parts[i]:
                moves["/".join(parts[: i + 1])] = "/".join(parts[:i] + [new])
    for old in sorted(moves, key=lambda p: p.count("/"), reverse=True):
        target = os.path.join(ROOT, moves[old])
        if os.path.isdir(target) and os.path.isdir(os.path.join(ROOT, old)):
            # The folder already exists under the new name: move the files one by one.
            for f in git("ls-files", old).split("\n"):
                if f:
                    os.makedirs(os.path.dirname(os.path.join(ROOT, moves[old] + f[len(old):])), exist_ok=True)
                    git("mv", f, moves[old] + f[len(old):])
        elif os.path.exists(os.path.join(ROOT, old)):
            git("mv", old, moves[old])
    return edited, moves


def branding_left():
    found = []
    for rel in git("ls-files").split("\n"):
        if not rel or rel.startswith("contributors/") or rel in BRANDING_ALLOWED_FILES:
            continue
        path = os.path.join(ROOT, rel)
        try:
            text = open(path, encoding="utf-8").read()
        except (UnicodeDecodeError, OSError):
            continue
        for n, line in enumerate(text.splitlines(), 1):
            if BRANDING.search(line):
                found.append(f"{rel}:{n}: {line.strip()[:140]}")
    return found


edited, moves = rebrand()
# The new names change line lengths: let rustfmt rewrap (skipped when Rust isn't installed).
try:
    subprocess.run(["cargo", "fmt", "--all"], cwd=ROOT, check=True)
except (OSError, subprocess.CalledProcessError) as e:
    print(f"cargo fmt skipped: {e}")
print(f"renamed text in {len(edited)} files, moved {len(moves)} paths")
for f in edited:
    print(f"  edited  {f}")
for old, new in moves.items():
    print(f"  moved   {old} -> {new}")
left = branding_left()
if left:
    print(f"\nArtCraft branding to remove by hand ({len(left)}):")
    for line in left:
        print(f"  {line}")
    sys.exit(1)
print("no ArtCraft branding left")
