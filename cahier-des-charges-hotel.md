# Cahier des Charges — Système de Gestion d'un Hôtel

## 1. Contexte

L'hôtel souhaite mettre en place un système permettant de gérer ses clients, ses chambres, les réservations, les séjours, les paiements et les services proposés.

Le système doit permettre de centraliser les informations et de faciliter la gestion quotidienne de l'hôtel.

---

## 2. Objectif du système

Le système doit permettre de :

- Gérer les clients.
- Gérer les chambres et leurs caractéristiques.
- Gérer les types de chambres.
- Enregistrer et suivre les réservations.
- Gérer les arrivées et les départs des clients.
- Enregistrer les paiements.
- Gérer les services proposés par l'hôtel.
- Suivre les services consommés par les clients.
- Connaître la disponibilité des chambres.
- Conserver l'historique des séjours.

---

## 3. Acteurs

### Client

Le client peut :

- Effectuer une réservation.
- Séjourner dans une chambre.
- Utiliser les services de l'hôtel.
- Effectuer des paiements.

### Réceptionniste

Le réceptionniste peut :

- Enregistrer les clients.
- Créer, modifier et annuler des réservations.
- Attribuer une chambre à un client.
- Enregistrer les arrivées et les départs.
- Enregistrer les paiements.
- Enregistrer les services consommés.

### Administrateur

L'administrateur peut :

- Gérer les chambres.
- Gérer les types de chambres.
- Gérer les services.
- Gérer les utilisateurs du système.
- Consulter les informations et statistiques de l'hôtel.

### Personnel de l'hôtel

Le personnel peut intervenir dans la gestion de certains services ou opérations de l'hôtel.

---

## 4. Contraintes métier

- Un client peut effectuer plusieurs réservations.
- Une réservation concerne au moins une chambre.
- Une chambre appartient à un seul type de chambre.
- Un type de chambre peut correspondre à plusieurs chambres.
- Une chambre ne peut pas être réservée par plusieurs clients pour la même période.
- Une réservation possède une date d'arrivée prévue et une date de départ prévue.
- Une réservation peut être annulée.
- Un client peut effectuer plusieurs séjours au cours du temps.
- Un séjour correspond à une réservation confirmée et réalisée.
- Un séjour possède une date d'arrivée réelle et une date de départ réelle.
- Un client peut utiliser plusieurs services pendant son séjour.
- Un service peut être utilisé par plusieurs clients.
- Chaque paiement est associé à une réservation ou à un séjour.
- Une réservation peut être réglée en plusieurs paiements.
- Les chambres peuvent avoir différents statuts : disponible, occupée, réservée, maintenance, etc.
- Le prix d'une chambre dépend de son type et peut évoluer dans le temps.
- Les informations importantes d'une réservation doivent être conservées même après son annulation ou sa clôture.

---

## 5. Informations à gérer

### Clients

Le système doit conserver notamment :

- Identifiant
- Nom
- Prénom
- Téléphone
- Email
- Adresse
- Date de naissance

### Chambres

Le système doit conserver notamment :

- Numéro de chambre
- Étage
- Type de chambre
- Statut
- Prix

### Types de chambres

Exemples :

- Simple
- Double
- Suite
- Familiale

### Réservations

Le système doit conserver :

- Client
- Chambre
- Date de réservation
- Date d'arrivée prévue
- Date de départ prévue
- Nombre de personnes
- Statut de la réservation

### Séjours

Le système doit conserver :

- Réservation concernée
- Date d'arrivée réelle
- Date de départ réelle
- Chambre occupée

### Paiements

Le système doit conserver :

- Montant
- Date
- Moyen de paiement
- Statut du paiement

### Services

Exemples :

- Petit-déjeuner
- Restaurant
- Blanchisserie
- Wi-Fi premium
- Spa
- Transport

Le système doit permettre de connaître quels services ont été utilisés, par quel client et à quelle date.

---

## 6. Fonctionnalités principales

Le système doit permettre de :

1. Ajouter, modifier, supprimer et consulter un client.
2. Ajouter, modifier et consulter une chambre.
3. Gérer les types de chambres.
4. Vérifier la disponibilité des chambres.
5. Créer une réservation.
6. Modifier ou annuler une réservation.
7. Enregistrer l'arrivée d'un client.
8. Enregistrer son départ.
9. Enregistrer un ou plusieurs paiements.
10. Ajouter des services consommés pendant un séjour.
11. Consulter l'historique d'un client.
12. Consulter l'occupation des chambres.
13. Consulter les réservations selon une période.
14. Consulter les revenus générés par les réservations et services.

---

## 7. Résultat attendu

Le système doit permettre à l'hôtel de disposer d'une base de données fiable et structurée pour gérer l'ensemble de ses activités liées aux clients, chambres, réservations, séjours, paiements et services.

La base de données devra être correctement normalisée et respecter les règles d'intégrité des données.
