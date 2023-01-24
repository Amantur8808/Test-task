#
# node:14-alpine image is used as the base image instead of ubuntu:18.04, this image is smaller in size and comes with Node.js pre-installed.
FROM node:14-alpine

# WORKDIR command is used to set the working directory to /app.
WORKDIR /app

# COPY package*.json ./ copies package.json and package-lock.json to the working directory and npm ci --only=production runs to install only production dependencies. 
# This will improve the build caching and minimize the final image size. 
# This will improve the build caching and minimize the final image size.
COPY package*.json ./
RUN npm ci --only=production

# COPY ./src . command is used to copy the src to the working directory
COPY ./src .

ENTRYPOINT ["npm"]
CMD ["run", "prod"]
