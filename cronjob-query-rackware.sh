#!/bin/bash

rw -j job query > $(pwd)/mock-rackware.txt || echo \{"success": false\} > $(pwd)/mock-rackware.txt


