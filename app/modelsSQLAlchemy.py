"""
modelsSQLAlchemy.py — Modèles SQLAlchemy (ORM) pour DigiMarket.

Niveau 🥉 : uniquement la table users (fil rouge « S'inscrire »).
Aucun code d'exécution : importer ce fichier ne touche pas à la base de données.
Même style que l'ancien projet (SQLAlchemy pur, pas Flask-SQLAlchemy).
"""

from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base

# Base = classe de base de tous les modèles (elle garde la métadonnée des tables)
Base = declarative_base()


class User(Base):
    # Nom de la table dans la base de données (pluriel, comme l'ancien projet)
    __tablename__ = "users"

    # Identifiant unique du compte (clé primaire, auto-incrémenté)
    id = Column(Integer, primary_key=True)
    # Email — unique (UK) et obligatoire : un seul compte par email (CDC)
    email = Column(String(255), unique=True, nullable=False)
    # Mot de passe haché — JAMAIS en clair
    password_hash = Column(String(255), nullable=False)
    # Prénom / nom — obligatoires
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    # Adresse — optionnelle
    address = Column(Text)
    # Rôle : 'client' par défaut, 'admin' pour les administrateurs
    role = Column(String(20), nullable=False, default="client")

    # Représentation textuelle de l'objet (affichée avec print())
    def __repr__(self):
        return f"<User {self.email}>"

# ------------------------------------------------------------------
# Schéma de la table (niveau 🥉 : une seule table) :
# ------------------------------------------------------------------
#   users
#   ├── id            (PK, int, auto-incrémenté)
#   ├── email         (UK, string, obligatoire)
#   ├── password_hash (string, obligatoire)
#   ├── first_name    (string, obligatoire)
#   ├── last_name     (string, obligatoire)
#   ├── address       (text, optionnel)
#   └── role          (string, défaut 'client')
# ------------------------------------------------------------------
