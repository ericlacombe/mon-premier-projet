"""
app.py — Point d'entrée de l'API DigiMarket (niveau 🥉).

Flask + SQLAlchemy pur : on crée l'app, on enregistre le blueprint auth,
puis on lance le serveur.

Lancer depuis la racine du projet :  python -m app.app
"""

# ------------------------------------------------------------------
# Importations
# ------------------------------------------------------------------
# Flask : sert à créer l'application, UNE SEULE FOIS, ici : app = Flask(__name__)
from flask import Flask

# session partagée (module db.py — tout le monde passe par db.py pour éviter
# l'import circulaire : app.py importe routes/auth.py, donc auth.py ne peut pas
# importer app.py)
from app.db import session
# modèle User (table users, défini dans modelsSQLAlchemy.py)
from app.modelsSQLAlchemy import User

# ------------------------------------------------------------------
# Création de l'application Flask
# ------------------------------------------------------------------
app = Flask(__name__)

# ------------------------------------------------------------------
# Blueprints (routes) — ici seulement auth pour le niveau 🥉
# ------------------------------------------------------------------
# auth_bp : le blueprint défini dans routes/auth.py (fonction métier F1 « Gérer les comptes »)
from app.routes.auth import auth_bp
# register_blueprint : enregistre les routes du blueprint dans l'app
# → elles seront accessibles sous /api/auth/... (ex. POST /api/auth/register)
app.register_blueprint(auth_bp)

# ------------------------------------------------------------------
# Données de test : un compte admin si la base est vide
# ------------------------------------------------------------------
def init_sample_data():
    """Ajoute un admin de test si la table users est vide."""
    if session.query(User).count() == 0:
        admin = User(
            email="admin@digimarket.fr",
            password_hash="hash_de_test",   # en vrai : generate_password_hash(...)
            first_name="Admin",
            last_name="Digi",
            role="admin",
        )
        session.add(admin)
        session.commit()
        print("Données de test initialisées.")

# ------------------------------------------------------------------
# Point d'entrée : lance le serveur Flask
# ------------------------------------------------------------------
if __name__ == "__main__":
    init_sample_data()     # données de test seulement au lancement direct
    app.run(debug=True)
