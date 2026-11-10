"""
modelsSQLAlchemy.py — Modèles SQLAlchemy (ORM) pour DigiMarket.

Niveau 🥉 : uniquement la table users (fil rouge « S'inscrire »).
Ce fichier définit (sous forme de classes) les modèles des tables de la base SQL, importés par :
- app/app.py        (l'API Flask, qui contient les endpoints)
- app/script_crud.py  (script CRUD standalone : opérations en console, à créer si besoin)
Aucun code d'exécution : importer ce fichier ne déclenche aucune opération en base de données.
Même style que l'ancien projet (SQLAlchemy pur, pas Flask-SQLAlchemy).
"""

# ------------------------------------------------------------------
# Imports SQLAlchemy
# ------------------------------------------------------------------
# Column               : définit une colonne dans une table
# Integer, String, Text : types de données des colonnes
from sqlalchemy import Column, Integer, String, Text

# declarative_base : fonction qui génère la classe de base des modèles
# (elle garde la "métadonnée" = la description de toutes les tables)
from sqlalchemy.orm import declarative_base

# ------------------------------------------------------------------
# Déclaration de la base des modèles
# ------------------------------------------------------------------
# declarative_base() crée une classe de base. Tous les modèles héritent de Base.
# En héritant de Base, chaque classe (= une table de la base) obtient :
# - le mapping ORM (SQLAlchemy sait que la classe = une table de la base)
# - la métadonnée (enregistrée dans Base.metadata)
# - les attributs magiques (ex: User.__table__, User.__mapper__)
# - la compatibilité session (les instances peuvent être ajoutées à une session)
Base = declarative_base()

# ------------------------------------------------------------------
# Définition du modèle
# ------------------------------------------------------------------

class User(Base):
    # Nom de la table dans la base de données (pluriel, comme l'ancien projet)
    __tablename__ = "users"

    # Identifiant unique du compte (clé primaire, auto-incrémenté)
    id = Column(Integer, primary_key=True)
    # Email — unique (UK) et obligatoire : un seul compte par email (CDC)
    email = Column(String(255), unique=True, nullable=False)
    # Mot de passe haché — JAMAIS en clair (on stocke seulement le hash)
    password_hash = Column(String(255), nullable=False)
    # Prénom / nom — obligatoires, limités à 100 caractères
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    # Adresse — optionnelle (type Text = pas de limite de taille)
    address = Column(Text)
    # Rôle : 'client' par défaut, 'admin' pour les administrateurs
    role = Column(String(20), nullable=False, default="client")

    # Représentation textuelle de l'objet (affichée avec print())
    def __repr__(self):
        return f"<User {self.email}>"

# ------------------------------------------------------------------
# Schéma de la table (niveau 🥉 : une seule table) :
# ------------------------------------------------------------------
#
#   users
#   ├── id            PK int, auto-incrémenté
#   ├── email         UK string, obligatoire
#   ├── password_hash string, obligatoire
#   ├── first_name    string, obligatoire
#   ├── last_name     string, obligatoire
#   ├── address       text, optionnel
#   └── role          string, défaut 'client'
#
# ------------------------------------------------------------------
