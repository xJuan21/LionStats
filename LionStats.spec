# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['C:\\LionStats\\LionStats\\manage.py'],
             pathex=[],
             binaries=[],
             datas=[('C:\LionStats\LionStats\static\styles', 'static/styles'),
             ('LionStats/templates', 'templates'),
             ('C:\LionStats\LionStats\static\images', 'static/images'),
             ('C:\LionStats\LionStats\static\js', 'static/js'),
             ('C:/LionStats/LionStats/teamproAPI', 'teamproAPI')],
             hiddenimports=['flask'],
             hookspath=[],
             hooksconfig={},
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
          name='manage',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
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
               name='manage')
