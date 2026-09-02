-- Create a new table 'Type_chambre' with a primary key and columns
CREATE TABLE
    Type_Chambre (
        id_type SERIAL PRIMARY KEY,
        nom_type VARCHAR(50) not null CHECK (nom_type in ('simple', 'familiale')),
        prix DECIMAL(10, 2) NOT NULL
    );

CREATE TABLE
    Chambre (
        id SERIAL PRIMARY KEY,
        num_chambre VARCHAR(10) NOT NULL UNIQUE,
        etage int not NULL,
        id_type int not null REFERENCES Type_Chambre(id_type),
        statut VARCHAR(20) NOT NULL check ( statut in ('disponible','occupée','réservée','maintenance'))
    );

CREATE TABLE
    Client (
        id_client VARCHAR(15) PRIMARY KEY,
        nom VARCHAR(100) not null,
        mail VARCHAR(100) not null UNIQUE,
        pays char(2) not NULL,
        birthdate DATE,
        type_client VARCHAR(15) not null check(type_client in ('VIP','particulier','entreprise'))
    );
CREATE TABLE
    reservation (
        id_reservation SERIAL PRIMARY KEY,
        id_client VARCHAR(15) not null REFERENCES client(id_client),
        id_chambre int not null references chambre(id),
        date_reservation DATE not null,
        date_arrivee_prevue DATE not null,
        date_depart_prevue DATE not null,
        nbre_personne int NOT NULL CHECK (nbre_personne>0 and nbre_personne<=7),
        statut VARCHAR(20) NOT NULL CHECK (statut in ('attente','confirmée','annulée'))
    );
CREATE TABLE
    sejour (
        id SERIAL PRIMARY KEY,
        id_reservation int not null UNIQUE references  reservation(id_reservation),
        date_arrivee DATE not null,
        date_depart DATE
    );
CREATE TABLE
    paiement (
        id_paiement SERIAL PRIMARY KEY,
        id_reservation int not null references reservation(id_reservation),
        montant DECIMAL(10, 2) NOT NULL check(montant>0),
        date_paiement DATE NOT NULL,
        moyen_paiement VARCHAR(20) NOT NULL check(moyen_paiement in ('carte','espèce','mobile money')),
        statut_paiement VARCHAR(20) NOT NULL check(statut_paiement in ('attente','validé','remboursé','echoué'))
    );



