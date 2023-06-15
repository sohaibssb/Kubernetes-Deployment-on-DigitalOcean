# Fetching the latest node image on alpine linux
FROM node:alpine AS development
WORKDIR /app
COPY package.json ./
COPY package-lock.json ./
RUN npm install

COPY . ./
CMD ["npm", "start"]