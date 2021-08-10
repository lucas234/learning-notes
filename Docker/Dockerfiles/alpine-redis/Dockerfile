FROM alpine:latest
MAINTAINER liulucas
RUN apk update && apk add --no-cache redis
EXPOSE 6379
CMD ["redis-server", "--protected-mode no"] # --daemonize yes  



