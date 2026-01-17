#!/usr/bin/env python3

"""
Modules utilitaires DevOps
Fonctions réutilisables pour l'automatisation
"""

import os
from datetime import datetime

def get_timestamp():
    """Retourne un timestamp formaté"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_file_size(filepath):
    """Retourne la taille d'un fichier en bytes"""
    if os.path.exists(filepath):
        return os.path.getsize(filepath)
    return 0

def format_bytes(bytes):
    """Convertit bytes en format lisible (KB, MB, GB)"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes < 1024:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024
    return f"{bytes:.2f} TB"

def check_file_exists(filepath):
    """Vérifie si un fichier existe"""
    return os.path.exists(filepath)

def list_files_in_directory(directory, extension=None):
    """Liste les fichiers dans un dossier (optionnel: filtre par extension)"""
    if not os.path.exists(directory):
        return []
    
    files = []
    for item in os.listdir(directory):
        filepath = os.path.join(directory, item)
        if os.path.isfile(filepath):
            if extension:
                if item.endswith(extension):
                    files.append(item)
            else:
                files.append(item)
    return files

def create_banner(text, char="="):
    """Crée un bandeau décoratif"""
    length = len(text) + 4
    banner = f"{char * length}\n  {text}\n{char * length}"
    return banner
