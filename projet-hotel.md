# 🏨 Projet : Système de gestion d'un hôtel

## 1. Contexte

Un hôtel souhaite informatiser la gestion de ses activités afin de centraliser les informations concernant :

- les clients ;
- les chambres ;
- les réservations ;
- les séjours ;
- les paiements ;
- les services proposés ;
- le personnel ;
- les différentes catégories de chambres ;
- les équipements ;
- les factures.

Le système devra permettre à l'hôtel de gérer son activité quotidienne tout en conservant un historique des opérations.

---

## 2. Objectifs du système

L'application doit permettre de :

1. gérer les clients ;
2. gérer les chambres ;
3. gérer les catégories/types de chambres ;
4. gérer les réservations ;
5. gérer les arrivées et départs ;
6. gérer les paiements ;
7. gérer les factures ;
8. gérer les services supplémentaires ;
9. associer des services aux séjours ;
10. gérer le personnel ;
11. gérer les équipements des chambres ;
12. suivre l'état des chambres ;
13. conserver l'historique des séjours et réservations.

---

## 3. Gestion des clients 👤

Un client peut être une personne physique souhaitant séjourner dans l'hôtel.

Pour chaque client, l'hôtel souhaite conserver notamment :

- son identité ;
- ses coordonnées ;
- ses informations de contact ;
- ses informations d'identification ;
- sa date d'inscription ;
- son statut.

Un client peut effectuer plusieurs réservations au cours du temps.

Une réservation est associée à un client principal.

Le système doit conserver l'historique des réservations d'un client.

---

## 4. Gestion des chambres 🛏️

L'hôtel possède plusieurs chambres.

Chaque chambre possède notamment :

- un numéro ;
- un étage ;
- une capacité maximale ;
- un état ;
- une catégorie ;
- un prix de base.

Une chambre appartient à une seule catégorie.

Une catégorie peut concerner plusieurs chambres.

Exemples de catégories :

- Simple ;
- Double ;
- Suite ;
- Deluxe ;
- Familiale.

L'état d'une chambre peut évoluer, par exemple :

- disponible ;
- occupée ;
- en nettoyage ;
- en maintenance ;
- hors service.

Le système doit éviter qu'une chambre soit réservée par deux clients pour des périodes qui se chevauchent.

---

## 5. Gestion des catégories de chambres

Chaque catégorie possède :

- un nom ;
- une description ;
- une capacité ;
- un tarif de base ;
- éventuellement certaines caractéristiques.

Une catégorie peut être associée à plusieurs chambres.

Le tarif de base peut servir de référence lors d'une réservation.

---

## 6. Gestion des réservations 📅

Un client peut effectuer une ou plusieurs réservations.

Une réservation doit notamment contenir :

- une date de réservation ;
- une date prévue d'arrivée ;
- une date prévue de départ ;
- le nombre de personnes ;
- le statut ;
- le montant prévu ;
- des remarques éventuelles.

Une réservation peut concerner une ou plusieurs chambres.

Une chambre peut être concernée par plusieurs réservations, mais pas pour des périodes qui se chevauchent.

Une réservation peut avoir différents statuts :

- en attente ;
- confirmée ;
- annulée ;
- terminée ;
- no-show.

Le système doit conserver les réservations annulées et terminées.

---

## 7. Gestion des occupants

Une réservation peut concerner plusieurs personnes.

Le client ayant effectué la réservation n'est pas nécessairement la seule personne qui séjournera dans l'hôtel.

Exemple :

> Jean réserve une chambre pour lui, sa femme et ses deux enfants.

Le système doit donc permettre d'enregistrer les différentes personnes occupant une chambre pendant un séjour.

---

## 8. Gestion des séjours 🏨

Lorsqu'un client arrive réellement à l'hôtel, la réservation devient un séjour effectif.

Le système doit enregistrer :

- la date et heure réelle d'arrivée ;
- la date et heure réelle de départ ;
- les chambres effectivement occupées ;
- les occupants ;
- les remarques ;
- le statut du séjour.

Un séjour peut être associé à une réservation.

Cependant, le système doit également pouvoir gérer les situations où un séjour est créé directement à l'hôtel sans réservation préalable.

---

## 9. Gestion des services 🧃

L'hôtel propose différents services supplémentaires.

Exemples :

- petit-déjeuner ;
- restaurant ;
- room service ;
- blanchisserie ;
- spa ;
- parking ;
- transport ;
- minibar.

Pour chaque service, l'hôtel souhaite conserver :

- son nom ;
- sa description ;
- son prix ;
- sa disponibilité ;
- sa catégorie éventuelle.

Un séjour peut utiliser plusieurs services.

Un service peut être utilisé par plusieurs séjours.

Le système doit enregistrer :

- le service utilisé ;
- la quantité ;
- la date ;
- le prix appliqué au moment de la consommation ;
- éventuellement l'employé ayant enregistré la consommation.

