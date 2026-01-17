#!/usr/bin/env python3

"""
Boucles Python - Automatisation DevOps
"""

# ============================================
# BOUCLES FOR
# ============================================

print("=== ROADMAP BOOTCAMP ===\n")

# Boucle simple
semaines = ["Semaine 1: Linux/Bash/Git", 
            "Semaine 2: Python/Docker",
            "Semaine 3: CI/CD",
            "Semaine 4: AWS"]

for semaine in semaines:
    print(f"📅 {semaine}")

print("\n=== COMPTEUR DE JOURS ===\n")

# Boucle avec range
for jour in range(1, 8):  # 1 à 7
    print(f"Jour {jour} : 2h de pratique ✅")

print("\n=== STACK TECHNIQUE ===\n")

# Boucle avec index
technologies = ["Linux", "Bash", "Git", "Python", "Docker", "Kubernetes", "AWS"]

for index, tech in enumerate(technologies, start=1):
    if index <= 4:
        statut = "✅ En cours/Acquis"
    else:
        statut = "⏳ À venir"
    print(f"{index}. {tech:15} {statut}")

# ============================================
# BOUCLES WHILE
# ============================================

print("\n=== SIMULATION APPRENTISSAGE ===\n")

competence_niveau = 0
objectif = 100

jours = 0
while competence_niveau < objectif:
    jours += 1
    competence_niveau += 15  # +15% par jour
    
    if jours % 7 == 0:  # Chaque semaine
        print(f"Semaine {jours//7} : Niveau {competence_niveau}%")

print(f"\n🎯 Objectif atteint en {jours} jours !")

# ============================================
# COMPREHENSION DE LISTES (Python pro)
# ============================================

print("\n=== SCRIPTS CRÉÉS ===\n")

scripts = ["system_check.sh", "backup_auto.sh", "git_stats.sh", 
           "check_file.sh", "list_files.sh", "deploy.sh"]

# Filtrer les scripts avec "check"
scripts_check = [s for s in scripts if "check" in s]
print(f"Scripts contenant 'check' : {scripts_check}")

# Créer une liste des longueurs
longueurs = [len(s) for s in scripts]
print(f"\nLongueurs des noms : {longueurs}")
print(f"Nom le plus long : {max(longueurs)} caractères")

# Transformer en majuscules
scripts_upper = [s.upper() for s in scripts]
print(f"\nEn majuscules : {scripts_upper[:3]}...")  # Affiche les 3 premiers
