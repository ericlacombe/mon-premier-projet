# ÉTAPE 0 appliquée à DigiMarket — AFB : Analyse fonctionnelle du besoin

⏱️ **~30 min — facile**

**Question** : quels sont les besoins bruts exprimés dans `attentes.md` ?
**Outil** : une simple **liste de phrases en français** — pas de diagramme à ce stade.
**Méthode** : relire `attentes.md` ligne par ligne, noter chaque besoin tel quel, en séparant 🔵 besoins et 🟠 contraintes imposées.

👉 **Sortie** : la liste ci-dessous.

---

## 🔵 Besoins (ce que veut DigiMarket / l'utilisateur)

1. DigiMarket (vente de matériel informatique) veut une **boutique en ligne (e-commerce)**.
2. Livrable : une **API REST** gérant **produits, catégories, commandes et utilisateurs**, avec **authentification**.
3. Deux types de profils : **client** et **administrateur**.
4. Le **client** peut : créer un compte, se connecter, parcourir le catalogue, passer des commandes, suivre l'état de ses commandes.
5. L'**administrateur** peut : gérer le catalogue produits, suivre et modifier les commandes.
6. L'inscription nécessite un **email unique**, un **mot de passe sécurisé** et les informations personnelles de base.
7. À la connexion, l'utilisateur reçoit un **token JWT** lui donnant accès aux fonctionnalités selon son rôle.
8. Visiteurs et clients peuvent : voir le **catalogue complet**, le **détail d'un produit** (description, prix, disponibilité), **rechercher** par nom ou caractéristiques.
9. L'admin peut : **ajouter, modifier, supprimer** des produits et **gérer les stocks**.
10. Fiche produit : nom, description complète, catégorie, prix, disponibilité en stock.
11. Le client peut : créer une commande, ajouter des produits avec quantités, donner une **adresse de livraison**, consulter son **historique**, suivre l'**état** d'une commande.
12. L'admin peut : voir **toutes** les commandes, **modifier leur statut** (en attente, validée, expédiée, annulée), voir le détail de chaque commande.
13. **Règle métier** : le système vérifie que les produits commandés sont **en stock** et **décrémente automatiquement le stock à la validation** d'une commande.
14. Architecture **modulaire** : séparation modèles / contrôleurs / vues (JSON), organisée en **Blueprints** par module fonctionnel.
15. Bonnes pratiques **REST**.
16. Sécurité : **JWT**, **hachage des mots de passe**, vérification des autorisations par rôle, protection contre les injections SQL.
17. Qualité : code **commenté**, gestion des erreurs, **tests unitaires et fonctionnels**, documentation complète de l'API.
18. Livrables : code source, structure claire, `requirements.txt`, application fonctionnelle, **README.md** (installation, fonctionnalités, doc API), base initialisée avec **données de test**, tests.
19. La remise peut se faire via un **dépôt Git public** contenant tous les livrables.

## 🟠 Contraintes imposées (technologie, délai, fichiers fournis)

- Langage : **Python**.
- Framework backend : **Flask**.
- Base de données : **SQLite** avec **SQLAlchemy** comme ORM.
- Authentification : **JWT**, utilisateurs stockés dans une **table SQL**.
- La structure des tables sera fournie dans **`structuredonnées.md`**.
- La base de données sera fournie dans **`digimarket.db`**.
- **Deadline de remise : 19 novembre.**

---

✅ **Checklist étape 0** :
- [x] chaque besoin tient en une seule phrase ;
- [x] besoins 🔵 et contraintes 🟠 séparés (ex. « en Flask » = contrainte 🟠, pas un besoin 🔵).

⚠️ **Piège évité** : on n'a pas commencé à coder — on a d'abord cette liste.

🧰 **Bonnes pratiques à ce stade** (le strict nécessaire — le reste est pour plus tard) :
- ✅ déjà fait : dépôt Git `mon-premier-projet` créé, avec `.gitignore` et `README.md` (conventions de nommage) ;
- **à faire maintenant** : déposer `attentes.md`, `methodologie.md`, `etape0-AFB.md` dans le dépôt → **1er commit**.

🧵 **Fil rouge** (suivi à toutes les étapes) : le besoin **« l'utilisateur s'inscrit avec un email unique »** (besoin n°6).

❓ **Auto-évaluation** :
1. Citez un besoin 🔵 et une contrainte 🟠 de DigiMarket.
2. Pourquoi séparer besoins et contraintes ?

📝 **À retenir (3 lignes)** :
1) Un besoin = une phrase, ce que veut l'utilisateur.
2) Une contrainte = imposé (techno, délai, fichiers fournis).
3) On ne code jamais avant d'avoir cette liste.
