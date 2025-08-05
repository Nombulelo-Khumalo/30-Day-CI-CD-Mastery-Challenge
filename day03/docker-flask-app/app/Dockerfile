# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy code
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port & run app
EXPOSE 5000
CMD ["python", "app/main.py"]
