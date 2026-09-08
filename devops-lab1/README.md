# DevOps Lab 1 — Dockerized Flask App

## Files
- `Dockerfile`
- `app.py`
- `requirements.txt`

## Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

## Build
```bash
docker build -t my-app .
```

## Run
```bash
docker run -d -p 5000:5000 --name my-container my-app
```

## Verify
- App: http://localhost:5000
- Enter container: `docker exec -it my-container /bin/sh`

## Screenshots
![Browser](./screenshots/browser.png)
![Terminal](./screenshots/terminal.png)
