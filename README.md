ToDo API - Django REST Framework

Ez a projekt egy egyszerű, Django REST API-ban készült alkalmazás, amely a ReqRes külső szolgáltatásán keresztül hitelesít, és felhasználói feladatokat (to-do-kat) kezel.

A fejlesztés Ubuntu 22 rendszeren történt.

Telepítés

1. Klónozd a projektet, majd lépj be a mappába:

    git clone <repo-url>

2. Hozz létre egy virtuális környezetet és aktiváld:

    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate

3. Telepítsd a szükséges csomagokat:

    pip install -r requirements.txt

4. Futtasd a migrációkat:

    python manage.py migrate

5. Indítsd el a szervert:

    python manage.py runserver

Bejelentkezés

A bejelentkezéshez a localhost/login oldalon történik:

{
  "email": "eve.holt@reqres.in",
  "password": "cityslicka"
}

Sikeres bejelentkezés után a token automatikusan elmentésre kerül a session-ben. Ez szükséges a védett végpontok (felhasználók és feladatok) eléréséhez.

Példa végpontok

- POST /login – Bejelentkezés (ReqRes API-n keresztül)
- GET /users – Felhasználók lekérése (külső API)
- GET /users/<id>/tasks – Egy felhasználó feladatainak listázása
- POST /users/<id>/tasks – Új feladat hozzáadása
- GET /users/<id>/tasks/<task_id> – Feladat részletei
- PUT /users/<id>/tasks/<task_id> – Feladat módosítása
- DELETE /users/<id>/tasks/<task_id> – Feladat törlése

Megjegyzés

A hitelesítés csak akkor működik, ha előzőleg sikeresen bejelentkeztél. A token automatikusan tárolódik a session-ben, és minden további kérésnél használatra kerül.
