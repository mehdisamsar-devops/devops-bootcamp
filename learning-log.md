# Journal DevOps - Bootcamp Intensif

## Objectif final
DevOps Engineer (Junior/Mid-level) - Position internationale - 6 mois
Ouvert à : Moyen-Orient (Arabie Saoudite, Émirats, Qatar), Europe, Amérique du Nord

## Pourquoi DevOps ?
- Passion pour l'automatisation et l'infrastructure
- Compétences techniques recherchées mondialement
- Opportunités internationales excellentes
- Salaires compétitifs et perspectives d'évolution
## Semaine 1 - Fondations Linux & Bash

### Jour 1 - 16 Janvier 2026 ✅

#### ✅ Compétences acquises :
- Navigation terminal (pwd, cd, ls -la)
- Gestion fichiers (mkdir -p, touch, rm, cp, mv)
- Recherche (find . -name "*.extension")
- Permissions (chmod +x, ls -l)
- Éditeur nano (Ctrl+O, Ctrl+X)
- Premier script Bash fonctionnel
- Variables et substitution de commandes $(commande)

#### 💪 Réalisations :
- Structure projet-web complète
- Script system_check.sh opérationnel
- 6 fichiers organisés
- Mémo commandes créé

#### 🎯 Commandes maîtrisées (19) :
pwd, cd, ls, mkdir, touch, cat, cp, mv, rm, find, echo, chmod, 
whoami, date, df, top, nano, tree, grep

#### 🤔 Points d'attention :
- Différence entre placeholder [dossier] et vrai chemin
- Importance du chmod +x pour scripts
- Symbole ~ = Option + N sur Mac

#### ⏱️ Temps : 2h (objectif respecté)

#### 🔥 Motivation : 10/10
Premier script qui fonctionne ! Je comprends la logique.

---

### Jour 2 - [Date] (À venir)
LAB 2 : Scripts Bash avancés, conditions, boucles
### Jour 2 - 16 Janvier 2026 ✅

#### ✅ Compétences acquises :
- Conditions Bash (if/else, tests -f/-d/-x/-z)
- Boucles for sur fichiers
- Arguments de scripts ($1, $2, $@)
- Variables et substitution $(commande)
- Codes de sortie et gestion d'erreurs ($?)
- Couleurs terminal (GREEN/RED/YELLOW)
- Archives tar.gz
- Pipes et awk pour formatage

#### 💪 Réalisations :
- check_file.sh : Vérification intelligente de fichiers
- list_files.sh : Inventaire automatique du projet
- backup_auto.sh : Système de backup professionnel avec horodatage

#### 🎯 Scripts créés (5 au total) :
1. system_check.sh (708B)
2. check_file.sh (808B)
3. list_files.sh (723B)
4. backup_auto.sh (1,6K) ⭐
5. deploy.sh (préparé pour la suite)

#### 📊 Statistiques projet :
- 6 dossiers organisés
- 9 fichiers
- 2 backups automatiques créés
- Total scripts : ~4KB de code Bash

#### 🔥 Moment fort :
Mon script de backup fonctionne parfaitement ! J'ai compris les conditions,
les boucles et les arguments. Je peux maintenant créer des outils utiles.

#### ⏱️ Temps : 1h45 (dans l'objectif de 2h/jour)

#### 🎯 Prochaine étape :
Jour 3 : Git professionnel + GitHub
### Jour 3 - 16 Janvier 2026 ✅ VALIDÉ

#### ✅ Compétences acquises :
- Configuration Git (user.name, user.email, init.defaultbranch)
- Authentification SSH avec GitHub (clés ed25519)
- Workflow Git complet (init, add, status, commit, push, pull, log)
- .gitignore pour exclusion de fichiers
- README.md professionnel en Markdown
- Messages de commit descriptifs et professionnels
- Analyse de repo avec git log

#### 💪 Réalisations majeures :
- ✅ Premier repo GitHub public créé et en ligne
- ✅ README professionnel visible sur github.com/mehdisamsar-devops
- ✅ 2 commits avec messages clairs
- ✅ Script git_stats.sh pour analyser l'historique Git
- ✅ Portfolio DevOps accessible aux recruteurs
- ✅ 13 fichiers sous contrôle de version

#### 🎯 Commandes Git maîtrisées (15) :
git init, config, add, commit, push, pull, status, log, remote, 
branch, clone, ls-files, --oneline, -v, --list

