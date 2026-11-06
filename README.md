# Mon premier projet — DigiMarket (API REST Flask)

## Conventions (étape 0)
- snake_case pour les variables et fonctions
- PascalCase pour les classes
- routes au pluriel : /api/produits, /api/commandes

## Fonctionnalités — cas d'utilisation (étape 1)
- **Visiteur** : s'inscrire, se connecter, consulter le catalogue, rechercher un produit, voir le détail d'un produit
- **Client** : en plus, passer une commande, consulter son historique de commandes, suivre l'état d'une commande
- **Administrateur** : gérer les produits et les stocks, voir toutes les commandes, changer le statut d'une commande

## Fonctions métier (étape 2)
- **F1 — Gérer les comptes** : inscription, connexion, émission du token JWT
- **F2 — Gérer le catalogue** : liste, recherche, détail, CRUD produits, gestion des stocks
- **F3 — Gérer les commandes** : passer une commande, historique, suivi, changement de statut, lignes
- **F4 — Sécuriser les accès** : hachage des mots de passe, vérification JWT, contrôle des rôles

## Modèle de données — objets (étape 3)
- **Utilisateur** : id, email (unique), mot_de_passe_hash, nom, prenom, adresse, role
- **Categorie** : id, nom (unique)
- **Produit** : id, nom, description, prix, stock, categorie_id (FK)
- **Commande** : id, utilisateur_id (FK), adresse_livraison, statut (en_attente | validée | expédiée | annulée), date_creation
- **LigneCommande** : id, commande_id (FK), produit_id (FK), quantite, prix_unitaire

Liens : Utilisateur 1—N Commande · Categorie 1—N Produit · Produit 1—N LigneCommande · Commande 1—N LigneCommande
(détail complet dans `etape3-objets.md`, schéma ER + PK/FK/UK)
