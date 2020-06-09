fuser -k -TERM -n tcp 8080

git stash
git pull
python3 server.py