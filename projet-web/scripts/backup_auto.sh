#!/bin/bash

# Script de backup automatique
# Auteur : Mehdi Samsar
# Date : 16 Janvier 2026

# Couleurs pour l'affichage
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Configuration
SOURCE_DIR="$HOME/devops-bootcamp/projet-web"
BACKUP_DIR="$HOME/devops-bootcamp/backups"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_NAME="backup_$DATE.tar.gz"

echo "=================================="
echo "   🔄 BACKUP AUTOMATIQUE"
echo "=================================="
echo ""

# Vérifier que le dossier source existe
if [ ! -d "$SOURCE_DIR" ]; then
    echo -e "${RED}❌ Erreur : Le dossier $SOURCE_DIR n'existe pas${NC}"
    exit 1
fi

# Créer le dossier de backup s'il n'existe pas
if [ ! -d "$BACKUP_DIR" ]; then
    echo -e "${YELLOW}📁 Création du dossier backups...${NC}"
    mkdir -p "$BACKUP_DIR"
fi

# Créer le backup
echo -e "${YELLOW}🔄 Création du backup...${NC}"
tar -czf "$BACKUP_DIR/$BACKUP_NAME" -C "$HOME/devops-bootcamp" projet-web

# Vérifier que le backup a réussi
if [ $? -eq 0 ]; then
    TAILLE=$(ls -lh "$BACKUP_DIR/$BACKUP_NAME" | awk '{print $5}')
    echo -e "${GREEN}✅ Backup créé avec succès !${NC}"
    echo ""
    echo "📦 Fichier : $BACKUP_NAME"
    echo "📊 Taille : $TAILLE"
    echo "📂 Emplacement : $BACKUP_DIR"
    echo ""
    
    # Lister tous les backups
    NB_BACKUPS=$(ls -1 "$BACKUP_DIR" | wc -l)
    echo "📋 Nombre total de backups : $NB_BACKUPS"
    echo ""
    echo "Liste des backups :"
    ls -lh "$BACKUP_DIR"
else
    echo -e "${RED}❌ Erreur lors de la création du backup${NC}"
    exit 1
fi

echo ""
echo "=================================="
