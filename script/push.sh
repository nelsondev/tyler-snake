#!/bin/bash

echo "Please enter commit message:"
read -p '> ' MESSAGE

git add *
git add .
git commit -m "$MESSAGE"
git push