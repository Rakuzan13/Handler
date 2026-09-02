
alter table type_chambre
alter COLUMN nom_type TYPE VARCHAR(50)  

-- Insert data into 'client'
INSERT INTO
    client (id_client,nom,mail,pays,birthdate,type_client)
VALUES
    ('cli-2026-000001','nathaniel brown','nath.br@gmail.com','deu','2003-06-20','particulier'),
    ('cli-2026-000002','rayana assi','raya.assi@gmail.com','civ','1998-09-14','entreprise'),
    ('cli-2026-000003','sabalenka aryna','aryn@gmail.com','blr','2000-08-12','VIP'),
    ('cli-2026-000004','novak djokovic','nole@gmail.com','svk','1987-05-22','VIP'),
    ('cli-2026-000005','tom brady','bradyt@gmail.com','usa','1997-08-03','particulier');

-- Insert data into 'Type_chambre'
INSERT INTO
    Type_chambre (nom_type, prix)
VALUES
    ('simple', 25000),
    ('suite', 25000),
    ('familiale', 85000)




    -- Insert data into 'chambre'
INSERT INTO
    chambre (num_chambre, etage, id_type, statut)
VALUES
    (101, 1, 1,'disponible'),
    (102, 1, 1,'occupée'),
    (201, 2, 2,'réservée'),
    (202, 2, 2,'disponible'),
    (301, 3, 3,'maintenance'),
    (302, 3, 3,'disponible')

    -- Insert data into 'reservation'
INSERT INTO
    reservation (id_client, id_chambre,date_reservation,date_arrivee_prevue,date_depart_prevue,nbre_personne,statut)
VALUES
    ('cli-2026-000001', 2,'2026-08-01','2026-08-10','2026-08-15',1,'confirmé'),
    ('cli-2026-000002', 3,'2026-08-05','2026-08-20','2026-08-25',2,'confirmé'),
    ('cli-2026-000003', 1,'2026-08-10','2026-08-18','2026-08-19',1,'annulée'),
    ('cli-2026-000004', 6,'2026-08-15','2026-09-01','2026-09-05',5,'confirmé'),
    ('cli-2026-000001', 4,'2026-08-20','2026-08-10','2026-09-12',2,'attente')

-- Insert data into 'sejour'
INSERT INTO 
    sejour (id_reservation,date_arrivee,date_depart )
VALUES 
       (1,'2026-08-10','2026-08-15'),
       (2,'2026-08-21',null),
       (4,'2026-09-01','2026-09-05')

-- Insert data into 'paiement'
INSERT INTO paiement (id_reservation, montant,date_paiement,moyen_paiement,'validé')
VALUES
    (1, 300000,'2026-08-01','carte','validé'),  
    (2, 150000,'2026-08-05','mobile money','validé'),
    (2, 150000,'2026-08-20','espèce','validé'),
    (4, 200000,'2026-08-15','mobile money','validé'),
    (4, 140000,'2026-09-01','carte','attente'),
    (5, 50000,'2026-08-20','mobile money','validé')
