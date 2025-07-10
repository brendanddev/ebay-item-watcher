
# Dockerfile defining the environment for the ebay item watcher app
# Brendand Dileo - July 2025

# Use lightweight python image as base
FROM python:3.12-slim

# Set working dir inside the container
WORKDIR /app

# Install cron
RUN apt-get update && \
    apt-get install -y cron && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*