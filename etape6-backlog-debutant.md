# ÉTAPE 6 — Backlog niveau 🥉 (DigiMarket, fil rouge « S'inscrire »)

⏱️ variable (c'est le codage)

**Règle** : chaque ligne du backlog est cochable et testable seule ; après chaque incrément le code reste fonctionnel. **Chaque ligne est commentée** (pourquoi elle est là — traçabilité avec les étapes 4/5).

## Backlog 🥉 (1 seul incrément)

- [ ] **1. Squelette** : `requirements.txt` (flask, sqlalchemy, pytest), `app/app.py` (Flask + engine SQLite + session + `create_all` + `init_sample_data()` + enregistrement du blueprint + `app.run`), `app/modelsSQLAlchemy.py` (`Base` + classe `User`, table `users`)
      → **pourquoi :** vient de l'étape 4 — 4.1 (base), 4.5 (classe), 4.8 (module/app) ; l'arborescence du README.
      → **testable :** `python app/app.py` démarre sans erreur
- [ ] **2. Route** `POST /api/auth/register` dans `app/routes/auth.py` (blueprint `auth_bp`, réponses 400/409/201 en JSON)
      → **pourquoi :** cas « S'inscrire » (étape 1, acteur Visiteur) → route 4.7 + erreurs 4.10 (409 email déjà pris prévu à l'étape 4).
      → **testable :** `curl -X POST http://127.0.0.1:5000/api/auth/register -H "Content-Type: application/json" -d '{...}'` renvoie `201`
- [ ] **3. Test** `test_register_email_deja_utilise` dans `app/tests/test_auth.py`
      → **pourquoi :** conçu à l'étape 5 (niveau 🥉 = 1 test unitaire) ; vérifie le cas d'erreur 409 de la route (étape 4).
      → **testable :** `pytest` → 1 test OK (attend `409` au 2e appel avec le même email)

## Definition of Done du niveau 🥉

- [ ] code ✅ (les 3 lignes cochées)
- [ ] test ✅ (`pytest` passe)
- [ ] README ✅ (install/lancement/test déjà en place)
- [ ] commit Git ✅ (message clair)

---

🧵 **Fil rouge** : « S'inscrire » → `POST /api/auth/register` fonctionnel + testé.

*Backlog 🥉 validé et commenté. Prochaine action (avec validation séparée) : écrire le code des 5 fichiers.*
