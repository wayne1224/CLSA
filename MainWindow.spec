# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['MainWindow.py'],
             pathex=['C:\\Users\\hungj\\Anaconda3\\Lib\\site-packages\\PyQt5\\Qt5\\bin', 'C:\\Users\\hungj\\Desktop\\專題\\CLSA'],
             binaries=[('C:\\ffmpeg\\bin\\ffmpeg.exe','ffmpeg.exe'),
                       ('C:\\ffmpeg\\bin\\ffplay.exe','ffplay.exe'),
                       ('C:\\ffmpeg\\bin\\ffprobe.exe','ffprobe.exe')],
             datas=[],
             hiddenimports=['dns'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=['torch.distributions'],
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
          name='MainWindow',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='MainWindow')
