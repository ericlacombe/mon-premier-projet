"""
__init__.py — Package app : l'API DigiMarket (Flask + SQLAlchemy pur).

À quoi sert ce fichier ? Il indique à Python que le dossier app/ est un
PACKAGE, c'est-à-dire un dossier de modules importables. Grâce à lui,
depuis la racine du projet, on peut écrire :
    from app.db import session
    from app.modelsSQLAlchemy import User
    from app.routes.auth import auth_bp
Sans ce fichier, ces imports échoueraient au lancement depuis la racine
(python -m app.app) et dans les tests (pytest).
Un __init__.py peut être vide ; ici il ne contient que ce docstring explicatif.
"""
