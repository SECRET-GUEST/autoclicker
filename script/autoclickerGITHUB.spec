# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['LOL:\\_YOUR_\\_PATH_\\_HERE_\\\\autoclicker.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('LOL:\\_YOUR_\\_PATH_\\_HERE_\\\\ico\\autoclicker.png', 'ico'),
        ('LOL:\\_YOUR_\\_PATH_\\_HERE_\\\\ico\\autoclicker.png', 'ico'),

    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Your Hardworking BRUH',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Change to False if you want a GUI executable
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='LOL:\\_YOUR_\\_PATH_\\_HERE_\\\\ico\\autoclicker.ico',
)

# Optional: use UPX to compress the executable
# You need to have UPX installed and added to the system PATH for this to work
# See https://upx.github.io/ for more information
import os
upx_path = 'upx'  # Change to the path of UPX if it's not in the system PATH
if os.path.exists(upx_path):
    exe.upx = True
    exe.upx_args.append('--lzma')
else:
    print('WARNING: UPX not found in system PATH, executable will not be compressed')
