"""
routes/auth.py — Blueprint de la fonction métier F1 « Gérer les comptes ».

Niveau 🥉 : une seule route, le fil rouge « S'inscrire ».

Route disponible :
  POST /api/auth/register  →  inscrit un nouvel utilisateur

Pourquoi un blueprint séparé et pas la route dans app.py ?
- le CDC demande une organisation en modules fonctionnels (Blueprints) :
  chaque domaine a son fichier (ici auth, plus tard produits.py, commandes.py) ;
- app.py reste l'ASSEMBLAGE : il crée l'app et enregistre les blueprints
  (register_blueprint) — il ne grossit pas à chaque nouvelle route ;
- le préfixe /api/auth est groupé ici (url_prefix du blueprint).
"""

# ------------------------------------------------------------------
# Importations
# ------------------------------------------------------------------
# Pourquoi Blueprint et PAS Flask ici ? Flask sert à créer l'application
# (une seule fois, dans app.py : app = Flask(__name__)). Un Blueprint regroupe
# les routes d'un domaine (ici "auth") ; app.py l'enregistre ensuite avec
# app.register_blueprint(auth_bp).
# - request : lire la requête entrante (ex. request.get_json() = le JSON envoyé)
# - jsonify : renvoyer une réponse JSON (ex. jsonify({...}), 400)
from flask import Blueprint, request, jsonify
# generate_password_hash : hache le mot de passe (jamais stocké en clair) — inclus avec Flask
from werkzeug.security import generate_password_hash

# session partagée (module db.py — évite l'import circulaire avec app.py)
from app.db import session
# modèle User (défini dans modelsSQLAlchemy.py, table users)
from app.modelsSQLAlchemy import User

# Le blueprint regroupe les routes du domaine "auth", préfixées /api/auth
auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")


# ------------------------------------------------------------------
# Création d'une route pour enregister un nouvel utilisateur.
#
# Pourquoi une route ? Pour relier une requête URL (POST /api/auth/register)
# à cet endpoint (la fonction register) où le code est exécuté.
# ------------------------------------------------------------------

@auth_bp.route("/register", methods=["POST"])   # la route = URL + méthode HTTP
def register():                                  # l'endpoint = cette fonction
    """Inscrit un nouvel utilisateur.

    Entrée (JSON) : {email, password, first_name, last_name, address?}
    Sorties : 201 créé · 400 champs manquants · 409 email déjà utilisé · 500 erreur

    Rappels des imports flask :
    - request : lire la requête entrante (ex. request.get_json() = le JSON envoyé par le client)
    - jsonify : renvoyer une réponse JSON (ex. jsonify({...}), 400)
    """
    try:
        body = request.get_json() or {}          # corps JSON de la requête ({} si vide)

        # 400 : champs obligatoires manquants
        if not body.get("email") or not body.get("password"):
            return jsonify({"error": "email et password requis"}), 400

        # 409 : email déjà pris (contrainte unique sur users.email)
        if session.query(User).filter_by(email=body["email"]).first():
            return jsonify({"error": "email déjà utilisé"}), 409

        # Création de l'utilisateur : mot de passe haché, jamais en clair
        user = User(
            email=body["email"],
            password_hash=generate_password_hash(body["password"]),
            first_name=body.get("first_name", ""),
            last_name=body.get("last_name", ""),
            address=body.get("address", ""),
            role="client",                        # tout nouvel inscrit est client
        )
        # session.add(user) : marque l'objet pour insertion — RIEN n'est encore écrit
        # en base : l'objet est juste "suivi" par la session (état "pending")
        session.add(user)
        # session.commit() : valide DÉFINITIVEMENT en base → exécute le vrai
        # INSERT INTO users (...) ; après ça, c'est écrit pour de bon
        # (d'où le session.rollback() dans le except si une erreur survient)
        session.commit()

        # 201 : ressource créée
        return jsonify({"message": "utilisateur créé", "email": user.email}), 201

    except Exception as e:
        session.rollback()                        # annule en cas d'erreur
        return jsonify({"error": str(e)}), 500
