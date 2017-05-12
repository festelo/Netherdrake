from cx_Freeze import setup, Executable

setup(
    name='VKcomments',
    version="1.1.0",
    description="Vk spam bot",
    executables=[Executable("Main.py", base="Win32GUI")],
    requires=['PyQt5', 'vk_api', 'requests', 'captcha_solver'],
)
