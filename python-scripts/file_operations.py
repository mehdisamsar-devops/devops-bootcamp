#!/usr/bin/env python3

"""
Manipulation de fichiers - DevOps automation
"""

import os
from datetime import datetime

# ============================================
# ÉCRITURE DE FICHIERS
# ============================================

print("=== CRÉATION DE FICHIERS ===\n")

# Créer un fichier de log
log_file = "devops_log.txt"

# Mode 'w' = write (écrase si existe)
with open(log_file, 'w') as f:
    f.write(f"[{datetime.now()}] Bootcamp démarré\n")
    f.write(f"[{datetime.now()}] Jour 4 - Python pour DevOps\n")
    f.write(f"[{datetime.now()}] Scripts créés : 6 Bash + 8 Python\n")

print(f"✅ Fichier {log_file} créé")

# Mode 'a' = append (ajoute à la fin)
with open(log_file, 'a') as f:
    f.write(f"[{datetime.now()}] Compétences : Linux, Bash, Git, Python\n")
    f.write(f"[{datetime.now()}] Prochaine étape : Docker\n")

print(f"✅ Nouvelles lignes ajoutées à {log_file}\n")

# ============================================
# LECTURE DE FICHIERS
# ============================================

print("=== LECTURE DE FICHIER ===\n")

# Lire tout le contenu
with open(log_file, 'r') as f:
    contenu = f.read()
    print(contenu)

# Lire ligne par ligne
print("\n=== LECTURE LIGNE PAR LIGNE ===\n")
with open(log_file, 'r') as f:
    for numero, ligne in enumerate(f, start=1):
        print(f"Ligne {numero}: {ligne.strip()}")

# ============================================
# ANALYSE DE FICHIER
# ============================================

print("\n=== STATISTIQUES FICHIER ===\n")

# Compter lignes
with open(log_file, 'r') as f:
    lignes = f.readlines()
    nb_lignes = len(lignes)
    nb_mots = sum(len(ligne.split()) for ligne in lignes)
    nb_caracteres = sum(len(ligne) for ligne in lignes)

print(f"📊 Lignes : {nb_lignes}")
print(f"📊 Mots : {nb_mots}")
print(f"📊 Caractères : {nb_caracteres}")

# Taille du fichier
taille = os.path.getsize(log_file)
print(f"📊 Taille : {taille} bytes")

# ============================================
# CHERCHER DANS UN FICHIER
# ============================================

print("\n=== RECHERCHE DANS FICHIER ===\n")

mot_recherche = "Python"
lignes_trouvees = []

with open(log_file, 'r') as f:
    for numero, ligne in enumerate(f, start=1):
        if mot_recherche in ligne:
            lignes_trouvees.append((numero, ligne.strip()))

print(f"🔍 Recherche de '{mot_recherche}':")
for num, ligne in lignes_trouvees:
    print(f"  Ligne {num}: {ligne}")

# ============================================
# CRÉER UN RAPPORT
# ============================================

rapport_file = "rapport_bootcamp.txt"

with open(rapport_file, 'w') as f:
    f.write("=" * 50 + "\n")
    f.write("  RAPPORT BOOTCAMP DEVOPS - JOUR 4\n")
    f.write("=" * 50 + "\n\n")
    
    f.write(f"Date : {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
    f.write(f"Participant : Mehdi Samsar\n")
    f.write(f"Objectif : DevOps Engineer International\n\n")
    
    f.write("PROGRESSION:\n")
    f.write("-" * 50 + "\n")
    f.write(f"✅ Jour 1 : Linux & Terminal\n")
    f.write(f"✅ Jour 2 : Scripts Bash avancés\n")
    f.write(f"✅ Jour 3 : Git & GitHub\n")
    f.write(f"✅ Jour 4 : Python pour DevOps (en cours)\n\n")
    
    f.write("STATISTIQUES:\n")
    f.write("-" * 50 + "\n")
    f.write(f"Scripts Bash : 6\n")
    f.write(f"Scripts Python : 8+\n")
    f.write(f"Commits Git : 3\n")
    f.write(f"Heures pratique : 8h\n")
    f.write(f"Fichiers versionnés : 13+\n\n")
    
    f.write("COMPÉTENCES ACQUISES:\n")
    f.write("-" * 50 + "\n")
    competences = ["Linux command line", "Bash scripting", 
                   "Git workflow", "Python basics",
                   "Automatisation", "Documentation"]
    for i, comp in enumerate(competences, start=1):
        f.write(f"{i}. {comp}\n")
    
    f.write("\n" + "=" * 50 + "\n")

print(f"\n✅ Rapport créé : {rapport_file}")
print(f"\n📄 Contenu du rapport:\n")

# Afficher le rapport
with open(rapport_file, 'r') as f:
    print(f.read())
