# -*- mode: python -*-

block_cipher = None


a = Analysis(['pyqtTest.py'],
             pathex=['mainwindow.py', 'choosecourse_window.py', 'firstCatch.py', 'C:\\selenium_driver_chrome\\py_to_exe'],
             binaries=[],
             datas=[],
             hiddenimports=['mainwindow', 'choosecourse_window', 'firstCatch'],
             hookspath=[],
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
          [],
          name='pyqtTest',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
