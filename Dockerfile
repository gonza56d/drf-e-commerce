FROM python:3.10-slim

# Upgrade pip and set work directory
RUN pip install --upgrade pip
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .
