#!/bin/bash

# Lister tous les fichiers du projet avec détails

echo "=================================="
echo "  INVENTAIRE DU PROJET"
echo "=================================="
echo ""

cd ~/devops-bootcamp/projet-web

# Compter les dossiers
NB_DOSSIERS=$(find . -type d | wc -l)
echo "📁 Nombre de dossiers : $NB_DOSSIERS"

# Compter les fichiers
NB_FICHIERS=$(find . -type f | wc -l)
echo "📄 Nombre de fichiers : $NB_FICHIERS"

echo ""
echo "📋 Liste des fichiers :"
echo "-----------------------------------"

# Boucle sur tous les fichiers
for fichier in $(find . -type f); do
    TAILLE=$(ls -lh "$fichier" | awk '{print $5}')
    echo "  - $fichier ($TAILLE)"
done

echo "=================================="
