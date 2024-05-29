#!/bin/bash

rw -j job query > $(pwd)/mock/mock-rackware.txt || echo \{"success": false\} > $(pwd)/mock/mock-rackware.txt


