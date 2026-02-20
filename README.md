# dummy-service

Tiny Python REST service.

## Run

```bash
cd /home/miheljakm/ws/.mm/dummy-service
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Test

```bash
curl -s http://localhost:8080/health
# {"health":"OK"}
```
# Testna sprememba za feature/test-change-2