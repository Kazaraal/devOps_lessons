# This is lesson 5 assignment

# 1.
# Clone Selenium Webdriver project

# git clone https://github.com/titusfortner/webdrivers.git
#########################################################################


# 2.
# Clone Appium project.

# git clone https://github.com/appium/appium.git
#########################################################################

# 3.
# Create a new Python project (any) and upload it to Github

## Create a new repository on the command line
# echo "print("Welcome")" > test.py
# git init
# git add test.py
# git commit -m "The first commit"
# git branch -M main
# git remote add origin https://github.com/Kazaraal/lesson5_folder.git 
# git push origin main

# Answer
# https://github.com/Kazaraal/lesson5_folder.git
#########################################################################

# 4.
# Create a branch in your project repository
# git branch <branch_name>

# Answer
# ken@kens:~/Desktop/DevOps_Online_Training/github/lesson5_folder$ git branch --list
#   alta
# * main
#   master
###########################################################################

# # 5.
# # Create a conflict between your Master and branch

# # Create and switch to new branch
# git checkout -b alta

# # Create a .txt file with text
# echo "First text" > test.txt

# # Add the file to the staging area
# git add test.txt

# # Commit the file
# git commit -m "The very first text"

# # Push the file to the alta branch
# git push --set-upstream origin alta


# # Switch back to the master branch
# git checkout master


# # Add text to the .txt file
# echo "First text\nSecond text" >> test.txt

# # Add the file to the staging area
# git add test.txt

# # Commit the file
# git commit -m "The first edit text"

# # Push the file to the master branch
# git push --set-upstream origin master

# # Merge the new alta branch into the master branch
# git merge alta

# ## Answer
# Error message
# Auto-merging test.txt
# CONFLICT (content): Merge conflict in test.txt
# Automatic merge failed; fix conflicts and then commit the result.

# Edit the test.txt
# Then 'git add test.txt'
# Then 'git commit -m "Resolved merge conflict between master and alta"'
# Then 'git push'
###############################################################################

# # 6.
# # Check out a specific commit using commit hash.
# git checkout bcbc0b5e2adbec6cba036c2fb2c59e8d87c0fc3c

# Answer
# Previous HEAD position was bcbc0b5 The first edit text
# HEAD is now at ceaf8c0 This is just a test!

# # Verify Detached Head status
# git status
########################################################################

# 7.
# Reset (hard) to a specific commit
# git reset --hard <commit>

# Answer 
# git reset --hard 5aef6d211e7315f08ee88053d52e69577c9d80ca
# HEAD is now at 5aef6d2 another test

