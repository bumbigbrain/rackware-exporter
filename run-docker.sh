#!/bin/bash

docker run -d -v "$(pwd)"/mock:/app/mock:ro -p 8779:4557 rw-exporter:latest
