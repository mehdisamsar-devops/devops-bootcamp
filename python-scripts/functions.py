#!/usr/bin/env python3

"""
Fonctions Python - Réutilisabilité du code
"""

# ============================================
# FONCTIONS DE BASE
# ============================================

def afficher_banner(titre):
    """Affiche un titre avec un bandeau"""
    longueur = len(titre) + 4
    print("=" * longueur)
    print(f"  {titre}")
    print("=" * longueur)

def calculer_progression(jour_actuel, jours_total):
    """Calcule le pourcentage de progression"""
    pourcentage = (jour_actuel / jours_total) * 100
    return round(pourcentage, 1)

def evaluer_niveau(heures_pratique):
    """Évalue le niveau selon les heures de pratique"""
    if heures_pratique >= 100:
        return "Expert"
    elif heures_pratique >= 50:
        return "Avancé"
    elif heures_pratique >= 20:
        return "Intermédiaire"
    else:
        return "Débutant"

# ============================================
# FONCTIONS AVEC PARAMÈTRES PAR DÉFAUT
# ============================================

def creer_commit_message(action, fichier, details=""):
    """Génère un message de commit Git"""
    message = f"{action}: {fichier}"
    if details:
        message += f" - {details}"
    return message

# ============================================
# FONCTIONS AVEC ARGUMENTS VARIABLES
# ============================================

def compter_scripts(*scripts):
    """Compte le nombre de scripts (nombre variable d'arguments)"""
    return len(scripts)

def afficher_stack(**technologies):
    """Affiche les technologies avec leur niveau (kwargs)"""
    print("\n📚 Stack Technique:")
    for tech, niveau in technologies.items():
        emoji = "✅" if niveau == "Maîtrisé" else "📚"
        print(f"  {emoji} {tech}: {niveau}")

# ============================================
# UTILISATION DES FONCTIONS
# ============================================

if __name__ == "__main__":
    # Banner
    afficher_banner("DEVOPS BOOTCAMP - JOUR 4")
    
    # Progression
    jour = 4
    total = 180
    prog = calculer_progression(jour, total)
    print(f"\n📊 Progression : Jour {jour}/{total} ({prog}%)")
    
    # Niveau
    heures = 8  # 4 jours × 2h
    niveau = evaluer_niveau(heures)
    print(f"🎯 Niveau actuel : {niveau}")
    
    # Messages de commit
    print("\n=== EXEMPLES COMMITS GIT ===")
    print(creer_commit_message("Add", "monitoring.py", "script de monitoring système"))
    print(creer_commit_message("Fix", "backup.py"))
    print(creer_commit_message("Update", "README.md", "ajout section Python"))
    
    # Compter scripts
    nb_scripts = compter_scripts("system_check.sh", "backup.sh", "git_stats.sh", 
                                  "check_file.sh", "list_files.sh", "deploy.sh")
    print(f"\n📝 Scripts Bash créés : {nb_scripts}")
    
    # Stack technique
    afficher_stack(
        Linux="Maîtrisé",
        Bash="Maîtrisé",
        Git="Maîtrisé",
        Python="En cours",
        Docker="À venir",
        AWS="À venir"
    )
    
    # Calculs multiples
    print("\n=== PROJECTIONS ===")
    for mois in [1, 3, 6]:
        jours = mois * 30
        heures = jours * 2
        niveau_futur = evaluer_niveau(heures)
        print(f"Après {mois} mois ({heures}h) : {niveau_futur}")
