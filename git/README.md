## Add and push to master

git add .

git commit -m "initial commit"

git remote add origin https://github.com/wulfnb/quick_book.git

git push -u origin master


## Change file permission not affect git 
git config --global core.filemode false

## Store credintial for 1 hour
git config --global credential.helper 'cache --timeout 3600'