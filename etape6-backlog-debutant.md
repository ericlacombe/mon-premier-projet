# ÉTAPE 6 — Backlog niveau 🥉 (DigiMarket, fil rouge « S'inscrire »)

⏱️ variable (c'est le codage)

**Règle** : chaque ligne du backlog est cochable et testable seule ; après chaque incrément le code reste fonctionnel.

## Backlog 🥉 (1 seul incrément)

- [ ] **1. Squelette** : `requirements.txt` (flask, sqlalchemy, pytest), `app/app.py` (Flask + engine SQLite + session + `create_all` + `init_sample_data()` + enregistrement du blueprint + `app.run`), `app/modelsSQLAlchemy.py` (`Base` + classe `Utilisateur`, table `users`)
      → *testable* : `python app/app.py` démarre sans erreur
- [ ] **2. Route** `POST /api/auth/register` dans `app/routes/auth.py` (blueprint `auth_bp`, réponses 400/409/201 en JSON)
      → *testable* : `curl -X POST http://127.0.0.1:5000/api/auth/register -H "Content-Type: application/json" -d '{...}'` renvoie `201`
- [ ] **3. Test** `test_register_email_deja_utilise` dans `app/tests/test_auth.py` (étape 5)
      → *testable* : `pytest` → 1 test OK (attend `409` au 2e appel avec le même email)

## Definition of Done du niveau 🥉

- [ ] code ✅ (les 3 lignes cochées)
- [ ] test ✅ (`pytest` passe)
- [ ] README ✅ (install/lancement/test déjà en place)
- [ ] commit Git ✅ (message clair)

---

🧵 **Fil rouge** : « S'inscrire » → `POST /api/auth/register` fonctionnel + testé.

*Backlog 🥉 validé. Prochaine action (avec validation séparée) : écrire le code des 5 fichiers.*
