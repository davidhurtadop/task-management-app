# Use a lightweight Node.js image as the base
FROM node:18-alpine 

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json (if you have one)
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of your application code
COPY . .

# Build the React application
RUN npm run build

# Stage 2: Production-ready Nginx server
FROM nginx:alpine

# Copy the build output from the previous stage to the Nginx web root
COPY --from=0 /app/build /usr/share/nginx/html

# Expose port 80 for the Nginx web server
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
