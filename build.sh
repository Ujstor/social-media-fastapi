#!/bin/bash
echo "Database migration started"
echo "================================"
alembic upgrade head
echo "================================"
echo "Database migration completed"
echo "Starting server"
uvicorn app.main:app --host=0.0.0.0 --port=${PORT:-8000}