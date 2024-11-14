# Use Node.js as base image for building the Vue app
FROM node:16

# Set the working directory inside the container
WORKDIR /app

# Copy the frontend code into the container
COPY . /app

# Install dependencies and build the Vue app
RUN npm install
RUN npm run build

# Install serve to serve the built app
RUN npm install -g serve

# Expose the port where the app will run
EXPOSE 5000

# Command to serve the Vue app
CMD ["serve", "-s", "dist", "-l", "5000"]