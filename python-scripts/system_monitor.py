#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
System Monitor - Outil de monitoring DevOps
Auteur : Mehdi Samsar
Date : 17 Janvier 2026
"""

import psutil
import json
from datetime import datetime

# Configuration
SEUIL_CPU = 80
SEUIL_RAM = 85
SEUIL_DISQUE = 90

# Couleurs
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def get_cpu_info():
    """Récupère les informations CPU"""
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count()
    cpu_freq = psutil.cpu_freq()
    
    # Sur Mac, cpu_freq peut être None
    if cpu_freq and cpu_freq.current:
        freq_mhz = round(cpu_freq.current, 2)
    else:
        freq_mhz = 0
    
    return {
        "utilisation_pourcent": cpu_percent,
        "nombre_coeurs": cpu_count,
        "frequence_mhz": freq_mhz,
        "status": "OK" if cpu_percent < SEUIL_CPU else "ALERTE"
    }

def get_memory_info():
    """Récupère les informations mémoire"""
    mem = psutil.virtual_memory()
    
    return {
        "total_gb": round(mem.total / (1024**3), 2),
        "utilisee_gb": round(mem.used / (1024**3), 2),
        "disponible_gb": round(mem.available / (1024**3), 2),
        "utilisation_pourcent": mem.percent,
        "status": "OK" if mem.percent < SEUIL_RAM else "ALERTE"
    }

def get_disk_info():
    """Récupère les informations disque"""
    disk = psutil.disk_usage('/')
    
    return {
        "total_gb": round(disk.total / (1024**3), 2),
        "utilise_gb": round(disk.used / (1024**3), 2),
        "libre_gb": round(disk.free / (1024**3), 2),
        "utilisation_pourcent": disk.percent,
        "status": "OK" if disk.percent < SEUIL_DISQUE else "ALERTE"
    }

def get_network_info():
    """Récupère les informations réseau"""
    net = psutil.net_io_counters()
    
    return {
        "bytes_envoyes_mb": round(net.bytes_sent / (1024**2), 2),
        "bytes_recus_mb": round(net.bytes_recv / (1024**2), 2),
        "paquets_envoyes": net.packets_sent,
        "paquets_recus": net.packets_recv
    }

def get_top_processes(n=5):
    """Récupère les N processus qui consomment le plus de CPU"""
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            pinfo = proc.info
            cpu_pct = pinfo['cpu_percent'] if pinfo['cpu_percent'] is not None else 0.0
            mem_pct = pinfo['memory_percent'] if pinfo['memory_percent'] is not None else 0.0

            processes.append({
                "pid": pinfo['pid'],
                "nom": pinfo['name'],
                "cpu_pourcent": cpu_pct,
                "ram_pourcent": round(mem_pct, 2)
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    processes.sort(key=lambda x: x['cpu_pourcent'], reverse=True)
    return processes[:n]

def print_banner():
    """Affiche le bandeau de démarrage"""
    separator = "=" * 60
    timestamp = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    
    print("\n" + Colors.CYAN + Colors.BOLD + separator)
    print("  SYSTEM MONITOR - DEVOPS TOOL")
    print(separator + Colors.RESET + "\n")
    print(Colors.BLUE + "Date : " + timestamp + Colors.RESET)
    print(Colors.BLUE + "Monitoring par : Mehdi Samsar" + Colors.RESET + "\n")

def print_metric(label, value, unit, status, percentage=None):
    """Affiche une métrique avec couleur selon status"""
    color = Colors.GREEN if status == "OK" else Colors.RED
    status_icon = "OK" if status == "OK" else "ALERTE"
    
    if percentage is not None:
        line = "[" + status_icon + "] " + label.ljust(20) + " : " + str(value) + " " + unit + " (" + str(percentage) + "%)"
    else:
        line = "      " + label.ljust(20) + " : " + str(value) + " " + unit
    
    print(color + line + Colors.RESET)

def display_monitoring_report(data):
    """Affiche le rapport de monitoring formaté"""
    print_banner()
    
    # CPU
    print(Colors.BOLD + "CPU" + Colors.RESET)
    print("-" * 60)
    cpu = data['cpu']
    print_metric("Utilisation", cpu['utilisation_pourcent'], "%", cpu['status'], cpu['utilisation_pourcent'])
    print_metric("Nombre de coeurs", cpu['nombre_coeurs'], "cores", "OK")
    print_metric("Frequence", cpu['frequence_mhz'], "MHz", "OK")
    print()
    
    # MEMOIRE
    print(Colors.BOLD + "MEMOIRE RAM" + Colors.RESET)
    print("-" * 60)
    mem = data['memoire']
    print_metric("Total", mem['total_gb'], "GB", "OK")
    print_metric("Utilisee", mem['utilisee_gb'], "GB", mem['status'], mem['utilisation_pourcent'])
    print_metric("Disponible", mem['disponible_gb'], "GB", "OK")
    print()
    
    # DISQUE
    print(Colors.BOLD + "DISQUE" + Colors.RESET)
    print("-" * 60)
    disk = data['disque']
    print_metric("Total", disk['total_gb'], "GB", "OK")
    print_metric("Utilise", disk['utilise_gb'], "GB", disk['status'], disk['utilisation_pourcent'])
    print_metric("Libre", disk['libre_gb'], "GB", "OK")
    print()
    
    # RESEAU
    print(Colors.BOLD + "RESEAU" + Colors.RESET)
    print("-" * 60)
    net = data['reseau']
    print_metric("Donnees envoyees", net['bytes_envoyes_mb'], "MB", "OK")
    print_metric("Donnees recues", net['bytes_recus_mb'], "MB", "OK")
    print()
    
    # TOP PROCESSUS
    print(Colors.BOLD + "TOP 5 PROCESSUS (CPU)" + Colors.RESET)
    print("-" * 60)
    for i, proc in enumerate(data['top_processus'], 1):
        cpu_val = proc['cpu_pourcent']
        ram_val = proc['ram_pourcent']
        nom = proc['nom'][:25]
        
        if cpu_val > 50:
            color = Colors.RED
        elif cpu_val > 20:
            color = Colors.YELLOW
        else:
            color = Colors.GREEN
        
        line = str(i) + ". " + nom.ljust(25) + " | CPU: " + format(cpu_val, '5.1f') + "% | RAM: " + format(ram_val, '5.2f') + "%"
        print(color + line + Colors.RESET)
    print()
    
    # ALERTES
    alertes = data['alertes']
    if alertes:
        print(Colors.RED + Colors.BOLD + "ALERTES ACTIVES" + Colors.RESET)
        print("-" * 60)
        for alerte in alertes:
            print(Colors.RED + alerte + Colors.RESET)
        print()

def generate_monitoring_data():
    """Génère toutes les données de monitoring"""
    data = {
        "timestamp": datetime.now().isoformat(),
        "timestamp_readable": datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
        "cpu": get_cpu_info(),
        "memoire": get_memory_info(),
        "disque": get_disk_info(),
        "reseau": get_network_info(),
        "top_processus": get_top_processes(5),
        "alertes": []
    }
    
    # Générer alertes
    if data['cpu']['status'] == "ALERTE":
        cpu_pct = data['cpu']['utilisation_pourcent']
        msg = "CPU eleve : " + str(cpu_pct) + "% (seuil: " + str(SEUIL_CPU) + "%)"
        data['alertes'].append(msg)
    
    if data['memoire']['status'] == "ALERTE":
        ram_pct = data['memoire']['utilisation_pourcent']
        msg = "RAM elevee : " + str(ram_pct) + "% (seuil: " + str(SEUIL_RAM) + "%)"
        data['alertes'].append(msg)
    
    if data['disque']['status'] == "ALERTE":
        disk_pct = data['disque']['utilisation_pourcent']
        msg = "Disque plein : " + str(disk_pct) + "% (seuil: " + str(SEUIL_DISQUE) + "%)"
        data['alertes'].append(msg)
    
    return data

def save_json_report(data, filename="monitoring_report.json"):
    """Sauvegarde le rapport en JSON"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(Colors.GREEN + "Rapport JSON sauvegarde : " + filename + Colors.RESET + "\n")

