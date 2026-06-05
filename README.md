# Centre de Suivi des Événements

Application web de suivi et d'analyse des événements utilisateur développée avec FastAPI, PostgreSQL, React et Docker.

## Stack technique

- Backend : FastAPI
- Base de données : PostgreSQL
- ORM : SQLAlchemy
- Frontend : React + Vite
- Conteneurisation : Docker & Docker Compose
- Tests : Pytest

---

## Fonctionnalités

- Enregistrement d'événements utilisateur
- Consultation de l'historique des événements
- Filtrage des événements par utilisateur et catégorie
- Génération d'un résumé statistique par utilisateur
- Interface web responsive adaptée aux ordinateurs, tablettes et mobiles
- Déploiement simplifié via Docker Compose

---

## Architecture du projet

```text
centre-suivi-evenements/

├── backend/
│   ├── app/
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── models/
│   │   │   └── event.py
│   │   ├── routers/
│   │   │   ├── events.py
│   │   │   └── users.py
│   │   ├── schemas/
│   │   │   └── event.py
│   │   └── services/
│   │       └── event_service.py
│   │
│   ├── tests/
│   │   └── test_events.py
│   │
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── Dockerfile
│   └── package.json
│
├── docker-compose.yml
└── README.md
```

---

## Lancement du projet

### Avec Docker

```bash
docker compose up --build
```

ou

```bash
sudo docker compose up --build
```

---

## Accès aux services

### Frontend

```text
http://localhost:5173
```

### Backend

```text
http://localhost:8000
```

### Documentation Swagger

```text
http://localhost:8000/docs
```

---

## Endpoints disponibles

### Vérification de l'API

```http
GET /
```

Réponse :

```json
{
  "status": "ok",
  "message": "API is running"
}
```

---

### Création d'un événement

```http
POST /events
```

Exemple :

```json
{
  "user_id": "user_1",
  "type": "login",
  "payload": {
    "ip": "127.0.0.1",
    "device": "web"
  }
}
```

Réponse :

```json
{
  "message": "Event created",
  "id": 1
}
```

---

### Liste des événements

```http
GET /events
```

Filtrage :

```http
GET /events?user_id=user_1
```

```http
GET /events?type=login
```

```http
GET /events?user_id=user_1&type=login
```

---

### Résumé d'un utilisateur

```http
GET /users/{user_id}/summary
```

Exemple :

```http
GET /users/user_1/summary
```

Réponse :

```json
{
  "user_id": "user_1",
  "total_events": 5,
  "event_types": {
    "login": 3,
    "report": 2
  }
}
```

---

## Tests

Depuis le dossier backend :

```bash
PYTHONPATH=. pytest
```

---

## Choix d'architecture

Le backend est organisé en plusieurs couches :

### Routers

Gestion des routes HTTP.

### Schemas

Validation des données avec Pydantic.

### Models

Définition des tables PostgreSQL avec SQLAlchemy.

### Services

Logique métier indépendante des routes.

### Database

Gestion de la connexion à PostgreSQL.

Cette séparation permet d'obtenir un code lisible, maintenable, évolutif et facilement testable.

---

## Sécurité

L'authentification JWT n'a pas été implémentée afin de respecter le périmètre du test technique et de privilégier la qualité du code, la documentation, les tests et les fonctionnalités demandées.

L'architecture actuelle permet toutefois l'ajout simple d'une authentification JWT dans une évolution future du projet.

---

## Améliorations possibles

- Authentification JWT
- Pagination des événements
- Validation métier avancée
- Gestion centralisée des erreurs
- Base de données de test dédiée
- Couverture de tests plus complète
- Migrations Alembic
- Déploiement cloud

---

## Temps passé

Environ 3 heures de développement, incluant :(13h jusqu'à 15h 25 mn)

- la conception de l'architecture backend ;
- l'intégration PostgreSQL ;
- le développement de l'interface React ;
- la conteneurisation Docker ;
- la rédaction de la documentation et des tests.