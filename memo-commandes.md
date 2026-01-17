 MÉMO COMMANDES LINUX - DevOps Bootcamp
NAVIGATION
pwd                          # Afficher où je suis
cd dossier                   # Aller dans un dossier
cd ~                         # Aller au dossier personnel
cd ..                        # Remonter d'un niveau
cd -                         # Retourner au dossier précédent
LISTER / VOIR
ls                           # Lister les fichiers
ls -l                        # Liste détaillée
ls -a                        # Montrer fichiers cachés
ls -la                       # Tout montrer en détail
cat fichier.txt              # Afficher contenu d'un fichier
tree                         # Arborescence (si installé)
CRÉER / SUPPRIMER
mkdir dossier                # Créer un dossier
mkdir -p dossier/sous        # Créer avec sous-dossiers
touch fichier.txt            # Créer un fichier vide
rm fichier.txt               # Supprimer un fichier
rm -r dossier/               # Supprimer un dossier
rm -rf dossier/              # Supprimer FORCE (⚠️ DANGER)
COPIER / DÉPLACER / RENOMMER
cp source.txt copie.txt      # Copier un fichier
cp -r dossier/ copie/        # Copier un dossier
mv fichier.txt backup/       # Déplacer un fichier
mv ancien.txt nouveau.txt    # Renommer un fichier
RECHERCHER
find . -name "*.txt"         # Chercher fichiers .txt
find . -type f               # Chercher tous les fichiers
find . -type d               # Chercher tous les dossiers
ÉCRIRE DANS UN FICHIER
echo "texte"                 # Afficher du texte
echo "texte" > fichier.txt   # Écrire (écrase le contenu)
echo "texte" >> fichier.txt  # Ajouter à la fin du fichier
PERMISSIONS
chmod +x script.sh           # Rendre un fichier exécutable
chmod 755 fichier            # Permissions complètes
ls -l fichier                # Voir les permissions d'un fichier
SYSTÈME & PROCESSUS
whoami                       # Mon nom d'utilisateur
date                         # Date et heure actuelles
df -h                        # Espace disque disponible
top                          # Processus actifs (Q pour quitter)
ps aux                       # Liste tous les processus
kill 1234                    # Arrêter un processus (par son ID)
RACCOURCIS CLAVIER
Tab                          # Auto-complétion
↑ / ↓                        # Historique des commandes
Ctrl + C                     # Annuler commande en cours
Ctrl + L                     # Effacer l'écran (ou taper: clear)
Ctrl + A                     # Aller au début de la ligne
Ctrl + E                     # Aller à la fin de la ligne
Ctrl + U                     # Effacer toute la ligne
SYMBOLES SPÉCIAUX
~                            # Dossier personnel (/Users/tonnom)
.                            # Dossier actuel
..                           # Dossier parent (un niveau au-dessus)
/                            # Racine du système


                       # N'importe quoi (wildcard)



                       # Redirection (écrase)

                      # Redirection (ajoute)


|                            # Pipe (enchaîner des commandes)
BASH SCRIPT
#!/bin/bash                  # Première ligne d'un script (shebang)
$(commande)                  # Exécuter une commande dans un script
chmod +x script.sh           # Rendre le script exécutable
./script.sh                  # Exécuter un script
HOMEBREW (Mac)
brew install tree            # Installer un programme
brew update                  # Mettre à jour Homebrew
brew list                    # Voir programmes installés
AIDE
man ls                       # Manuel d'une commande
ls --help                    # Aide rapide
history                      # Historique des commandes
COMMANDES DANGEREUSES - NE JAMAIS FAIRE
rm -rf /                     # ❌ DÉTRUIT TON SYSTÈME
rm -rf ~                     # ❌ DÉTRUIT TON DOSSIER PERSONNEL
chmod -R 777 /               # ❌ CASSE LES PERMISSIONS
EXEMPLES PRATIQUES COMBINÉS
mkdir projet && cd projet && touch README.md && ls -la
find . -name "*.txt" | wc -l
ls -la > liste-fichiers.txt
tail -10 fichier.log
grep "erreur" fichier.log
LES 10 COMMANDES LES PLUS UTILISÉES (80% du temps)
pwd              # Où suis-je ?
ls -la           # Qu'est-ce qu'il y a ici ?
cd dossier       # Aller quelque part
mkdir            # Créer dossier
touch            # Créer fichier
cp               # Copier
mv               # Déplacer/Renommer
rm               # Supprimer
cat              # Lire fichier
find             # Chercher
