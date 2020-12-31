import cx_Freeze
 
executables = [cx_Freeze.Executable("main.py",
                                    targetName="Floppy.exe",
                                    icon="icon.ico")]
                                  #base = "Win32GUI",
                                  #icon = "assets/bobi_icon.png")]
 
build_exe_options = {"packages": ["pygame"],
                     "include_files":["src", "assets"]}
 
cx_Freeze.setup(
    name = "Floppy: Ad aeternum",
    version = "1.0b",
    description = "Juego Floppy: Ad aeternum",
    options={"build_exe": build_exe_options},
    executables = executables
    )