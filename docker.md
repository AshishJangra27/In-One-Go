# 🐳 Docker Complete Command Cheat Sheet (Interview + Real-World)

This guide covers almost every commonly used Docker command including:

- Docker Core Commands
- Docker Images
- Docker Containers
- Docker Volumes
- Docker Networks
- Docker Compose
- Docker System & Cleanup
- Docker Logs & Debugging
- Docker Registry (Docker Hub)
- Docker Inspect & Monitoring

---

# Quick Summary

| Category | Most Important Commands |
|----------|--------------------------|
| Images | `build`, `images`, `pull`, `push`, `tag`, `rmi`, `inspect`, `history` |
| Containers | `run`, `ps`, `stop`, `start`, `restart`, `exec`, `logs`, `rm` |
| Volumes | `volume ls`, `volume create`, `volume inspect`, `volume rm` |
| Networks | `network ls`, `network create`, `network connect`, `network inspect`, `network rm` |
| Compose | `up`, `down`, `build`, `logs`, `ps`, `exec`, `run`, `restart`, `pull`, `config` |
| Cleanup | `container prune`, `image prune`, `volume prune`, `network prune`, `system prune` |
| Debugging | `inspect`, `logs`, `stats`, `top`, `events`, `diff`, `port`, `system df` |

---

# 1. Check Docker Version

```bash
docker --version
```

Shows installed Docker version.

```bash
docker version
```

Shows Client and Server versions.

---

# 2. Docker System Information

```bash
docker info
```

Displays Docker daemon information.

---

# 3. Docker Help

```bash
docker --help
```

Shows all Docker commands.

Specific help:

```bash
docker run --help
```

---

# Docker Images

Images are read-only templates used to create containers.

---

## 1. Build an Image

```bash
docker build -t myimage:latest .
```

Options

- `-t` → Name and tag
- `.` → Dockerfile location

Without cache

```bash
docker build --no-cache -t myimage .
```

Specify Dockerfile

```bash
docker build -f Dockerfile.dev -t myimage .
```

---

## 2. List Images

```bash
docker images
```

or

```bash
docker image ls
```

---

## 3. Pull an Image

```bash
docker pull ubuntu:latest
```

Downloads image from Docker Hub.

---

## 4. Push an Image

```bash
docker push username/myimage:v1
```

Uploads image to Docker Hub.

---

## 5. Tag an Image

```bash
docker tag myimage:latest username/myimage:v1
```

---

## 6. Remove an Image

```bash
docker rmi myimage:latest
```

Remove by ID

```bash
docker rmi IMAGE_ID
```

---

## 7. Inspect an Image

```bash
docker inspect myimage
```

Shows metadata in JSON.

---

## 8. Image History

```bash
docker history myimage
```

Shows image layers.

---

## 9. Save an Image

```bash
docker save -o myimage.tar myimage
```

---

## 10. Load an Image

```bash
docker load -i myimage.tar
```

---

## 11. Create Image from Running Container

```bash
docker commit container_id myimage:v1
```

---

# Docker Containers

Containers are running instances of images.

---

## 1. Run a Container

```bash
docker run nginx
```

Detached mode

```bash
docker run -d nginx
```

Interactive mode

```bash
docker run -it ubuntu bash
```

Name container

```bash
docker run --name web nginx
```

Port mapping

```bash
docker run -p 8080:80 nginx
```

Volume mount

```bash
docker run -v myvolume:/data nginx
```

Bind mount

```bash
docker run -v $(pwd):/app nginx
```

Environment variables

```bash
docker run -e ENV=production nginx
```

Restart policy

```bash
docker run --restart always nginx
```

Auto remove

```bash
docker run --rm ubuntu
```

---

## 2. List Running Containers

```bash
docker ps
```

All containers

```bash
docker ps -a
```

---

## 3. Stop Container

```bash
docker stop container_name
```

---

## 4. Start Container

```bash
docker start container_name
```

---

