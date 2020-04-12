#!/bin/bash
# show status code
curl -s -L -I "$1" -o /dev/null -w '%{http_code}'
