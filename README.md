# Proxy Relay Server

This repository contains a V2Ray (V2Fly) Docker Compose to run a relay (bridge) server.
It supports shadowsocks (Shadowsocks24, Outline, and shadowsocks-libev) and any other protocol based on TCP and UDP.
A proxy relay server will let you bypass restricted networks with no safe, direct, or stable access to upstream (exit)
servers.

## Documentation

### What is a proxy relay server?

The proxy servers like Shadowsocks24 usually work as below.
The clients connect to upstream (exit) servers directly.

```
[client] <-> [upstream server] <-> (Internet)
```

Where this direct connection is not possible, unsafe, or unstable, you must use a relay server with a better connection
to clients and upstream servers.
This repository is a proxy relay server based on the V2Ray proxy (dokodemo-door protocol) that can pass incoming TCP and
UDP traffic to specified upstream (exit) servers.
It supports shadowsocks and any other proxy and non-proxy protocols that are based on TCP or UDP.

The proxy relay server changes the flow as below.

```
[client] <-> [relay server] <-> [upstream server] <-> (Internet)
```

#### Set up the proxy relay

Follow these steps to run a V2Ray proxy as the proxy relay server.

1. Install Docker and Docker-compose.
2. Clone (copy) this repository into the bridge server.
3. Run `./setup.py` script. It gets the following inputs:
    1. `Enter number of upstream servers:`: Number of upstream servers to set up.
    2. `Enter server #i IP address:`: The i-th server IP address.
    3. `Enter server #i port number: `: The i-th server port number.
4. Run `docker-compose up -d` or `docker compose up -d`.
5. Replace upstream server IP in proxy links with relay server IP.

### Docker images

By default, this repository uses the GitHub registry.
You can modify the Docker-compose file to use Docker Hub.

* GitHub:
    * Image: ```ghcr.io/internet24/v2fly-core:v4.45.2```
    * URL: https://github.com/orgs/internet24/packages/container/package/v2fly-core
    * Digest: `sha256:289fc9451f21a265f95615e29f05ea23bc32026db152863eee317738813521d7`
* Docker Hub:
    * Image: ```v2fly/v2fly-core:v4.45.2```
    * URL: https://hub.docker.com/r/v2fly/v2fly-core/tags
    * Digest: `sha256:289fc9451f21a265f95615e29f05ea23bc32026db152863eee317738813521d7`
