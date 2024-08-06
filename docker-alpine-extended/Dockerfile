# Start from the Alpine base image
FROM alpine:latest

# Install curl
RUN apk add --no-cache curl

# Copy the configuration file into the container
COPY config.txt /app/config.txt

# Set the default command to run
CMD ["sh"]
