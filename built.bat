build
pyinstaller start_gui.spec --noconfirm
robocopy utils/ dist/Game/utils
robocopy configs/ dist/Game/configs
robocopy models/ dist/Game/models
copy MiSans.ttf dist\Game\MiSans.ttf