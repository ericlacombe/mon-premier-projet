# ÉTAPE 3 appliquée à DigiMarket — Objets manipulés par les fonctions métier

⏱️ **~1 h — moyenne**

**Question** : quels **OBJETS** sont créés/manipulés par les fonctions métier F1–F4 (étape 2), avec quels liens et quels états ?
**Rappel** : un **objet** = une **chose** avec des **attributs** (données) et peut-être un **état** (qui change au fil du temps). La fonction métier agit sur l'objet.

## 📋 Attributs de chaque objet

| Objet | Attributs | A un état (cycle de vie) ? |
|---|---|---|
| **Utilisateur** | `id` (PK), `email` (UK), `mot_de_passe_hash`, `nom`, `prenom`, `adresse`, `role` (client \| admin) | ❌ non |
| **Categorie** | `id` (PK), `nom` (UK) — *c'est tout : une catégorie, c'est juste un nom unique* | ❌ non |
| **Produit** | `id` (PK), `nom`, `description`, `prix`, `stock`, `categorie_id` (FK) | ❌ non (le stock change, mais ce n'est pas un « état » au sens cycle de vie) |
| **Commande** | `id` (PK), `utilisateur_id` (FK), `adresse_livraison`, **`statut`** (en_attente \| validée \| expédiée \| annulée), `date_creation` | ✅ **oui** → `statut` (voir le state diagram ci-dessous) |
| **LigneCommande** | `id` (PK), `commande_id` (FK), `produit_id` (FK), `quantite`, `prix_unitaire` | ❌ non |

## Modèle de données (schéma ER)

```mermaid
erDiagram
    UTILISATEUR ||--o{ COMMANDE : "passe"
    CATEGORIE ||--o{ PRODUIT : "contient"
    PRODUIT ||--o{ LIGNE_COMMANDE : "est référencé par"
    COMMANDE ||--o{ LIGNE_COMMANDE : "comporte"

    UTILISATEUR {
        int id PK
        string email "unique"
        string mot_de_passe_hash
        string nom
        string prenom
        string adresse
        string role "client | admin"
    }
    CATEGORIE {
        int id PK
        string nom UK
    }
    PRODUIT {
        int id PK
        string nom
        text description
        float prix
        int stock "colonne du produit, PAS une table à part"
        int categorie_id FK
    }
    COMMANDE {
        int id PK
        int utilisateur_id FK
        string adresse_livraison
        string statut "en_attente | validee | expediee | annulee"
        datetime date_creation
    }
    LIGNE_COMMANDE {
        int id PK
        int commande_id FK
        int produit_id FK
        int quantite
        float prix_unitaire "prix figé au moment de la commande"
    }
```

### 🔑 PK / FK / UK — la 3ᵉ colonne de chaque attribut indique son rôle

| Sigle | Signification | Rôle | Exemple dans DigiMarket |
|---|---|---|---|
| **PK** | *Primary Key* = clé primaire | Identifiant **unique** de chaque ligne de la table | `UTILISATEUR.id` — chaque utilisateur a un `id` différent (1, 2, 3…) |
| **FK** | *Foreign Key* = clé étrangère | Colonne qui **pointe vers la PK d'une autre table** → c'est ça qui crée la relation 1—N | `COMMANDE.utilisateur_id FK` = « cette commande appartient à l'utilisateur dont l'`id` vaut cette valeur » |
| **UK** | *Unique* | Valeur unique dans la table, mais pas forcément la clé principale | `UTILISATEUR.email UK` (email unique, imposé par le CDC) |

💡 **Pourquoi séparer en 2 tables à chaque fois ?**
1. **CATEGORIE séparée de PRODUIT** — relation 1—N : une catégorie contient plusieurs produits (ex. « PC portables » → 15 produits). Si la catégorie était juste un texte dans `Produit`, on aurait « Informatique » répété 50 fois, avec des fautes (« info », « Info »…) qui créeraient des catégories fantômes. Avec une table `CATEGORIE` + `produit.categorie_id FK`, la catégorie existe **une seule fois**, et tous les produits pointent vers elle.
2. **LIGNE_COMMANDE séparée de COMMANDE** — relation 1—N : une commande contient plusieurs produits avec des quantités (panier). Impossible de mettre ça dans une seule ligne `COMMANDE` (il faudrait des colonnes `produit1, qte1, produit2, qte2…` en nombre inconnu). Donc : `COMMANDE` = l'en-tête (qui, adresse, statut, date) et chaque produit du panier = une ligne dans `LIGNE_COMMANDE` (`commande_id` FK, `produit_id` FK, `quantite`, `prix_unitaire`).

💡 **Pourquoi pas de table `stocks` à part ?** Le stock est un **attribut** du produit (colonne `stock`), comme le prix : « gérer les stocks » = modifier cette colonne ; « décrémenter à la validation » = `UPDATE produits SET stock = stock - qte`. Une table séparée créerait une redondance (risque de divergence). On n'en ferait une que pour un historique des mouvements de stock — non demandé par le CDC.

## Cycle de vie — l'objet `Commande` (le seul objet à états)

```mermaid
stateDiagram-v2
    [*] --> en_attente : F3 « Passer une commande » (POST /api/commandes)
    en_attente --> validee : F3 « Changer le statut » (PATCH /api/commandes/{id}, admin)
    validee --> expediee : F3 « Changer le statut » (PATCH, admin)
    expediee --> [*]
    en_attente --> annulee : F3 « Changer le statut » (PATCH, admin)
    validee --> annulee : F3 « Changer le statut » (PATCH, admin)
    annulee --> [*]
```

**Règle métier liée** : quand F3 fait passer la `Commande` à `validée`, elle **décrémente le stock** de chaque `Produit` concerné (`stock = stock - quantite`).

## Persisté ou temporaire, par objet

| Objet | Persisté ? | Pourquoi | Conséquence (étape 4.1) |
|---|---|---|---|
| `Utilisateur` | ✅ oui | comptes à conserver entre les connexions | table `utilisateurs` |
| `Categorie` | ✅ oui | catalogue | table `categories` |
| `Produit` | ✅ oui | catalogue + stock | table `produits` |
| `Commande` | ✅ oui | historique + suivi | table `commandes` |
| `LigneCommande` | ✅ oui | détail des commandes | table `lignes_commande` |
| token JWT décodé | ❌ temporaire | utile une seule requête | simple `dict`, **pas de table** |

---

✅ **Checklist étape 3** :
- [x] chaque objet vient d'une fonction métier de l'étape 2 (F1→Utilisateur, F2→Categorie/Produit, F3→Commande/Ligne) ;
- [x] pour chaque objet : persisté ou temporaire ? (tableau ci-dessus) ;
- [x] pour chaque transition : la fonction métier qui la déclenche est notée (F3 « Changer le statut »).

⚠️ **Piège évité** : créer des objets « au cas où » (ex. une table `stocks`) ; oublier l'état de `Commande`.

🧰 **Bonnes pratiques à ce stade** : commit Git de cette étape (ce push).

🧵 **Fil rouge** : l'objet **Utilisateur** est créé par F1 « Gérer les comptes » ; attributs : email (unique), mot de passe (haché), nom, prénom, adresse, rôle ; **persisté** ; pas de cycle de vie.

❓ **Auto-évaluation** :
1. Pourquoi `stock` est-il une colonne de `Produit` et pas une table ?
2. Quels objets sont persistés ? Lequel est temporaire ?
3. Quelle fonction métier fait changer l'état d'une commande ?

📝 **À retenir (3 lignes)** :
1) Objet = chose avec attributs et peut-être un état (ici `Commande.statut`).
2) Persisté → table en base (4.1) ; temporaire (token) → `dict`, pas de table.
3) La fonction métier agit sur l'objet (F3 change l'état de la commande et décrémente le stock).

---
*Étape 3 ✅ terminée. En attente de votre accord pour entrer dans la BOUCLE (étape 4, niveau 🥉 débutant).*
