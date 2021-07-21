# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['gui_windows.py'],
             pathex=['Shenka.ico', 'city_code.txt', 'city_tuple.txt', 'C:\\Users\\〇\\Desktop\\招聘网站项目'],
             binaries=[],
             datas=[],
             hiddenimports=['Data_analysis.py', 'Data_cleaning.py', 'Display_info.py', 'gui_classes.py', 'gui_functions.py', 'Recrawler.py', 'Winscrawler.py'],
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
          name='gui_windows',
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
               name='gui_windows')
