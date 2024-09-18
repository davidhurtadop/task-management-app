# Use the official Python image from the Docker Hub
FROM python:3.12.5-slim

# Set the working directory to /app/src before installing dependencies
WORKDIR /app/src

# Install dependencies
COPY requirements.txt /app/src/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Remove unnecessary files and directories in a single RUN step
RUN rm -rf requirements.txt

WORKDIR /app

# Use only when run docker build
# COPY .env /app/

# Copy the source code into the container
COPY ./src/ /app/src/

# Expose the port your Flask app listens on
EXPOSE 5000

# Set the entry point for the container
CMD ["python", "-m", "src.main"]