## 5. Restart Container

```bash
docker restart container_name
```

---

## 6. Pause Container

```bash
docker pause container_name
```

---

## 7. Resume Container

```bash
docker unpause container_name
```

---

## 8. Kill Container

```bash
docker kill container_name
```

---

## 9. Remove Container

```bash
docker rm container_name
```

Force remove

```bash
docker rm -f container_name
```

---

## 10. Rename Container

```bash
docker rename old_name new_name
```

---

## 11. Execute Commands

```bash
docker exec -it container bash
```

Example

```bash
docker exec -it web python app.py
```

---

## 12. Attach to Container

```bash
docker attach container_name
```

---

## 13. Copy Files

Host → Container

```bash
docker cp file.txt container:/tmp
```

Container → Host

```bash
docker cp container:/tmp/file.txt .
```

---

## 14. Inspect Container

```bash
docker inspect container_name
```

---

## 15. View Processes

```bash
docker top container_name
```

---

## 16. View Resource Usage

```bash
docker stats
```

Specific container

```bash
docker stats container_name
```

---

# Docker Logs

## View Logs

```bash
docker logs container_name
```

Follow logs

```bash
docker logs -f container_name
```

Last 100 lines

```bash
docker logs --tail 100 container_name
```

---

# Docker Volumes

Volumes persist data.

---

## List Volumes

```bash
docker volume ls
```

---

## Create Volume

```bash
docker volume create myvolume
```

---

## Inspect Volume

```bash
docker volume inspect myvolume
```

---

## Remove Volume

```bash
docker volume rm myvolume
```

---

## Remove Unused Volumes

```bash
docker volume prune
```

---

# Docker Networks

Networks allow containers to communicate.

---

## List Networks

```bash
docker network ls
```

---

## Create Network

```bash
docker network create mynetwork
```

---

## Inspect Network

```bash
docker network inspect mynetwork
```

---

## Connect Container

```bash
docker network connect mynetwork container_name
```

---

## Disconnect Container

```bash
docker network disconnect mynetwork container_name
```

---

## Remove Network

```bash
docker network rm mynetwork
```

---

## Remove Unused Networks

```bash
docker network prune
```

---

# Docker Compose

Docker Compose manages multi-container applications.

---

## Start Services

```bash
docker compose up
```

Detached

```bash
docker compose up -d
```

---

## Build Images

```bash
docker compose build
```

Without cache

```bash
docker compose build --no-cache
```

---

## Build and Restart

```bash
docker compose up --build
```

---

## Stop Services

```bash
docker compose stop
```

---

## Start Stopped Services

```bash
docker compose start
```

---

## Restart Services

```bash
docker compose restart
```

Specific service

```bash
docker compose restart web
```

---

## Remove Everything

```bash
docker compose down
```

Remove volumes too

```bash
docker compose down -v
```

---

## View Running Services

```bash
docker compose ps
```

---

## View Logs

```bash
docker compose logs
```

Live logs

```bash
docker compose logs -f
```

Specific service

```bash
docker compose logs -f web
```

---

## Execute Commands

```bash
docker compose exec web bash
```

Example

```bash
docker compose exec web python manage.py migrate
```

---

## Run One-Time Commands

```bash
docker compose run web bash
```

Example

```bash
docker compose run web python manage.py createsuperuser
```

---

## Pull Latest Images

```bash
docker compose pull
```

---

## Validate Compose File

```bash
docker compose config
```

---

## Scale Services

```bash
docker compose up --scale web=3 -d
```

---

# Docker System Cleanup

---

## Remove Unused Containers

```bash
docker container prune
```

---

## Remove Unused Images

```bash
docker image prune
```

All unused images

```bash
docker image prune -a
```

---

## Remove Unused Volumes

```bash
docker volume prune
```

---

## Remove Unused Networks

```bash
docker network prune
```

---

## Remove Everything Unused

```bash
docker system prune
```

Including images

```bash
docker system prune -a
```

