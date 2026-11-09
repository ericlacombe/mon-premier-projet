"""
app.py — Point d'entrée de l'API DigiMarket (niveau 🥉).

Flask + SQLAlchemy pur : on crée l'app, on enregistre le blueprint auth,
puis on lance le serveur.

Lancer depuis le dossier app/ :  python app.py
"""

from flask import Flask

from db import session                      # session partagée (db.py)
from modelsSQLAlchemy import User           # modèle

app = Flask(__name__)

# ------------------------------------------------------------------
# Blueprints (routes) — ici seulement auth pour le niveau 🥉
# ------------------------------------------------------------------
from routes.auth import auth_bp            # blueprint F1 « Gérer les comptes »
app.register_blueprint(auth_bp)            # les routes seront sous /api/auth/...

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
