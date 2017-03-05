from cx_Freeze import setup, Executable

setup(
    name="ClinicaMedica EXECUTABLE",
    version = "1.0.0",
    description = ".py to .exe",
    executables = [Executable("ClinicaMedica.py")])
