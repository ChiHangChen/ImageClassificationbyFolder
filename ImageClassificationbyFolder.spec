# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['ImageClassificationbyFolder.py'],
             pathex=['C:\\Users\\ChiHang\\Documents\\GitHub\\ImageClassificationbyFolder'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['mkl','whl'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
			 
a.datas += [ ('back.png', 'icon/back.png', 'DATA')]
a.datas += [ ('main.ico', 'icon/main.ico', 'DATA')]
a.datas += [ ('folder.png', 'icon/folder.png', 'DATA')]
a.datas += [ ('download.png', 'icon/download.png', 'DATA')]
a.datas += [ ('scissors.png', 'icon/scissors.png', 'DATA')]
a.datas += [ ('paste.png', 'icon/paste.png', 'DATA')]


pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='ImageClassificationbyFolder',
          debug=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='icon\\main.ico')
