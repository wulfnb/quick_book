Multiple SSH Keys settings for different github account
create different public key

create different ssh key according the article Mac Set-Up Git

$ ssh-keygen -t rsa -C "your_email@youremail.com"

for example, 2 keys created at:
```
~/.ssh/id_rsa_company
~/.ssh/id_rsa_personal
```
then, add these two keys as following

> $ ssh-add ~/.ssh/id_rsa_company
> $ ssh-add ~/.ssh/id_rsa_personal

you can delete all cached keys before

> $ ssh-add -D

finally, you can check your saved keys

> $ ssh-add -l

Modify the ssh config
```
$ cd ~/.ssh/
$ touch config
$ subl -a config
```
Then added
```
#company account
Host github.com-company
	HostName github.com
	User git
	IdentityFile ~/.ssh/id_rsa_company

#personal account
Host github.com-personal
	HostName github.com
	User git
	IdentityFile ~/.ssh/id_rsa_personal
```

Clone you repo and modify your Git config

clone your repo git clone git@github.com:company/gfs.git gfs_personal

cd gfs_personal and modify git config

```
$ git config user.name "personal"
$ git config user.email "personal@gmail.com" 

$ git config user.name "company"
$ git config user.email "name@company-mail.com" 
```
or you can have global git config $ git config --global user.name "personal" $ git config --global user.email "personal@gmail.com"

then use normal flow to push your code
```
$ git add .
$ git commit -m "your comments"
$ git push
```
