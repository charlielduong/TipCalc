# Start from a base Python 3.11 image on Debian buster
FROM python:3.11-buster

# Install Tesseract OCR and other necessary packages
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    && rm -rf /var/lib/apt/lists/*

# Create the working directory
RUN mkdir app
WORKDIR /app

# Set environment variables
ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.

# Copy and install the requirements
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the source code into the Docker image
COPY src/ .
