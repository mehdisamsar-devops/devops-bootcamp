#!/usr/bin/env python3

"""
Manipulation JSON - Format standard DevOps
Utilisé par : Docker, Kubernetes, AWS, APIs, configs...
"""

import json
from datetime import datetime

# ============================================
# CRÉER UN OBJET JSON
# ============================================

print("=== CRÉATION JSON ===\n")

# Dict Python → JSON
bootcamp_data = {
    "participant": {
        "nom": "Mehdi Samsar",
        "age": 35,
        "pays": "France",
        "objectif": "DevOps Engineer International"
    },
    "bootcamp": {
        "debut": "2026-01-16",
        "duree_mois": 6,
        "heures_par_jour": 2,
        "jour_actuel": 4
    },
    "competences": {
        "acquises": ["Linux", "Bash", "Git", "Python basics"],
        "en_cours": ["Python avancé"],
        "a_venir": ["Docker", "Kubernetes", "AWS", "Terraform"]
    },
    "statistiques": {
        "scripts_bash": 6,
        "scripts_python": 8,
        "commits_git": 3,
        "fichiers_versionnes": 13,
        "heures_pratique": 8
    },
    "projets": [
        {
            "nom": "system_check.sh",
            "type": "Bash",
            "description": "Monitoring système",
            "status": "Terminé"
        },
        {
            "nom": "backup_auto.sh",
            "type": "Bash",
            "description": "Backup automatique avec timestamp",
            "status": "Terminé"
        },
        {
            "nom": "git_stats.sh",
            "type": "Bash",
            "description": "Analyse repo Git",
            "status": "Terminé"
        }
    ]
}

# Sauvegarder en JSON
json_file = "bootcamp_data.json"
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(bootcamp_data, f, indent=2, ensure_ascii=False)

print(f"✅ Fichier JSON créé : {json_file}\n")

# Afficher le JSON formaté
print("📄 Contenu JSON:\n")
print(json.dumps(bootcamp_data, indent=2, ensure_ascii=False))

# ============================================
# LIRE UN FICHIER JSON
# ============================================

print("\n" + "="*50)
print("=== LECTURE JSON ===\n")

# Charger depuis fichier
with open(json_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Accéder aux données
print(f"👤 Participant : {data['participant']['nom']}")
print(f"🎯 Objectif : {data['participant']['objectif']}")
print(f"📅 Jour actuel : {data['bootcamp']['jour_actuel']}")
print(f"⏱️  Heures pratique : {data['statistiques']['heures_pratique']}h")

print(f"\n📚 Compétences acquises :")
for comp in data['competences']['acquises']:
    print(f"  ✅ {comp}")

print(f"\n📊 Projets terminés : {len(data['projets'])}")
for projet in data['projets']:
    print(f"  📄 {projet['nom']} ({projet['type']})")

# ============================================
# MODIFIER ET METTRE À JOUR JSON
# ============================================

print("\n" + "="*50)
print("=== MISE À JOUR JSON ===\n")

# Ajouter une nouvelle compétence
data['competences']['acquises'].append("File operations")
data['competences']['acquises'].append("JSON manipulation")

# Mettre à jour statistiques
data['statistiques']['scripts_python'] += 2  # +2 nouveaux scripts
data['statistiques']['heures_pratique'] = 10  # Mise à jour heures

# Ajouter un nouveau projet
nouveau_projet = {
    "nom": "json_operations.py",
    "type": "Python",
    "description": "Manipulation JSON pour configs DevOps",
    "status": "En cours"
}
data['projets'].append(nouveau_projet)

# Ajouter métadonnées
data['metadata'] = {
    "derniere_mise_a_jour": datetime.now().isoformat(),
    "version": "1.0",
    "progression_pourcentage": round((4/180) * 100, 1)
}

# Sauvegarder les modifications
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ JSON mis à jour avec :")
print(f"  • 2 nouvelles compétences")
print(f"  • 1 nouveau projet")
print(f"  • Statistiques actualisées")
print(f"  • Métadonnées ajoutées")

# ============================================
# CRÉER UN DASHBOARD JSON
# ============================================

dashboard = {
    "dashboard_devops": {
        "titre": "Bootcamp DevOps - Dashboard",
        "participant": data['participant']['nom'],
        "mise_a_jour": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "progression": {
            "jour_actuel": data['bootcamp']['jour_actuel'],
            "total_jours": 180,
            "pourcentage": data['metadata']['progression_pourcentage'],
            "heures_investies": data['statistiques']['heures_pratique']
        },
        "metriques": {
            "scripts_total": data['statistiques']['scripts_bash'] + data['statistiques']['scripts_python'],
            "scripts_bash": data['statistiques']['scripts_bash'],
            "scripts_python": data['statistiques']['scripts_python'],
            "commits_git": data['statistiques']['commits_git'],
            "competences_acquises": len(data['competences']['acquises']),
            "projets_termines": len([p for p in data['projets'] if p['status'] == "Terminé"])
        },
        "prochaines_etapes": data['competences']['a_venir'][:3]
    }
}

dashboard_file = "dashboard.json"
with open(dashboard_file, 'w', encoding='utf-8') as f:
    json.dump(dashboard, f, indent=2, ensure_ascii=False)

print(f"\n✅ Dashboard créé : {dashboard_file}")
print("\n📊 DASHBOARD:\n")
print(json.dumps(dashboard, indent=2, ensure_ascii=False))

print("\n" + "="*50)
print("✅ Tous les fichiers JSON créés avec succès !")
print(f"📁 {json_file}")
print(f"📁 {dashboard_file}")
