# -*- mode: python ; coding: utf-8 -*-

added_files = [
("configs/database.cfg", "configs/"),
("models/charity_match.py", "models/"),
("models/club.py", "models/"),
("models/coach.py", "models/"),
("models/debug.py", "models/"),
("models/error.py", "models/"),
("models/field.py", "models/"),
("models/footballer.py", "models/"),
("models/highlighting.py", "models/"),
("models/info.py", "models/"),
("models/load_game.py", "models/"),
("models/manager.py", "models/"),
("models/panels.py", "models/"),
("models/player.py", "models/"),
("models/property.py", "models/"),
("models/revive.py", "models/"),
("models/save_game.py", "models/"),
("models/statistics.py", "models/"),
("models/transfer_window.py", "models/"),
("models/tv_company.py", "models/"),
("models/vaccine.py", "models/"),
("utils/constants.py", "utils/"),
("utils/initialize.py", "utils/")]

a = Analysis(
    ['start_gui.py'],
    pathex=["C:/Users/ARnoLD/Desktop/[0 GUI] Football Manager"],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Game',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Game',
)
