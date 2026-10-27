# PlatformIO port: ESP32-S3-Zero + SH1106 + I2S DAC

This is the first migration step. The original yoRadio source and SPIFFS data layout are retained.

## Requirements

- VS Code with the PlatformIO IDE extension
- ESP32-S3-Zero
- SH1106 128x64 I2C display
- PCM5100A I2S DAC/amplifier module

## Configure

1. Open the `yoRadio` directory (the one containing `platformio.ini`) in VS Code.
2. `myoptions.h` is already configured for the current wiring; `myoptions.h.example` is a template with the same values.
3. GPIO mapping: SH1106 SDA=8/SCL=9; PCM5100A BCLK=5/LRCK=6/DOUT=7; encoder left=1/button=2/right=3.
4. Build with PlatformIO: `pio run`.

## Build / upload

Run these commands from the `yoRadio` directory:

- `pio run` — compile firmware
- `pio run -t upload` — flash firmware
- `pio run -t uploadfs` — upload the contents of `data/` as SPIFFS
- `pio device monitor` — serial monitor at 115200 baud

PlatformIO installs the pinned Adafruit display dependencies. The pre-build script patches the managed Adafruit GFX font from `fonts/glcdfont.c`; it does not modify the global `.platformio` package tree.

## Current status / limitations

This is an initial build-system port, not yet a verified firmware release. The project has not yet been compiled against a physical ESP32-S3-Zero. The 4 MB partition table reserves 320 KiB for SPIFFS and two 1.8 MiB OTA app slots; confirm the resulting firmware and filesystem fit before flashing. GPIOs must be set to the actual wiring. Other optional display libraries may need to be added to `lib_deps` if the initial compile reveals unconditional includes.
