# LightKub app icon

<img src="lightkub.svg" alt="LightKub app icon: a flat red panda resting its paws on a white card with a photo (sun and mountains), on violet glass" width="128">

**Creature:** a flat red panda (แพนด้าแดง), head and paws, resting its paws on a white card that shows
a photo (sun and mountains). Cream inner ears, brows, cheeks and muzzle, dark tear marks under the eyes. The same panda in all three
*Kub apps ([PdfKub](https://github.com/teh-natsu/pdfkub), [LightKub](https://github.com/teh-natsu/lightkub),
[CadKub](https://github.com/teh-natsu/cadkub)); each has its own tile colour and symbol.

**Palette:**

| Colour | Hex | Used for |
|---|---|---|
| Violet (app colour) | `#b673ff` → `#6526c2` | the tile, top-left to bottom-right; the symbol on the card |
| Glass lights | `#ff86d8`, `#5b8cff` | two blurred lights behind the frosted pane (top-left, bottom-right) |
| Glass | white at 7 %, a white sheen and a white rim | the frosted pane, its diagonal sheen and its lit edge |
| Fur | `#f2732f`; paws `#d85a1e` | head and ears; paws |
| Cream | `#fff5e8` | inner ears, brows, cheeks, muzzle |
| Tear marks | `#a3391a` | under the eyes |
| Ink | `#22140f` | eyes, nose, mouth |
| Card | `#ffffff`; sun `#ffc53d` | a photo: frame, sun and two mountains in the app colour |

**Tile:** `viewBox="0 0 512 512"`, a rounded square with `rx=114` that clips everything; the card casts a
soft shadow. Windows and Linux icons use the full-bleed tile. macOS icons put it on Apple's grid (an
824/1024 body with a transparent margin).

**Small sizes:** `lightkub-small.svg` (used at 24 px and below) drops the glass lights, the shadow, the eye
highlights and the mouth, and draws bigger eyes, a thicker rim, frame and sun.

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
