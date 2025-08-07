# Library Management System

Une application web complète de gestion de bibliothèque développée avec Flask et SQLite, permettant la gestion des livres, bibliothèques et prix internationaux avec fonctionnalités CRUD complètes.

## 📋 Description

Cette application web permet de gérer efficacement une bibliothèque avec trois modules principaux : gestion des livres, gestion des bibliothèques, et suivi des prix internationaux. L'interface intuitive offre toutes les opérations CRUD (Create, Read, Update, Delete) avec une fonctionnalité de recherche avancée.

## ✨ Fonctionnalités principales

### 📚 Gestion des Livres


### 🏛️ Gestion des Bibliothèques


### 💰 Suivi des Prix Internationaux


## 🛠️ Technologies utilisées

- **Backend** : Flask (Python)
- **Base de données** : SQLite3
- **Frontend** : HTML/CSS avec templates Jinja2
- **Architecture** : MVC (Model-View-Controller)


### Navigation

- **Accueil** : `/` - Page d'accueil
- **Livres** : `/books` - Liste des livres
- **Bibliothèques** : `/library` - Gestion des bibliothèques
- **Prix** : `/prices` - Suivi des prix internationaux
- **Recherche** : `/search?query=terme` - Recherche de livres

## 📁 Structure du projet

```
ML_Project/
│
├── app.py                    # Application Flask principale
├── books.db                  # Base de données SQLite
├── templates/                # Templates HTML
│   ├── home.html            # Page d'accueil
│   ├── books.html           # Liste des livres
│   ├── add_book.html        # Formulaire d'ajout de livre
│   ├── edit_book.html       # Formulaire d'édition de livre
│   ├── libraries.html       # Liste des bibliothèques
│   ├── add_library.html     # Formulaire d'ajout de bibliothèque
│   ├── edit_library.html    # Formulaire d'édition de bibliothèque
│   ├── prices.html          # Liste des prix
│   ├── add_price.html       # Formulaire d'ajout de prix
│   ├── edit_price.html      # Formulaire d'édition de prix
│   └── search_results.html  # Résultats de recherche
├── static/                   # Fichiers statiques (CSS, JS)
│   ├── css/
│   ├── js/
│   └── images/
└── README.md                # Ce fichier
```

## 🎯 Fonctionnalités détaillées

### Gestion des Livres

## 🎨 Interface utilisateur

### Pages principales

1. **Accueil** : Vue d'ensemble avec navigation
2. **Liste des livres** : Tableau avec actions (modifier/supprimer)
3. **Formulaires** : Interface intuitive pour l'ajout/modification
4. **Recherche** : Barre de recherche avec résultats instantanés

### Actions disponibles

- ✅ **Créer** : Nouveaux livres, bibliothèques, prix
- 👁️ **Lire** : Affichage des listes et détails
- ✏️ **Modifier** : Édition des informations existantes
- 🗑️ **Supprimer** : Suppression avec confirmation

## 🔧 Personnalisation


### Recherche de livres
1. Utiliser la barre de recherche
2. Taper "Prince" ou "Saint-Exupéry"
3. Voir les résultats correspondants

## 🚀 Déploiement

### Déploiement local


## 🔒 Sécurité

### Mesures implémentées
- **Requêtes préparées** : Protection contre l'injection SQL
- **Validation des données** : Contrôle des entrées utilisateur
- **Gestion des erreurs** : Messages d'erreur appropriés

### Améliorations possibles
- Authentification utilisateur
- Hachage des mots de passe
- Sessions sécurisées
- CSRF protection

## 🤝 Contribution


### Guidelines de contribution

## 🐛 Dépannage

### Erreurs courantes

**Base de données non trouvée** 

## 📄 Licence
