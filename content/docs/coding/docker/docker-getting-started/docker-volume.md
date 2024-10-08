---
linktitle: ''
summary: ''
weight: 16
title: Docker Volume
date: 2020-02-06
draft: false

authors:
- admin
tags:
- Docker
- getting-started
categories:
- Coding
toc: true
profile: false
reading_time: true
share: true
featured: true
comments: true
disable_comment: false
commentable: true
editable: false
header:
  caption: ''
  image: ''
---

In general, Docker containers are **ephemeral**, running just as long as it takes for the command issued in the container to complete. By default, any data created inside the container is ONLY available from within the container and only while the container is running.

Docker **volumes** can be used to share files between a host system and the Docker container. 

## Bindmounting a Volume

We can use `-v` flag in `docker run` to bind mount a volume. Let's take a look at an example, which will create a directory called `nginxlogs` in your current user’s home directory and bindmount it to `/var/log/nginx` in the container:

```bash
docker run --name=nginx -d -v ~/nginxlogs:/var/log/nginx -p 5000:80 nginx
```

`-v ~/nginxlogs:/var/log/nginx` sets up a bindmount volume that links the `/var/log/nginx` directory from inside the Nginx container to the `~/nginxlogs` directory on the host machine. Docker uses a `:` to split the host’s path from the container path, and the **host path always comes first**.

{{% callout note%}} 

If the first argument of `-v` begins with a `/` or `~/`, you’re creating a bindmount. Remove that, and you’re naming the volume.

- `-v /path:/path/in/container` mounts the host directory, `/path` at the `/path/in/container`
- `-v path:/path/in/container` creates a volume named `path` with no relationship to the host.

{{% /callout %}}

If you make any changes to the `~/nginxlogs` folder, you’ll be able to see them from inside the Docker container in real time as well. In other words, the content of `~/nginxlogs` and `/var/log/nginx` are synchronous.

## Reference

- [Use bind mounts](https://docs.docker.com/storage/bind-mounts/): Docker official documentation

- [How To Share Data Between the Docker Container and the Host](https://www.digitalocean.com/community/tutorials/how-to-share-data-between-the-docker-container-and-the-host)
- [Docker Basics: How to Share Data Between a Docker Container and Host](https://thenewstack.io/docker-basics-how-to-share-data-between-a-docker-container-and-host/)
- [Docker Volume - 目录挂载以及文件共享](https://kebingzao.com/2019/02/25/docker-volume/)