#### 📊 Statistiques Git :
- Commits : 2
- Fichiers trackés : 13
- Branches : 1 (main)
- Remote : SSH configuré

#### 🔗 Portfolio en ligne :
GitHub : https://github.com/mehdisamsar-devops/devops-bootcamp
Public : Oui (visible par recruteurs)

#### 🤔 Leçon importante :
Toujours faire "git status" avant "git commit" pour vérifier que 
les fichiers sont bien en staging (verts). J'ai oublié le "git add" 
une fois, mais j'ai compris mon erreur immédiatement.

#### ⏱️ Temps : 2h (respect du planning)

#### 🔥 Moment fort :
MON CODE EST EN LIGNE ! Mon portfolio GitHub est visible publiquement.
Les recruteurs en Arabie Saoudite peuvent maintenant voir mon travail.
C'est concret, c'est réel, c'est professionnel !

---

## 📈 Bilan Semaine 1 (Jours 1-3)

**Compétences acquises :** 40+ commandes (Linux + Git)
**Scripts créés :** 6 scripts Bash fonctionnels
**Lignes de code :** ~150 lignes de Bash
**Commits Git :** 2
**Temps investi :** 6h (3 jours × 2h)
**Objectif respecté :** 100% ✅

**Prochaine étape :** Jour 4-5 - Python pour DevOps
### Jour 4 - 17 Janvier 2026 ✅ VALIDÉ

#### ✅ Compétences acquises :
- Python syntax complète (variables, types, structures)
- Conditions (if/elif/else) et boucles (for/while)
- Fonctions avec paramètres, return, docstrings
- Modules et imports (création de utils.py réutilisable)
- Manipulation fichiers (modes r/w/a, context managers)
- Format JSON (dump, load, structures complexes)
- Librairie psutil pour monitoring système
- Classes Python (Colors)
- Gestion d'erreurs (try/except)
- Formatage et affichage professionnel

#### 💪 Réalisations majeures :
- ✅ 9 scripts Python fonctionnels
- ✅ Module utils.py réutilisable
- ✅ Rapports automatiques (TXT + JSON)
- ✅ Dashboard JSON
- ✅ **system_monitor.py** : Outil de monitoring professionnel
  - Surveillance CPU, RAM, Disque, Réseau
  - Top 5 processus
  - Système d'alertes avec seuils
  - Génération JSON + Logs horodatés
  - Affichage coloré terminal

#### 📊 Scripts créés (9) :
1. basics.py - Variables, types, structures
2. conditions.py - Logique conditionnelle
3. loops.py - Boucles et itérations
4. functions.py - Fonctions réutilisables
5. utils.py - Module d'utilitaires
6. use_utils.py - Démonstration imports
7. file_operations.py - Manipulation fichiers
8. json_operations.py - Manipulation JSON
9. system_monitor.py - Monitoring système (OUTIL PRO) ⭐

#### 📁 Fichiers générés (6) :
- devops_log.txt, rapport_bootcamp.txt
- bootcamp_data.json, dashboard.json
- monitoring_report.json, system_monitor.log

#### 🎯 Métriques système surveillées :
- CPU: 20.4% (4 cœurs @ 2000 MHz)
- RAM: 70.9% (8 GB total)
- Disque: 21.8% (167 GB total)
- Réseau: 729 MB envoyés / 1254 MB reçus
- Statut: Aucune alerte - Système OK ✅

#### 💡 Outil DevOps vs développeur :
Différence clé apprise : En DevOps, Python sert à automatiser
l'infrastructure (monitoring, déploiement, configuration) plutôt
qu'à développer des applications. system_monitor.py est un exemple
parfait d'outil qu'un DevOps crée et utilise quotidiennement.

#### 🔧 Workflow :
Passage de nano à VSCode pour meilleure productivité :
- Indentation automatique
- Détection erreurs en temps réel
- Coloration syntaxe
- Terminal intégré

#### ⏱️ Temps : 2h30 (dépassement de 30min à cause du setup VSCode - investi pour la suite)

#### 🔥 Moment fort :
J'AI CRÉÉ UN VRAI OUTIL DE MONITORING DEVOPS ! Ce n'est plus juste
de l'apprentissage, c'est un outil que je pourrais utiliser sur de
vrais serveurs. system_monitor.py surveille mon Mac en temps réel,
génère des rapports JSON, log les métriques. C'est exactement ce
que font les DevOps en production !

#### 🚀 Prochaine étape :
Jour 5 : Python avancé - APIs, requests, automation scripts