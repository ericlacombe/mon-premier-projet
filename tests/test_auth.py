"""
tests/test_auth.py — Tests du niveau 🥉 (fil rouge « S'inscrire »).

Lancer depuis la racine du projet :  pytest
"""

# ------------------------------------------------------------------
# Importations
# ------------------------------------------------------------------
# pytest : le lanceur de tests (fixture @pytest.fixture, exécution avec `pytest`)
import pytest
# create_engine : crée un moteur SQLite EN MÉMOIRE (sqlite:///:memory:)
from sqlalchemy import create_engine
# sessionmaker : fabrique de sessions (ici pour la base de test en mémoire)
from sqlalchemy.orm import sessionmaker

# app : l'application Flask créée dans app/app.py (le point d'entrée)
from app.app import app
# Base (pour create_all/drop_all) et User (le modèle) définis dans modelsSQLAlchemy.py
from app.modelsSQLAlchemy import Base, User
# le module des routes auth : on va remplacer SA session par celle de test
import app.routes.auth as auth_module


@pytest.fixture
def client():
    """Client de test Flask + base SQLite en mémoire (jetable à chaque test)."""
    engine = create_engine("sqlite:///:memory:")   # base en RAM, rien sur le disque
    Base.metadata.create_all(engine)                # crée la table users
    TestSession = sessionmaker(bind=engine)
    auth_module.session = TestSession()             # la route utilisera CETTE session

    app.config["TESTING"] = True                    # mode test : pas de vrai serveur
    yield app.test_client()                         # le client qui appelle les routes

    Base.metadata.drop_all(engine)                  # nettoyage après le test


def test_register_email_deja_utilise(client):
    """Scénario : inscrire 2 fois le même email → la 2e fois échoue en 409."""
    payload = {
        "email": "a@b.c",
        "password": "secret",
        "first_name": "Alice",
        "last_name": "Martin",
    }

    # 1er appel : inscription OK → 201
    r1 = client.post("/api/auth/register", json=payload)
    assert r1.status_code == 201                    # assert = vérifie le résultat attendu

    # 2e appel, MÊME email → doit échouer → 409 (conflit, email unique)
    r2 = client.post("/api/auth/register", json=payload)
    assert r2.status_code == 409
    assert r2.get_json()["error"] == "email déjà utilisé"
