# Use Python 3.10 slim image as base
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install poetry
RUN pip install poetry

# Copy poetry files
COPY pyproject.toml poetry.lock* ./

# Configure poetry to not create a virtual environment inside the container
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --no-dev --no-interaction --no-ansi

# Copy application code
COPY . .

# Create instance directories
RUN mkdir -p instance/uploads instance/results

# Set environment variables
ENV FLASK_APP=run.py
ENV FLASK_ENV=production

# Expose port
EXPOSE 6000

# Run the application
CMD ["poetry", "run", "python", "run.py"]
