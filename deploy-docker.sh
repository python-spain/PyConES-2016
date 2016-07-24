#!/bin/bash
echo "...Updating pycones-2016: Fetch code from github"
git fetch origin
git reset --hard origin/master
echo "...Updating pycones-2016: Building the docker image"
docker build -t pycones2016:1.0 -f Dockerfile .
echo "...Updating pycones-2016: Restart service"
docker-compose -f docker-compose.yml stop pycones2016
docker-compose -f docker-compose.yml rm -v -f pycones2016
docker-compose -f docker-compose.yml up -d --no-deps pycones2016
echo "Updating pycones-2016: done!"
