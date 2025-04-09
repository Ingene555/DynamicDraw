import os
import sys
import ctypes
import winreg as reg

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    script = sys.argv[0]
    params = ' '.join(sys.argv[1:])
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f"{script} {params}", None, 1)

def associate_dynd_file_extension(program_path):
    if not os.path.isfile(program_path):
        return
    try:
        reg_key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, ".dynd")
        reg.SetValue(reg_key, "", reg.REG_SZ, "DyndFile")
        reg.CloseKey(reg_key)
        print(".dynd extension associée avec DyndFile")
        reg_key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, "DyndFile\\shell\\open\\command")
        reg.SetValue(reg_key, "", reg.REG_SZ, f'"{program_path}" "%1"')
        reg.CloseKey(reg_key)
        print(f"DyndFile associé avec '{program_path}'")
    
    except Exception as e:
        print(f"Erreur lors de l'association du fichier: {e}")

def associate_dynd_file_extension2():
    program_path = os.path.join(os.getcwd(), sys.argv[0])
    if not os.path.isfile(program_path):
        print(f"Le chemin du programme '{program_path}' est invalide.")
        return
    try:
        reg_key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, ".dynd")
        reg.SetValue(reg_key, "", reg.REG_SZ, "DyndFile")
        reg.CloseKey(reg_key)
        print(".dynd extension associée avec DyndFile")
        reg_key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, "DyndFile\\shell\\open\\command")
        reg.SetValue(reg_key, "", reg.REG_SZ, f'"{sys.executable}" "{program_path}" "%1"')
        reg.CloseKey(reg_key)
        print(f"DyndFile associé avec '{program_path}'")
    
    except Exception as e:
        print(f"Erreur lors de l'association du fichier: {e}")
        return
