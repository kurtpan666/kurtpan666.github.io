#! /bin/zsh

git add .
git commit -m "`date +\"%Y-%m-%d\"`"
git push
ghp-import -n -p -f _build/html