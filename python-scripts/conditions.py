#!/usr/bin/env python3

"""
Conditions et logique - Python pour DevOps
"""

# ============================================
# CONDITIONS
# ============================================

jour_bootcamp = 4
scripts_crees = 6

print("=== ÉVALUATION PROGRESSION ===\n")

# If simple
if jour_bootcamp >= 4:
    print("✅ Semaine 1 bientôt terminée !")

# If/else
if scripts_crees > 5:
    print("✅ Tu as créé plus de 5 scripts - Excellent !")
else:
    print("⚠️  Continue à pratiquer")

# If/elif/else
heures_pratique = 8  # 4 jours × 2h

if heures_pratique >= 20:
    niveau = "Avancé"
elif heures_pratique >= 10:
    niveau = "Intermédiaire"
elif heures_pratique >= 5:
    niveau = "Débutant+"
else:
    niveau = "Débutant"

print(f"\n📊 Niveau actuel : {niveau}")
print(f"⏱️  Heures de pratique : {heures_pratique}h")

# Conditions multiples
competences_bash = True
competences_git = True
competences_python = False  # En cours d'apprentissage

if competences_bash and competences_git:
    print("\n✅ Fondations DevOps solides (Bash + Git)")

if competences_bash and competences_git and competences_python:
    print("🚀 Prêt pour Docker et AWS")
else:
    print("📚 Continue Python, puis direction Docker !")

# Opérateurs de comparaison
commits = 3
print(f"\n=== ANALYSE COMMITS ===")
print(f"Commits >= 3 : {commits >= 3}")
print(f"Commits == 3 : {commits == 3}")
print(f"Commits != 5 : {commits != 5}")

# Vérifier si élément dans liste
stack = ["Linux", "Bash", "Git", "Python"]

if "Docker" in stack:
    print("\n✅ Docker maîtrisé")
else:
    print("\n⏳ Docker : prochaine étape (semaine 2)")

if "Python" in stack:
    print("🐍 Python en cours d'apprentissage")
