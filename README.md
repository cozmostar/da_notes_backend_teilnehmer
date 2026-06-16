# Notes Backend (Django)

Python-Django-Backend für das Frontend `da_notes_frontend_teilnehmer`.

Es stellt die folgende REST-API bereit:

- `GET /notes/`
- `POST /notes/`
- `PUT /notes/{id}/`
- `DELETE /notes/{id}/`

## Datenmodell

- `id: UUID` (wird serverseitig generiert)
- `title: string`
- `content: string`
- `marked: boolean`
- `trash: boolean`

## Setup

```bash
cd da_notes_backend_teilnehmer
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py runserver 127.0.0.1:8000
```

## API testen

```bash
curl http://127.0.0.1:8000/notes/
curl -X POST http://127.0.0.1:8000/notes/ \
  -H 'Content-Type: application/json' \
  -d '{"title":"Neue Notiz","content":"Hallo Welt","marked":false,"trash":false}'
```
