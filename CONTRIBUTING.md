# CONTRIBUTING

## How to run the Dockerfile locally

```
docker build -t IMAGE_NAME .
docker run -dp 5000:5000 -w /app -v "$(pwd):/app" IMAGE_NAME sh -c "flask run"
```

## Command for generating JWT secret key

```
import secrets
secrets.SystemRandom().getrandbits(128)
```

## Command for running background worker

```
docker run -w /app first-app-restapi sh -c "rq worker -u rediss://red-ceu14lpgp3jmgl2lim00:f5uqZMFULwZFSSieFXuS3Y8Pm9B3om7e@oregon-redis.render.com:6379 emails"
```