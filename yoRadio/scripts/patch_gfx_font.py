Import("env")

from pathlib import Path
import shutil

project_dir = Path(env["PROJECT_DIR"])
libdeps_dir = Path(env.subst("$PROJECT_LIBDEPS_DIR")) / env.subst("$PIOENV")
source_font = project_dir / "fonts" / "glcdfont.c"

if not source_font.is_file():
    raise RuntimeError("yoRadio font file is missing: {}".format(source_font))

candidates = list(libdeps_dir.glob("**/Adafruit GFX Library/**/glcdfont.c"))
if not candidates:
    # PlatformIO package folder names can vary slightly; search only inside this
    # environment's managed dependencies, never in the global .platformio tree.
    candidates = [
        p for p in libdeps_dir.glob("**/glcdfont.c")
        if "adafruit" in str(p.parent).lower() and "gfx" in str(p).lower()
    ]

if not candidates:
    raise RuntimeError(
        "Adafruit GFX glcdfont.c was not found under {}. "
        "Check that Adafruit GFX Library is installed by PlatformIO.".format(libdeps_dir)
    )

for target in candidates:
    if target.resolve() != source_font.resolve():
        shutil.copy2(str(source_font), str(target))
        print("yoRadio: patched managed GFX font: {}".format(target))
