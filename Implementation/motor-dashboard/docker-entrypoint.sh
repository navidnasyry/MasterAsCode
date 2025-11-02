#!/bin/sh

# Generate runtime configuration
envsubst < /usr/share/nginx/html/config/config.js.template > /usr/share/nginx/html/config/config.js

# Start nginx
exec nginx -g 'daemon off;'