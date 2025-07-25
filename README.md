# ToDo API - Django REST Framework

Ez a projekt egy egyszerű, Django REST API-ban készült alkalmazás, amely a ReqRes külső szolgáltatásán keresztül hitelesít, és felhasználói feladatokat (to-do-kat) kezel.

A fejlesztés Ubuntu 22 rendszeren történt.

---

## Telepítés

1. Klónozd a projektet, majd lépj be a mappába:

   ```bash
   git clone <repo-url>
   cd <repo-folder>
   ```

2. Hozz létre egy virtuális környezetet és aktiváld:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Szükséges csomagok telepítése:

   ```bash
   pip install -r requirements.txt
   ```

4. Migrációk futattása:

   ```bash
   python3 manage.py migrate
   ```

5. Szerver indítása:

   ```bash
   python3 manage.py runserver
   ```

---

## Bejelentkezés

A bejelentkezés a `POST /login` végponton történik:

```json
{
  "email": "eve.holt@reqres.in",
  "password": "cityslicka"
}
```

Sikeres bejelentkezés után a token automatikusan elmentésre kerül a session-ben. Ez szükséges a védett végpontok (felhasználók és feladatok) eléréséhez.

---

## Példa végpontok

### POST /login – Bejelentkezés (ReqRes API-n keresztül)

### URL: POST http://127.0.0.1:8000/login

**INPUT:**

```json
{
  "email": "eve.holt@reqres.in",
  "password": "cityslicka"
}
```

**OUTPUT:**
```json
{
  "token": "QpwL5tke4Pnpja7X4"
}
```

---

### GET /users – Felhasználók lekérése

### URL: GET http://127.0.0.1:8000/users

**OUTPUT:**
```json
{
  "page": 1,
  "per_page": 6,
  "total": 12,
  "total_pages": 2,
  "data": [
    {
        "id": 1,
        "email": "george.bluth@reqres.in",
        "first_name": "George",
        "last_name": "Bluth",
        "avatar": "https://reqres.in/img/faces/1-image.jpg"
    },
    {
        "id": 2,
        "email": "janet.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": "https://reqres.in/img/faces/2-image.jpg"
    },
    {
        "id": 3,
        "email": "emma.wong@reqres.in",
        "first_name": "Emma",
        "last_name": "Wong",
        "avatar": "https://reqres.in/img/faces/3-image.jpg"
    },
    {
        "id": 4,
        "email": "eve.holt@reqres.in",
        "first_name": "Eve",
        "last_name": "Holt",
        "avatar": "https://reqres.in/img/faces/4-image.jpg"
    },
    {
        "id": 5,
        "email": "charles.morris@reqres.in",
        "first_name": "Charles",
        "last_name": "Morris",
        "avatar": "https://reqres.in/img/faces/5-image.jpg"
    },
    {
        "id": 6,
        "email": "tracey.ramos@reqres.in",
        "first_name": "Tracey",
        "last_name": "Ramos",
        "avatar": "https://reqres.in/img/faces/6-image.jpg"
    }
  ],
  "support": {
    "url": "https://contentcaddy.io",
    "text": "Tired of writing endless social media content? Let Content Caddy generate it for you."
  }
}
```

---

### GET /users/id/tasks – Egy felhasználó feladatainak listázása

### URL: GET http://127.0.0.1:8000/users/2/tasks

```json
[
    {
        "id": 1,
        "user_id": 2,
        "title": "title",
        "description": "Description",
        "startdate": "2025-07-25T00:00:00Z",
        "deadline": "2025-07-26T00:00:00Z",
        "completed": true
    },
    {
        "id": 2,
        "user_id": 2,
        "title": "title 2",
        "description": "Description 2",
        "startdate": "2025-07-24T00:00:00Z",
        "deadline": "2025-07-25T00:00:00Z",
        "completed": false
    },
    {
        "id": 3,
        "user_id": 2,
        "title": "title 3",
        "description": "Description 3",
        "startdate": "2025-07-24T00:00:00Z",
        "deadline": "2025-07-25T00:00:00Z",
        "completed": false
    },
    {
        "id": 4,
        "user_id": 2,
        "title": "title 4",
        "description": "Description 4",
        "startdate": "2025-07-24T00:00:00Z",
        "deadline": "2025-07-25T00:00:00Z",
        "completed": false
    }
]
```

### POST /users/<id>/tasks – Új feladat hozzáadása

### URL: POST http://127.0.0.1:8000/users/2/tasks

**INPUT:**
```json
{
  "title": "Dokumentáció írása",
  "description": "README és Postman kérések",
  "startdate": "2025-07-23T14:00:00Z",
  "deadline": "2025-07-25T18:00:00Z",
  "completed": false
}
```

**OUTPUT:**
```json
{
  "id": 5,
  "user_id": 2,
  "title": "Dokumentáció írása",
  "description": "README és Postman kérések",
  "startdate": "2025-07-23T14:00:00Z",
  "deadline": "2025-07-25T18:00:00Z",
  "completed": false
}
```

### GET /users/<id>/tasks/<task_id> – Feladat részletei

### URL: GET http://127.0.0.1:8000/users/2/tasks/5

```json
{
  "id": 5,
  "user_id": 2,
  "title": "Dokumentáció írása",
  "description": "README és Postman kérések",
  "startdate": "2025-07-23T14:00:00Z",
  "deadline": "2025-07-25T18:00:00Z",
  "completed": false
}
```

### PUT /users/<id>/tasks/<task_id> – Feladat módosítása

### URL: PUT http://127.0.0.1:8000/users/2/tasks/5

**INPUT:**
```json
{
  "title": "Új feladatcím",
  "description": "Ez a feladat leírásának frissített változata.",
  "completed": true,
  "startdate": "2025-07-25",
  "deadline": "2025-08-01"
}
```

**OUTPUT:**
```json
{
  "id": 5,
  "user_id": 2,
  "title": "Új feladatcím",
  "description": "Ez a feladat leírásának frissített változata.",
  "startdate": "2025-07-25T00:00:00Z",
  "deadline": "2025-08-01T00:00:00Z",
  "completed": true
}
```

### DELETE /users/<id>/tasks/<task_id> – Feladat törlése

```
DELETE http://127.0.0.1:8000/users/2/tasks/5
```

---

## Megjegyzés

A hitelesítés csak akkor működik, ha előzőleg sikeresen bejelentkeztél. A token automatikusan tárolódik a session-ben, és minden további kérésnél használatra kerül.

## Kijelentkezés

A kijelentkezéshez használd a `POST /logout` végpontot:

### URL: POST http://127.0.0.1:8000/logout

Ez törli a session-ben tárolt tokent, és megszünteti a hitelesített kapcsolatot.

