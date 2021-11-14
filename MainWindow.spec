# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import copy_metadata

import sys
sys.setrecursionlimit(5000)
block_cipher = None

# Transformers metadatas
datas = copy_metadata('tqdm')
datas += copy_metadata('regex')
datas += copy_metadata('requests')
datas += copy_metadata('sacremoses')
datas += copy_metadata('packaging')
datas += copy_metadata('filelock')
datas += copy_metadata('numpy')
datas += copy_metadata('tokenizers')
datas.append(('C:\\Users\\hungj\\Desktop\\env_win\\Lib\\site-packages\\ckip_transformers','ckip_transformers'))
datas.append(('C:\\Users\\hungj\\Desktop\\env_win\\Lib\\site-packages\\transformers','transformers'))

# Other stuffs
datas.append(('config.ini', '.' ))
datas.append(('C:\\ffmpeg\\bin\\ffmpeg.exe', '.' ))
datas.append(('C:\\ffmpeg\\bin\\ffplay.exe', '.' ))
datas.append(('C:\\ffmpeg\\bin\\ffprobe.exe', '.' ))
datas.append(('image','image'))
datas.append(('QSS','QSS'))


a = Analysis(['MainWindow.py'],
             pathex=['C:\\Users\\hungj\\Anaconda3\\Lib\\site-packages\\PyQt5\\Qt5\\bin',
                     'C:\\Users\\hungj\\Desktop\\專題\\CLSA',],
             binaries=[],
             datas=datas,
             hiddenimports=[],
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
