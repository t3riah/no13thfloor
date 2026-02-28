#!/bin/bash
set -e

echo "→ Pulling latest..."
git pull origin main

echo "→ Building containers..."
docker compose build --no-cache

echo "→ Restarting services..."
docker compose down
docker compose up -d

echo "→ Health check..."
sleep 5
curl -sf http://localhost:8000/health && echo "✓ App healthy" || echo "✗ Health check failed"

echo "→ Done. No 13th Floor is live."
