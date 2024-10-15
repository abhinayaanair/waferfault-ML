# Use a base image
FROM python:3.8

# Set working directory
WORKDIR /app

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --timeout=100 -r requirements.txt

# Copy the rest of the application code
COPY . .

# Command to run your application
CMD ["python", "app.py"]
