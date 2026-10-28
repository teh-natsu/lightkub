---
title: Install LightKub
description: Download LightKub for Windows 11, macOS or Linux, install it, and open your photo library.
order: 10
verified: 0.7.1
---

Download the file for your system from the [latest release](https://github.com/teh-natsu/lightkub/releases/latest) and install it. In the file names, `<version>` stands for the version number, for example `0.7.1`.

## Windows 11

1. Open the [latest release](https://github.com/teh-natsu/lightkub/releases/latest).
2. Download `lightkub-<version>-windows-x64.msi`. It fits most PCs (Intel and AMD, 64-bit).
3. Run the file. The installer asks where to install. The default is `C:\Program Files\LightKub`, and upgrades stay in the folder you chose.
4. At the end, choose the option to start LightKub.

For a Snapdragon or other Arm PC, download `lightkub-<version>-windows-arm64.msi` instead. For a 32-bit Windows, download `lightkub-<version>-windows-x86.msi`.

Upgrading from an installer older than 0.6.0 also keeps LightKub in the folder it was installed in. If that folder was deleted, the upgrade installs to `C:\Program Files\LightKub`.

To run it without installing, download `lightkub-<version>-windows-x64-portable.zip`. Portable builds for `arm64` and `x86` are on the release page too.

## macOS

1. Download `lightkub-<version>-macos-universal.dmg`. It works on Apple silicon and Intel Macs, and is signed and notarized.
2. Open the file and install LightKub.

## Linux

The release has these files for `x86_64` and `aarch64` (Arm). Replace `x86_64` with `aarch64` on Arm.

| File                                         | Notes                                                    |
|----------------------------------------------|----------------------------------------------------------|
| `lightkub-<version>-linux-x86_64.AppImage` | Runs anywhere.                                           |
| `lightkub-<version>-linux-x86_64.flatpak`  | Sandboxed. Install with `flatpak install --user <file>`. |
| `lightkub-<version>-linux-x86_64.deb`      | For Debian and Ubuntu.                                   |
| `lightkub-<version>-linux-x86_64.rpm`      | For Fedora, RHEL and openSUSE.                           |
| `lightkub-<version>-linux-x86_64.tar.gz`   | Unpack anywhere.                                         |

RISC-V and FreeBSD builds are on the release page too. On a Wayland desktop, LightKub runs through XWayland when it is available, because only X11 gives it file drag-and-drop.

## In a web browser

The release also has `lightkub-web-<version>.zip`, a static site that runs LightKub in a modern browser. Host it on any static web server.

## First run

1. Start LightKub. It opens your library at `~/Pictures/LightKub Library`. A new library starts with demo photos.
2. To bring in your own photos, see [Import photos](../guides/import-photos.md).

## Still stuck?

Open an issue in the [issue tracker](https://github.com/teh-natsu/lightkub/issues).
