#!/bin/bash

docker run -d -v "$(pwd)":/app/mock:ro -p 8779:4557 rw-exporter:latest
