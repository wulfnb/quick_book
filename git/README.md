## Add and push to master

git add .

git commit -m "initial commit"

git remote add origin https://github.com/wulfnb/quick_book.git

git push -u origin master


## Changes in file permission not affect git 
git config --global core.filemode false

## Store credintial for 1 hour
git config --global credential.helper 'cache --timeout 3600'

## Setup name and email
git config --global user.name "Name"

git config --global user.email "Email"


[link to Google!](http://google.com)

![GitHub Logo](/images/logo.png)
Format: ![Alt Text](url)

~~The Striked Text~~


[link text](#abcd)


First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column

- [x] Finish my changes
- [ ] Push my commits to GitHub
- [ ] Open a pull request


@mention


1. First list item
    - First nested list item
        - Second nested list item
    - First nested list item
    


> Pardon my French


<a name="abcd">Hi all</a> 


[Contribution guidelines for this project](docs/CONTRIBUTING.md)