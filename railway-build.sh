#!/bin/bash
echo "Database migration started"
alembic upgrade head
echo "================================"
