# Use Python as the base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only the requirements file first to leverage Docker cache
COPY requirements.txt /app/

# Create and activate a virtual environment
RUN python -m venv /env
ENV PATH="/env/bin:$PATH"

# Install backend dependencies (Flask, gunicorn, etc.)
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the backend code into the container
COPY . /app/

# Expose the port that the Flask app will run on
EXPOSE 5000

# Set the default command to run the Flask app using gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]