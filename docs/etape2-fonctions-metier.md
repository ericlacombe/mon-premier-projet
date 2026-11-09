# ÉTAPE 2 appliquée à DigiMarket — Fonctions MÉTIER du système

⏱️ **~1 h — moyenne**

**Question** : quelles **ACTIONS globales internes** (fonctions métier) réalisent les cas de l'étape 1 ?
**Rappel** : une fonction métier = une action (verbe + complément), PAS une fonction Python. Test du « une phrase » : chaque fonction métier tient en une seule phrase.

## Les 4 fonctions métier de DigiMarket

| Bloc | Fonction métier (action) | Cas réalisés (étape 1) |
|---|---|---|
| **F1** | Gérer les comptes | S'inscrire, Se connecter |
| **F2** | Gérer le catalogue | Consulter, Rechercher, Détail produit, Ajouter/Modifier/Supprimer un produit, Gérer les stocks |
| **F3** | Gérer les commandes | Passer une commande, Historique, Suivi d'état, Voir toutes les commandes, Changer le statut |
| **F4** | Sécuriser les accès | (transversal : vérifie le token JWT et le rôle sur chaque requête protégée) |

## Diagramme fonctionnel (blocs d'actions + flux de données)

```mermaid
flowchart TB
    subgraph EXT["Acteurs externes"]
        VIS["Visiteur"]
        CLI["Client"]
        ADM["Administrateur"]
    end

    subgraph SYS["Système DigiMarket (API REST) — fonctions MÉTIER"]
        F1["F1 — Gérer les comptes<br/>s'inscrire · se connecter · émettre le token JWT"]
        F2["F2 — Gérer le catalogue<br/>lister · chercher · CRUD produits · gérer le stock"]
        F3["F3 — Gérer les commandes<br/>passer une commande · historique · suivi · statut · lignes"]
        F4["F4 — Sécuriser les accès<br/>hacher les mots de passe · vérifier le JWT · contrôler les rôles"]
    end

    subgraph DATA["Données persistées (SQLite)"]
        D1[("utilisateurs")]
        D2[("produits / catégories")]
        D3[("commandes / lignes")]
    end

    VIS -->|demande de compte / connexion| F1
    CLI -->|token JWT| F2
    CLI -->|token JWT| F3
    ADM -->|token JWT| F2
    ADM -->|token JWT| F3

    F1 -->|vérifie identifiants, signe le token| F4
    F2 -->|vérifie le rôle| F4
    F3 -->|vérifie le rôle| F4

    F1 <-->|lire / créer un compte| D1
    F2 <-->|lire / modifier le catalogue| D2
    F3 <-->|lire / créer commandes et lignes| D3
    F3 -->|vérifie et décrémente le stock| D2

    F1 -->|réponse JSON : token| VIS
    F2 -->|réponse JSON : produits| CLI
    F2 -->|réponse JSON : produits| VIS
    F3 -->|réponse JSON : commandes| CLI
    F3 -->|réponse JSON : commandes| ADM
```

## Diagramme de flux — la fonction métier complexe « Passer une commande » (F3)

```mermaid
flowchart TD
    START([Client appelle POST /api/commandes<br/>avec son token JWT]) --> AUTH{Token valide ?}
    AUTH -- non --> E401([401 : non authentifié])
    AUTH -- oui --> ROLE{"Rôle = client ou admin ?<br/>(garde-fou : tout rôle inconnu → 403)"}
    ROLE -- non --> E403([403 : accès interdit])
    ROLE -- oui --> DATA{Lecture du JSON :<br/>adresse + lignes produit_id/quantité valides ?}
    DATA -- non --> E400a([400 : requête invalide])
    DATA -- oui --> STOCK{Pour chaque ligne :<br/>stock du produit suffisant ?}
    STOCK -- non --> E400b([400 : stock insuffisant])
    STOCK -- oui --> CREATE[Créer l'objet Commande<br/>état = en_attente<br/>+ ses lignes en base]
    CREATE --> RESP([201 : commande créée,<br/>retour JSON de la commande])
```

💡 Le `403` est un **garde-fou** : avec seulement 2 rôles (client, admin) et un token obligatoire, la branche « non » est normalement inatteignable — mais elle protège si un jour un rôle inconnu/invalide apparaît (bonne pratique : jamais de confiance aveugle côté serveur).

---

✅ **Checklist étape 2** :
- [x] chaque fonction métier réalise au moins un cas de l'étape 1 (traçabilité) ;
- [x] chaque fonction métier tient en une seule phrase.

⚠️ **Piège évité** : confondre fonction métier (F1 « Gérer les comptes ») et fonction Python.

🧰 **Bonnes pratiques à ce stade** :
- traçabilité poursuivie (cas → fonction métier, voir tableau ci-dessus) ;
- commit Git de cette étape (ce push).

🧵 **Fil rouge** : le cas « S'inscrire » est réalisé par **F1 « Gérer les comptes »** ; son flux : données valides ? email unique ? → créer le compte / sinon erreur `409`.

❓ **Auto-évaluation** :
1. Quelle fonction métier réalise « S'inscrire » ?
2. Fonction métier ou fonction Python : quelle différence ?
3. Pourquoi ne détailler qu'UN seul flux (celui de « Passer une commande ») ?

📝 **À retenir (3 lignes)** :
1) Fonction métier = action globale (F1–F4), tient en une phrase.
2) Le diagramme fonctionnel montre les blocs + les flux vers la base.
3) On détaille UN seul flux complexe (ici « Passer une commande »).

---
*Étape 2 ✅ terminée. En attente de votre accord pour l'étape 3 (objets).*
