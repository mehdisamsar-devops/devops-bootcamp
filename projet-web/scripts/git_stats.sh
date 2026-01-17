#!/bin/bash

# Script d'analyse Git
# Affiche des stats sur le repo

echo "=================================="
echo "   📊 GIT STATISTICS"
echo "=================================="
echo ""

# Nombre de commits
NB_COMMITS=$(git log --oneline | wc -l)
echo "📝 Nombre de commits : $NB_COMMITS"

# Dernier commit
echo ""
echo "🕐 Dernier commit :"
git log -1 --pretty=format:"%h - %s (%cr)" --abbrev-commit

# Nombre de fichiers trackés
NB_FICHIERS=$(git ls-files | wc -l)
echo ""
echo ""
echo "📁 Fichiers sous Git : $NB_FICHIERS"

# Branches
echo ""
echo "🌿 Branches :"
git branch

echo ""
echo "=================================="
