# -*- mode: python ; coding: utf-8 -*-
import os

spec_root = os.path.abspath(SPECPATH)
block_cipher = None
from kivy_deps import sdl2, glew
from kivymd import hooks_path as kivymd_hooks_path

a = Analysis(['main.py'],
            pathex=[spec_root],
            binaries=[],
            datas=[('main.kv', '.'), ('./Backgrounds/*.png', 'images'), ('./Backgrounds/*.jpg', 'images'), ('./Extra_Widgets/*.py', 'Extra_Widgets'), ('./Extra_Widgets/*.kv', 'Extra_Widgets'), ('./Fonts/*.ttf', 'Fonts'), ('./Icons/*.png', 'Icons'), ('./WindowManager/*.py', 'WindowManager'), ('./WindowManager/*.kv', 'WindowManager')],
            hiddenimports=['win32timezone'],
            hookspath=[kivymd_hooks_path],
            runtime_hooks=[],
            excludes=[],
            win_no_prefer_redirects=False,
            win_private_assemblies=False,
            cipher=block_cipher,
            noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
            cipher=block_cipher)
exe = EXE(pyz,
            a.scripts,
            [],
            exclude_binaries=True,
            name='main',
            debug=True,
            bootloader_ignore_signals=False,
            strip=False,
            upx=False,
            console=False)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=False,
               name='main')

