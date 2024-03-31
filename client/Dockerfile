FROM node:lts-alpine

# Set working directory
WORKDIR /app

# Add npm global path to PATH environment variable
ENV PATH /app/node_modules/.bin:$PATH

# Install Vue CLI
RUN npm install @vue/cli@5.0.8 -g

# Copy package.json and package-lock.json
COPY package.json .
COPY package-lock.json .

# Install dependencies
RUN npm install

# Install bootstrap
RUN npm install bootstrap

# Copy the rest of the application code
COPY . .

CMD ["npm", "run", "serve"]