def save_log(data, logfile="system_monitor.log"):
    """Ajoute une entrée dans le fichier de log"""
    with open(logfile, 'a', encoding='utf-8') as f:
        timestamp = data['timestamp_readable']
        cpu = data['cpu']['utilisation_pourcent']
        ram = data['memoire']['utilisation_pourcent']
        disk = data['disque']['utilisation_pourcent']
        alertes = len(data['alertes']) 
        log_line = "[" + timestamp + "] CPU:" + format(cpu, '5.1f') + "% | RAM:" + format(ram, '5.1f') + "% | DISK:" + format(disk, '5.1f') + "% | Alertes:" + str(alertes) + "\n"
        f.write(log_line)
    
    print(Colors.GREEN + "Log ajoute : " + logfile + Colors.RESET)

def main():
    """Fonction principale"""
    # Générer les données
    data = generate_monitoring_data()
    
    # Afficher le rapport
    display_monitoring_report(data)
    
    # Sauvegarder JSON
    save_json_report(data)
    
    # Sauvegarder log
    save_log(data)
    
    # Résumé
    separator = "=" * 60
    print(Colors.CYAN + separator)
    print("  RESUME")
    print(separator + Colors.RESET)
    
    if not data['alertes']:
        status = Colors.GREEN + "Systeme OK" + Colors.RESET
    else:
        nb_alertes = len(data['alertes'])
        status = Colors.RED + str(nb_alertes) + " alerte(s)" + Colors.RESET
    
    print("Status general : " + status)
    print("Fichiers crees : monitoring_report.json, system_monitor.log")
    print(Colors.CYAN + separator + Colors.RESET + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n" + Colors.YELLOW + "Monitoring interrompu" + Colors.RESET)
    except Exception as e:
        print("\n" + Colors.RED + "Erreur : " + str(e) + Colors.RESET)


