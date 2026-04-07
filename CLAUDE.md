# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

The project uses [Poetry](https://python-poetry.org/) for dependency and environment management.

```sh
# Install dependencies
poetry install

# Run the GUI app
poetry run qrCodeGenGUI

# Run the CLI entry point (stub, currently just calls GenerateQrCode())
poetry run qrCodeGen
```

No test suite is currently configured.

## Architecture

This is a PySide6 desktop app for generating QR codes from URLs, with optional center-icon overlay.

### Entry points (`src/qrcodegen/app.py`)
- `mainGUI()` — launches the Qt GUI (`RunGUI` in `QRCodeGenWidget.py`)
- `main()` — CLI stub, calls `GenerateQrCode()` directly

### Core modules

| File | Role |
|------|------|
| `QRCodeUtils.py` | `GenerateQrCode(savePath, url, iconPath=None)` — the single function that produces a QR code PNG. Handles icon overlay (centered, 1/4 QR width, with white border via `ImageOps.expand`). |
| `QRCodeGenWidget.py` | `QRCodeWidget` (PySide6 `QWidget`) — UI with URL input, optional icon picker, and save-file dialog. Calls `GenerateQrCode` on submit. |
| `qrCodeGen.py` | Legacy/batch script for a separate use-case (booth QR codes with color-coded icons). Imports from a `consts` module that is **not part of this package** — this file is not wired into the current app and will fail if run directly. |

### Key implementation detail
`QRCodeUtils.GenerateQrCode` uses `ERROR_CORRECT_H` (30% error correction), which allows placing a center icon over ~30% of the QR code without making it unscannable. The icon is pasted using itself as the alpha mask, so the source image must have an alpha channel for transparency to work correctly.
