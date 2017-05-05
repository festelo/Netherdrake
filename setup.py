from cx_Freeze import setup, Executable

setup(
    name='NetherDrake',
    version="1.0.0",
    description="Vk spam bot",
    executables=[Executable("Main.py", base="Win32GUI")],
    requires=['PyQt5', 'vk'],
)
