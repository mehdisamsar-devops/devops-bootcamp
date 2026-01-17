#!/usr/bin/env python3

"""
Utilisation du module utils
Démonstration d'import et réutilisation
"""

# Import de notre module
import utils

# Import de modules Python standard
import os

# ============================================
# UTILISATION DES FONCTIONS UTILITAIRES
# ============================================

print(utils.create_banner("UTILISATION MODULE UTILS"))

# Timestamp
print(f"\n⏰ Timestamp actuel : {utils.get_timestamp()}")

# Vérifier fichiers
print("\n=== VÉRIFICATION FICHIERS ===")
fichiers_a_verifier = ["basics.py", "functions.py", "inexistant.py"]

for fichier in fichiers_a_verifier:
    existe = utils.check_file_exists(fichier)
    symbole = "✅" if existe else "❌"
    print(f"{symbole} {fichier}")
    
    if existe:
        size = utils.get_file_size(fichier)
        size_formatted = utils.format_bytes(size)
        print(f"   Taille : {size_formatted}")

# Lister fichiers Python
print("\n=== SCRIPTS PYTHON ===")
scripts_py = utils.list_files_in_directory(".", extension=".py")
print(f"Nombre de scripts .py : {len(scripts_py)}")
for script in scripts_py:
    size = utils.get_file_size(script)
    size_formatted = utils.format_bytes(size)
    print(f"  📄 {script:20} ({size_formatted})")

# Lister scripts Bash
print("\n=== SCRIPTS BASH ===")
bash_dir = "../projet-web/scripts"
if os.path.exists(bash_dir):
    scripts_sh = utils.list_files_in_directory(bash_dir, extension=".sh")
    print(f"Nombre de scripts .sh : {len(scripts_sh)}")
    for script in scripts_sh:
        filepath = os.path.join(bash_dir, script)
        size = utils.get_file_size(filepath)
        size_formatted = utils.format_bytes(size)
        print(f"  📄 {script:20} ({size_formatted})")
