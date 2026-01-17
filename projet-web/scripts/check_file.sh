#!/bin/bash

# Script de vérification de fichier
# Usage: ./check_file.sh nom_fichier

# Vérifier qu'un argument est fourni
if [ -z "$1" ]; then
    echo "❌ Erreur : Aucun fichier spécifié"
    echo "Usage : ./check_file.sh nom_fichier"
    exit 1
fi

FICHIER=$1

# Vérifier si le fichier existe
if [ -f "$FICHIER" ]; then
    echo "✅ Le fichier $FICHIER existe"
    
    # Afficher des infos
    echo "📊 Taille : $(ls -lh "$FICHIER" | awk '{print $5}')"
    echo "📅 Dernière modification : $(ls -l "$FICHIER" | awk '{print $6, $7, $8}')"
    
    # Vérifier si exécutable
    if [ -x "$FICHIER" ]; then
        echo "🚀 Le fichier est exécutable"
    else
        echo "⚠️  Le fichier n'est pas exécutable"
    fi
else
    echo "❌ Le fichier $FICHIER n'existe pas"
    exit 1
fi
