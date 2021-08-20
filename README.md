# color-loop-hue
A simple docker container to make a color loop for a specific lights Hue group.

## Compose
You can create a Docker container, with the official and latest Docker image available on [Docker Hub](https://hub.docker.com/r/alexthegeek/color-loop-hue).  
Before start the container, you need to change the variables in the `env` file.  
Example compose command to deploy the container.
```shell
sudo docker-compose -f docker-compose.yml -p hue_loop --env-file env up -d
```

## Build your own Docker Image
You can build your proper Docker image with the files in the `Build Docker` folder.
```shell
sudo docker build -t color-loop-hue .
```

## Code
All the code can be found in the `App Code` folder.

## Credit
Alexis Brunet  
contact[at]lapinfo[dot]fr.
