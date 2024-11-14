# Use Python as the base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt first to install dependencies
COPY requirements.txt /app/

# Create and activate a virtual environment
RUN python -m venv /env
ENV PATH="/env/bin:$PATH"

# Upgrade pip and install dependencies from requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the game logic code into the container
COPY . /app/

# Expose any necessary ports (if required by your service)
EXPOSE 5000

# Set the default command to run the game logic app (adjust based on how you run it)
CMD ["python", "game_terminal.py"]