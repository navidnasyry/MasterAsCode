#!/bin/bash

# Set default API base URL if not provided
if [ -z "$REACT_APP_API_BASE_URL" ]; then
  export REACT_APP_API_BASE_URL="http://localhost:8000/api"
fi

echo "Using API Base URL: $REACT_APP_API_BASE_URL"

# Create runtime config file
cat > /usr/share/nginx/html/runtime-config.js <<EOF
window.RUNTIME_CONFIG = {
  REACT_APP_API_BASE_URL: "$REACT_APP_API_BASE_URL"
};
EOF

# Substitute environment variables in nginx config
envsubst '${REACT_APP_API_BASE_URL}' < /etc/nginx/conf.d/default.conf.template > /etc/nginx/conf.d/default.conf

# Start nginx
exec nginx -g 'daemon off;'