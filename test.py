#!/usr/bin/env python3
"""
Guide Complet du Module datetime en Python
===========================================
Tout ce qu'il faut savoir pour maîtriser les dates et heures en Python
"""

from datetime import datetime, date, time, timedelta, timezone
from datetime import datetime as dt
import time as time_module

print("=" * 70)
print("GUIDE COMPLET DU MODULE DATETIME")
print("=" * 70)

# =============================================================================
# 1. LES BASES - Obtenir la date et l'heure actuelles
# =============================================================================
print("\n📅 1. OBTENIR LA DATE ET L'HEURE ACTUELLES")
print("-" * 70)

maintenant = datetime.now()
print(f"datetime.now() : {maintenant}")
print(f"Type : {type(maintenant)}")

aujourd_hui = date.today()
print(f"\ndate.today() : {aujourd_hui}")
print(f"Type : {type(aujourd_hui)}")


# 2. CRÉER DES DATES ET HEURES SPÉCIFIQUES
# =============================================================================
print("\n\n📆 2. CRÉER DES DATES ET HEURES SPÉCIFIQUES")
print("-" * 70)

# Créer une date
ma_date = date(2024, 12, 25)
print(f"Date de Noël 2024 : {ma_date}")

# Créer une heure
mon_heure = time(14, 30, 45)
print(f"Heure spécifique : {mon_heure}")

# Créer un datetime complet
mon_datetime = datetime(2024, 12, 25, 14, 30, 45)
print(f"Datetime complet : {mon_datetime}")

# Avec microsecondes
avec_micro = datetime(2024, 12, 25, 14, 30, 45, 123456)
print(f"Avec microsecondes : {avec_micro}")


maintenant = datetime.now()
print(f"Date complète : {maintenant}")
print(f"  Année       : {maintenant.year}")
print(f"  Mois        : {maintenant.month}")
print(f"  Jour        : {maintenant.day}")
print(f"  Heure       : {maintenant.hour}")
print(f"  Minute      : {maintenant.minute}")
print(f"  Seconde     : {maintenant.second}")
print(f"  Microseconde: {maintenant.microsecond}")
print(f"  Jour semaine: {maintenant.weekday()} (0=lundi, 6=dimanche)")
print(f"  Numéro ISO  : {maintenant.isoweekday()} (1=lundi, 7=dimanche)")