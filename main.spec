# -*- mode: python ; coding: utf-8 -*-

block_cipher = None
from kivymd import hooks_path as kivymd_hooks_path

def find_gst_plugin_path():
    p = subprocess.Popen(
        ['gst-inspect-1.0', 'coreelements'],
        stdout=subprocess.PIPE)
    (stdoutdata, stderrdata) = p.communicate()

    match = re.search(r'\s+(\S+libgstcoreelements\.\S+)', stdoutdata)

    if not match:
        raise Exception('could not find GStreamer plugins')

    return os.path.dirname(match.group(1))


def find_gst_binaries():
    plugin_path = find_gst_plugin_path()

    plugin_filepaths = glob.glob(os.path.join(plugin_path, 'libgst*'))

   # PyInstaller does not automatically include the libraries the plugins link to
    lib_filepaths = set()
    for plugin_filepath in plugin_filepaths:
        plugin_deps = bindepend.selectImports(plugin_filepath)
        lib_filepaths.update([path for _, path in plugin_deps])

    plugin_binaries = [(f, 'gst-plugins') for f in plugin_filepaths]
    lib_binaries = [(f, '.') for f in lib_filepaths]

    return plugin_binaries + lib_binaries

a = Analysis(['main.py'],
             pathex=[],
             binaries=find_gst_binaries(),
             datas=[('main.kv', '.')],
             hiddenimports=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )







