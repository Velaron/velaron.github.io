pelican content -s publishconf.py
invoke gh-pages
git add --all
git commit -m "update"
git push