#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script d'apprentissage Python - Basics
Auteur : Mehdi Samsar
Date : 17 Janvier 2026
"""

# ============================================
# VARIABLES ET TYPES
# ============================================

# String (texte)
nom = "Mehdi"
role = "DevOps Engineer"
message = f"Bonjour, je suis {nom}, futur {role}"
print(message)
print()

# Numbers (nombres)
age = 35
experience_mois = 0
salaire_cible = 70000
print(f"Âge : {age} ans")
print(f"Expérience DevOps : {experience_mois} mois")
print(f"Salaire cible : {salaire_cible}€")
print()

# Boolean (vrai/faux)
portfolio_en_ligne = True
certification_aws = False
print(f"Portfolio GitHub en ligne : {portfolio_en_ligne}")
print(f"Certification AWS obtenue : {certification_aws}")
print()

# Lists (listes)
competences = ["Linux", "Bash", "Git", "Python"]
print(f"Compétences actuelles : {competences}")
print(f"Nombre de compétences : {len(competences)}")
print(f"Première compétence : {competences[0]}")
print(f"Dernière compétence : {competences[-1]}")
print()

# Ajouter à la liste
competences.append("Docker")
competences.append("AWS")
print(f"Compétences mises à jour : {competences}")
print()

# Dictionary (dictionnaire - comme un objet)
profil = {
    "nom": "Mehdi Samsar",
    "pays": "France",
    "objectif": "International",
    "bootcamp_jour": 4,
    "scripts_bash": 6,
    "commits_git": 3
}
print("=== PROFIL DEVOPS ===")
for cle, valeur in profil.items():
    print(f"{cle}: {valeur}")
