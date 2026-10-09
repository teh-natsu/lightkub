# LightKub app icon

<img src="lightkub.svg" alt="LightKub app icon: a red panda peeking over a landscape photo and holding it with both paws, on violet" width="128">

**Creature:** a red panda (แพนด้าแดง), head and paws, peeking over the top edge of a photo print and
holding it. Cream brows, cheeks and muzzle, dark tear marks under the eyes, cream-rimmed ears. The same
red panda as [PdfKub](https://github.com/teh-natsu/pdfkub)'s icon, holding a photo instead of a page.

**Palette:**

| Colour | Hex | Used for |
|---|---|---|
| Violet (app colour) | `#9b4fd8` → `#4b1a78` | the full-bleed field, top to bottom |
| Fur | `#e8692d` → `#bb4015` | head and ears, top to bottom |
| Dark fur | `#6b2410`, `#3a1a10` | tear marks and inner ears; paws |
| Cream | `#fff6ea` | brows, cheeks, muzzle, ear rims |
| Ink | `#1a0f0b` | eyes, nose, mouth |
| Photo | `#ffffff` border; sky `#7cc6ef` → `#d6efff`, sun `#ffc93c`, hills `#3f9a7c`, `#226a52` | the print and its landscape |

**Tile:** `viewBox="0 0 512 512"`, a rounded square with `rx=112` that clips everything. Windows and Linux
icons use the full-bleed tile. macOS files (`.icns`, `lightkub-macos-512.png`) put it on Apple's grid (an
824/1024 body with a transparent margin).

**Small sizes:** `lightkub-small.svg` (used at 24 px and below) drops the eye highlights, blush, mouth,
claws and the far hill, and draws bigger eyes and a bigger sun instead.

**Provenance:** drawn as plain SVG shapes by [`packaging/make_icon.py`](../../packaging/make_icon.py); no
fonts or third-party artwork. Licence: [LICENSE.txt](LICENSE.txt) (`MIT OR Apache-2.0`, like the repo).

## Files

| File | What it is |
|---|---|
| `lightkub.svg` | the master vector; every PNG, `.ico` and `.icns` above 24 px is rendered from it |
| `lightkub-small.svg` | the 16–24 px variant |
| `lightkub-1024.png` | 1024 px render (store listings, docs) |
| `lightkub-macos-512.png` | runtime window/Dock icon on macOS (embedded by `apps/lightkub/src/main.rs`) |
| `lightkub.icns` | macOS bundle icon (`CFBundleIconFile`) |
| `lightkub.ico` | Windows icon, 16–256 px, embedded in `lightkub.exe` by `apps/lightkub/build.rs` |
| `hicolor/<n>x<n>/apps/io.github.teh_natsu.lightkub.png` | Linux icon theme, 16–512 px; the 256 px one is also the runtime window icon on Windows and Linux |
| `hicolor/scalable/apps/io.github.teh_natsu.lightkub.svg` | Linux scalable icon (copy of the master) |

The app id is `io.github.teh_natsu.lightkub`: the Wayland app id, the `.desktop` file
(`packaging/linux/io.github.teh_natsu.lightkub.desktop`, `Icon=io.github.teh_natsu.lightkub`) and the
hicolor icon name. To install on Linux, copy `hicolor/` into `/usr/share/icons/hicolor/` (or
`~/.local/share/icons/hicolor/`) and the `.desktop` file into `applications/`.

## Regenerate

```sh
python3 packaging/make_icon.py assets/app-icon   # writes lightkub.svg and lightkub-small.svg
packaging/icons.sh                               # needs resvg (Pillow for the .icns off macOS)
```
