# Git Operations Sequence

```bash
# initialise git
git init

# create 3 code files a.py b.py and c.py
echo "print('a')" > a.py
echo "print('b')" > b.py
echo "print('c')" > c.py

# check git status
git status

# add code to staging area
git add a.py
git add b.py

# commit the code as per the staging area
git commit -m "adding a,b"

# check git status
git status

# add code to staging area
git add c.py

# check git status
git status

# commit the code as per the staging area
git commit -m "adding c"

# check git status
git status

# track git logs
git log
git log --oneline

# connect it with remote 
git remote add origin [https://github.com/ashishjangra27/test](https://github.com/ashishjangra27/test)

# git push
git push -u origin main

# pull original code from github
git pull origin main

# create branch
git branch abcd

# switch to any branch
git checkout abcd
git switch abcd

# create and switch to a branch
git checkout -b abcd

# create new files
echo "print('branch')" > branch.py
echo "print('bran')" > bran.py  

# add new files to staging environment
git add .

# push the code directly on main
git push origin abcd:main

# merge the code of branch abcd with main
git merge main

# push final code
git push

# check available branches
git branch

# delete branch
git branch -d capitals