Le prix actuel du service peut changer. L'historique doit néanmoins conserver le prix réellement payé.

---

## 10. Gestion des paiements 💳

Un séjour peut donner lieu à plusieurs paiements.

Exemple :

> Client → acompte → paiement partiel → solde final.

Chaque paiement doit contenir notamment :

- montant ;
- date ;
- moyen de paiement ;
- statut ;
- référence de transaction éventuelle.

Les moyens de paiement peuvent être :

- espèces ;
- carte bancaire ;
- mobile money ;
- virement ;
- autre.

Un paiement appartient à un seul dossier de séjour/facturation.

---

## 11. Gestion des factures 🧾

L'hôtel doit pouvoir générer une facture pour un séjour.

Une facture doit notamment contenir :

- numéro de facture ;
- date ;
- montant hors taxe ;
- taxes ;
- montant total ;
- statut ;
- date d'échéance éventuelle.

Une facture peut regrouper :

- les nuits ;
- les services ;
- les taxes ;
- les réductions ;
- autres frais éventuels.

Le système doit permettre de connaître le détail du montant facturé.

---

## 12. Gestion des employés 👨‍💼

L'hôtel possède plusieurs employés.

Un employé peut avoir :

- nom ;
- prénom ;
- coordonnées ;
- date d'embauche ;
- poste ;
- salaire ;
- statut.

Exemples de postes :

- réceptionniste ;
- manager ;
- concierge ;
- agent d'entretien ;
- responsable maintenance ;
- comptable.

Un employé appartient à un service/département de l'hôtel.

Un département peut avoir plusieurs employés.

---

## 13. Gestion des équipements 🔧

Les chambres peuvent posséder différents équipements.

Exemples :

- télévision ;
- climatisation ;
- réfrigérateur ;
- coffre-fort ;
- Wi-Fi ;
- baignoire ;
- sèche-cheveux.

Un équipement peut être présent dans plusieurs chambres.

Une chambre peut posséder plusieurs équipements.

Le système doit donc permettre de gérer ces associations.

Pour chaque association chambre-équipement, on pourrait avoir des informations supplémentaires comme :

- quantité ;
- date d'installation ;
- état ;
- date de dernière vérification.

À déterminer lors de la conception si ces informations appartiennent à l'équipement lui-même ou à son association avec une chambre.

---

## 14. Maintenance 🛠️

Une chambre peut nécessiter des interventions de maintenance.

Le système doit conserver l'historique des interventions :

- chambre concernée ;
- employé/responsable ;
- date ;
- problème rencontré ;
- description ;
- coût ;
- statut ;
- date de résolution.

Une chambre peut avoir plusieurs interventions de maintenance.

---

## 15. Promotions et réductions 🎟️

L'hôtel peut proposer des promotions.

Une promotion peut avoir :

- un nom ;
- une description ;
- un pourcentage ou montant de réduction ;
- une date de début ;
- une date de fin ;
- des conditions d'application ;
- un statut.

Une réservation peut éventuellement bénéficier d'une promotion.

Le système doit conserver la réduction réellement appliquée à la réservation.

---

## 16. Règles métier importantes

### Réservations

- Une réservation appartient à un client.
- Une réservation peut concerner plusieurs chambres.
- Une chambre peut avoir plusieurs réservations dans le temps.
- Deux réservations confirmées ne doivent pas occuper la même chambre pendant la même période.
- Une réservation annulée ne doit pas bloquer une chambre.

### Chambres

- Une chambre appartient à une seule catégorie.
- Une catégorie possède plusieurs chambres.
- Une chambre peut être temporairement indisponible.
- Une chambre en maintenance ne doit pas être attribuée à un nouveau séjour.

### Séjours

- Un séjour peut provenir d'une réservation.
- Un séjour peut également être créé sans réservation.
- Un séjour possède une date d'arrivée réelle.
- Un séjour peut posséder plusieurs occupants.
- Un séjour peut utiliser plusieurs services.

### Services

- Un service peut être consommé plusieurs fois.
- La quantité consommée doit être conservée.
- Le prix payé doit être conservé même si le prix du service change plus tard.

### Paiements

- Un séjour peut avoir plusieurs paiements.
- Un paiement ne peut appartenir qu'à un seul dossier.
- La somme des paiements doit pouvoir être comparée au montant dû.

### Équipements

- Une chambre peut avoir plusieurs équipements.
- Un équipement peut être installé dans plusieurs chambres.
- L'état d'un équipement doit pouvoir être suivi.

---

## 17. Contraintes supplémentaires

Le système devra gérer :

### Intégrité

- identifiants uniques ;
- clés primaires ;
- clés étrangères ;
- contraintes `NOT NULL` ;
- contraintes `UNIQUE` ;
- contraintes `CHECK`.

### Cohérence

Exemples de contraintes possibles :

```text
date_depart > date_arrivee
```
