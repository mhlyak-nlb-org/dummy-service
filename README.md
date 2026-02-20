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


## Priporočila za produkcijsko uporabo in CI/CD

Pipeline, ki je implementiran, je primeren za lokalno testiranje in domačo uporabo. 
Če bi aplikacija tekel v produkcijskem okolju z več razvijalci in visokimi zahtevami za varnost, zanesljivost in sledljivost, priporočamo naslednje izboljšave:

### Varnost
- Upravljanje skrivnosti preko GitHub Secrets (gesla, API ključi, GHCR login).
- Uporaba minimalnih Docker image-ov (npr. `python:3.12-alpine`) in multi-stage build.
- Varnostni scanning: `docker scan`, `pip-audit` ali `safety` za Python dependencies.

### Zanesljivost in testiranje
- Automatizirani unit in integration testi pred build/push.
- Ločeno staging okolje za testiranje pred produkcijo.
- CI/CD pipeline razdeljen na: build & test → push Docker image → deploy staging → deploy production po odobritvi.
- Rollback strategija za hitre vrnitve na prejšnjo verzijo slike.

### Sledljivost in monitoring
- Centralni logging in monitoring (npr. ELK stack, Prometheus + /metrics endpoint).
- Audit trail: kdo je sprožil deploy, katera verzija kode in Docker slike.

### Skaliranje
- Produkcijsko okolje naj uporablja orkestrator (Kubernetes, Docker Swarm, ECS) namesto samo Docker Compose.
- Semantično verzioniranje in taganje Docker image-ov (npr. git commit hash ali semantic version).