"""
db.py — Moteur SQLite + session partagée (SQLAlchemy pur).

Petit module séparé pour que app.py ET les routes puissent utiliser
la même session sans import circulaire.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.modelsSQLAlchemy import Base

# 'sqlite:///digimarket.db' : fichier SQLite local (créé automatiquement)
engine = create_engine("sqlite:///digimarket.db", echo=False)

# Crée les tables déclarées (users) si elles n'existent pas encore
Base.metadata.create_all(engine)

# Session = "conversation" avec la base (add / commit / query / rollback)
Session = sessionmaker(bind=engine)
session = Session()
