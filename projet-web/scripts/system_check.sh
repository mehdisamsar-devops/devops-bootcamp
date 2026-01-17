#!/bin/bash

# Script de vérification système
# Auteur : Mehdi Samsar
# Date : 16 Janvier 2026

echo "=================================="
echo "   INFORMATIONS SYSTÈME"
echo "=================================="
echo ""

echo "📅 Date et heure :"
date
echo ""

echo "👤 Utilisateur actuel :"
whoami
echo ""

echo "📂 Dossier actuel :"
pwd
echo ""

echo "💾 Espace disque disponible :"
df -h ~
echo ""

echo "🖥️  Mémoire système :"
top -l 1 | grep PhysMem
echo ""

echo "📊 Nombre de fichiers dans le projet :"
find ~/devops-bootcamp/projet-web -type f | wc -l
echo ""

echo "=================================="
echo "   Vérification terminée !"
echo "=================================="
