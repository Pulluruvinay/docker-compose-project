# Use Node.js for building and running React
FROM node:18-alpine

WORKDIR /app

# Copy package.json and install dependencies
COPY package.json .
RUN npm install

# Copy source code
COPY . .

# Expose port for React dev server
EXPOSE 3000

# Start the React app
CMD ["npm", "start"]
