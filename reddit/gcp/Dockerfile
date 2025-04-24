FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Install only the required Python dependencies
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app code into the container
COPY . .

# Expose the FastAPI app port
EXPOSE 8080

# Start FastAPI using Uvicorn
CMD ["uvicorn", "redditApp:app", "--host", "0.0.0.0", "--port", "8080"]