Including volumes

```bash
docker system prune -a --volumes
```

---

# Docker Login & Registry

Login

```bash
docker login
```

Logout

```bash
docker logout
```

Search Docker Hub

```bash
docker search nginx
```

---

# Docker Export & Import

Export container

```bash
docker export container_name > container.tar
```

Import container

```bash
docker import container.tar myimage
```

---

# Docker Events

Monitor Docker events

```bash
docker events
```

---

# Docker Diff

Show filesystem changes

```bash
docker diff container_name
```

---

# Docker Port

Show mapped ports

```bash
docker port container_name
```

---

# Docker System Disk Usage

```bash
docker system df
```

Shows disk usage by:

- Images
- Containers
- Volumes
- Build Cache

---

# Docker Builder Cache

Remove build cache

```bash
docker builder prune
```

---

# Common Docker Run Options

| Option | Description |
|---------|-------------|
| `-d` | Detached mode |
| `-it` | Interactive terminal |
| `--name` | Container name |
| `-p` | Port mapping |
| `-v` | Mount volume |
| `-e` | Environment variable |
| `--rm` | Auto remove container |
| `--restart always` | Restart automatically |
| `--network` | Connect to network |

---

# Common Docker Build Options

| Option | Description |
|---------|-------------|
| `-t` | Tag image |
| `-f` | Specify Dockerfile |
| `--no-cache` | Ignore build cache |
| `.` | Build context |

---

# Docker Interview Workflow

## Step 1

Create Dockerfile

```bash
docker build -t myapp:v1 .
```

---

## Step 2

Verify image

```bash
docker images
```

---

## Step 3

Run container

```bash
docker run -d -p 8000:80 --name myapp myapp:v1
```

---

## Step 4

Check running containers

```bash
docker ps
```

---

## Step 5

View logs

```bash
docker logs -f myapp
```

---

## Step 6

Execute inside container

```bash
docker exec -it myapp bash
```

---

## Step 7

Stop application

```bash
docker stop myapp
```

---

## Step 8

Remove container

```bash
docker rm myapp
```

---

## Step 9

Push image

```bash
docker tag myapp:v1 username/myapp:v1
docker push username/myapp:v1
```

---

## Step 10

Deploy using Docker Compose

```bash
docker compose up -d
```

---

# ⭐ Top 30 Interview Commands

```bash
docker --version
docker info
docker build -t myapp .
docker images
docker pull ubuntu
docker push username/myapp
docker tag myapp username/myapp
docker run -d -p 8080:80 --name web nginx
docker ps
docker ps -a
docker stop web
docker start web
docker restart web
docker rm web
docker rmi myapp
docker exec -it web bash
docker logs -f web
docker inspect web
docker stats
docker volume ls
docker volume create data
docker network ls
docker network create mynetwork
docker compose up -d
docker compose down
docker compose build
docker compose logs -f
docker compose exec web bash
docker compose config
docker system prune -a --volumes
```

---

# Quick Summary

| Category | Most Important Commands |
|----------|--------------------------|
| Images | `build`, `images`, `pull`, `push`, `tag`, `rmi`, `inspect`, `history` |
| Containers | `run`, `ps`, `stop`, `start`, `restart`, `exec`, `logs`, `rm` |
| Volumes | `volume ls`, `volume create`, `volume inspect`, `volume rm` |
| Networks | `network ls`, `network create`, `network connect`, `network inspect`, `network rm` |
| Compose | `up`, `down`, `build`, `logs`, `ps`, `exec`, `run`, `restart`, `pull`, `config` |
| Cleanup | `container prune`, `image prune`, `volume prune`, `network prune`, `system prune` |
| Debugging | `inspect`, `logs`, `stats`, `top`, `events`, `diff`, `port`, `system df` |

---

🎯 **Interview Tip:** Master the commands in the **Top 30 Interview Commands** section first. They cover the vast majority of Docker tasks you'll encounter in interviews and day-to-day development.
