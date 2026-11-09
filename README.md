# Mon premier projet — DigiMarket (API REST Flask)

📖 **Méthode suivie** : ce projet suit la méthode décrite dans **[methodologie.md](methodologie.md)** (étapes 0–6 + niveaux 🥉🥈🥇). Les fichiers `etape0-AFB.md` … `etape6-backlog-debutant.md` sont **le résultat de chaque étape** de cette méthode (conception puis code).

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

## Structure du projet (étape 4 → code étape 6, niveau 🥉)
```
mon-premier-projet/
├── requirements.txt            # flask, sqlalchemy, pytest
├── digimarket.db               # base SQLite (créée au lancement)
├── README.md, attentes.md, methodologie.md, methodologie-canva.mmd
├── etape0-AFB.md … etape6-backlog-debutant.md   # étapes de la méthode
└── app/
    ├── app.py                  # point d'entrée Flask (app, blueprint, app.run)
    ├── db.py                   # engine SQLite + session partagée (SQLAlchemy pur)
    ├── modelsSQLAlchemy.py     # Base + classe User (table users)
    ├── routes/
    │   └── auth.py             # blueprint auth_bp : POST /api/auth/register
    └── tests/
        └── test_auth.py        # test_register_email_deja_utilise (409)
```

## Installation et lancement (étape 6)
```bash
python -m venv venv                # crée un environnement virtuel isolé (dossier venv/) : les bibliothèques du projet n'installent PAS dans ton Python global
source venv/bin/activate           # active cet environnement (Windows : venv\Scripts\activate) — toutes les commandes suivantes (pip, python) l'utilisent
pip install -r requirements.txt    # installe toutes les bibliothèques listées dans requirements.txt (flask, sqlalchemy, pytest) — la "liste de courses" du projet : mêmes versions pour tout le monde
cd app && python app.py            # lance l'API sur http://127.0.0.1:5000
```

## Comment tester (étape 5)
```bash
pytest            # lance tous les tests (ici : test_register_email_deja_utilise → 409)
```

## Fichiers du projet (étapes 0–6, niveau 🥉)
| Fichier | Description |
|---|---|
| `attentes.md` | Cahier des charges de l'exercice (DigiMarket) |
| `methodologie.md` | Méthode de travail en 6 étapes + 3 niveaux (🥉🥈🥇) — voir le lien en haut de ce README |
| `methodologie-canva.mmd` | Schéma visuel (Mermaid) de la méthode |
| `etape0-AFB.md` | Étape 0 : liste des besoins 🔵 et contraintes 🟠 |
| `etape1-use-cases.md` | Étape 1 : acteurs, cas d'utilisation, matrice des rôles |
| `etape2-fonctions-metier.md` | Étape 2 : fonctions métier F1–F4 + flux « Passer une commande » |
| `etape3-objets.md` | Étape 3 : schéma ER (5 objets, PK/FK/UK), cycle de vie de Commande |
| `etape4-conception-debutant.md` | Étape 4 niveau 🥉 : base, classe, route, module, erreurs (fil rouge) |
| `etape5-tests-debutant.md` | Étape 5 niveau 🥉 : 1 test unitaire (409 email déjà pris) |
| `etape6-backlog-debutant.md` | Étape 6 niveau 🥉 : backlog cochée, code fonctionnel (register + test) |
| `requirements.txt` | Dépendances (flask, sqlalchemy, pytest) |
| `app/app.py` | Point d'entrée Flask |
| `app/db.py` | Moteur SQLite + session partagée |
| `app/modelsSQLAlchemy.py` | Modèle User (table users) |
| `app/routes/auth.py` | Route POST /api/auth/register |
| `app/tests/test_auth.py` | Test 409 email déjà pris |
| `README.md` | Ce fichier |
