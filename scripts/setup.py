import sys
import os
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["os", "sys", "uuid", "random", "ctypes", "functools", "time", "threading", "PyQt5", "pynput"],
    "excludes": ["tkinter"],
    "include_files": [
        os.path.join("ico", "autoclicker.ico"),
        os.path.join("ico", "autoclicker.png"),
        os.path.join("ico", "close.png"),
        os.path.join("ico", "hide.png"),
        os.path.join("ico", "open.png"),
        os.path.join("ico", "theme1.png"),
        os.path.join("ico", "theme2.png"),
        os.path.join("ico", "theme3.png"),
        os.path.join("ico", "theme4.png"),
        os.path.join("ico", "theme5.png"),
        os.path.join("style", "style1.txt"),
        os.path.join("style", "style2.txt"),
        os.path.join("style", "style3.txt"),
        os.path.join("style", "style4.txt"),
        os.path.join("style", "style5.txt")
    ],
}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Autoclicker",
    version="1.0",
    description="Autoclicker Application",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base, icon=os.path.join("ico", "autoclicker.ico"), shortcut_name="Autoclicker", shortcut_dir="DesktopFolder")],
    license="LICENSE.rtf",
)
