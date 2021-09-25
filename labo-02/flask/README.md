# Start with docker

## Install Docker

Ref : https://docs.docker.com/get-docker/

## Build containers

From the `flask` directory, run the following command:

`docker-compose up`

This will:

1. Download python image
2. Build the image
3. Assemble everything and start the container with the `docker-compose.yml` file
4. Run flask app as development mode

**_Note_**: Ensure port `5000` is free.

Visit: `http://localhost:5000` and enjoy !
