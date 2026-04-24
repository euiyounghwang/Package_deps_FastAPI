# SSE (Server-Sent Events)
<i> Package_deps_FastAPI

Server-Sent Events (SSE) in Python allow servers to push real-time data to clients over a persistent HTTP connection using the text/event-stream format. SSE is commonly used for AI chat streaming, live notifications, logs and observability, and other cases where the server pushes updates to the client

### Run SSE client
- Reference : https://towardsdatascience.com/introducing-server-sent-events-in-python/
- http://localhost:8000/stream
```bash
data: The time is 16:20:10

data: The time is 16:20:11

data: The time is 16:20:12

data: The time is 16:20:13

data: The time is 16:20:14

data: The time is 16:20:15

data: The time is 16:20:16

data: The time is 16:20:17

data: The time is 16:20:18

data: The time is 16:20:19

data: The time is 16:20:20

data: The time is 16:20:21

data: The time is 16:20:22

data: The time is 16:20:23

data: The time is 16:20:24
```

- python ./sse-client.py
```bash
data: The time is 16:20:10

data: The time is 16:20:11
```