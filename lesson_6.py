# This is lesson 6 assignment

# 1. 
# Build Job that creates a text file containing your name on your
# desktop.

# Answer
# Started by user ken

# Running as SYSTEM
# Building in workspace /var/lib/jenkins/workspace/namer
# [namer] $ /bin/sh -xe /tmp/jenkins15049978904115374692.sh
# + echo Kenneth
# Finished: SUCCESS
######################################################################

# 2.
# Build job that will read your text file, and print its content.

# Answer
# Started by user ken
# Running as SYSTEM
# Building in workspace /var/lib/jenkins/workspace/reader
# [reader] $ /bin/sh -xe /tmp/jenkins4816894681327135825.sh
# + cat /var/lib/jenkins/workspace/namer/test.txt
# Kenneth
# Finished: SUCCESS
########################################################################

# 3.
# Build job that prints the free disk space.

# Answer
# Started by user ken
# Running as SYSTEM
# Building in workspace /var/lib/jenkins/workspace/freeDiskSpace
# [freeDiskSpace] $ /bin/sh -xe /tmp/jenkins14518774243669111304.sh
# + free
#                total        used        free      shared  buff/cache   available
# Mem:        16052416    11639228      954124     1069800     4959780     4413188
# Swap:        4194300      766208     3428092
# Finished: SUCCESS
#####################################################################################

# 4.
# Build job that moves your text file into another directory

# # Answer
# Started by user ken
# Running as SYSTEM
# Building in workspace /var/lib/jenkins/workspace/moveFile
# [moveFile] $ /bin/sh -xe /tmp/jenkins1152316757579830540.sh
# + mkdir first_folder second_folder
# + echo We are in a file in first folder
# + mv ./first_folder/test.txt ./second_folder/
# + ls first_folder
# + ls second_folder
# test.txt
# Finished: SUCCESS
######################################################################################

# 5.

# Create a job that runs once a day at 8:00

# 0 8 * * * /home/ken/task.sh

######################################################################################

# 6.
# Create a declarative Jenkins pipeline which will perform exercises
# 1-4 in 4 stages.

# pipeline {
#     agent any 

#     stages {
#         stage('Exercise 1') {
#             steps {
#                 script {
#                     echo 'Performing Exercise 1...'
#                     // Add your exercise 1 commands here
#                     sh 'echo "Exercise 1 completed."'
#                 }
#             }
#         }

#         stage('Exercise 2') {
#             steps {
#                 script {
#                     echo 'Performing Exercise 2...'
#                     // Add your exercise 2 commands here
#                     sh 'echo "Exercise 2 completed."'
#                 }
#             }
#         }

#         stage('Exercise 3') {
#             steps {
#                 script {
#                     echo 'Performing Exercise 3...'
#                     // Add your exercise 3 commands here
#                     sh 'echo "Exercise 3 completed."'
#                 }
#             }
#         }

#         stage('Exercise 4') {
#             steps {
#                 script {
#                     echo 'Performing Exercise 4...'
#                     // Add your exercise 4 commands here
#                     sh 'echo "Exercise 4 completed."'
#                 }
#             }
#         }
#     }

#     post {
#         always {
#             echo 'Pipeline execution finished.'
#         }
#     }
# }

#######################################################################################

# # 7.
# Started by user ken
# Obtained Jenkinsfile from git https://github.com/Kazaraal/jenkins_pipeline.git
# [Pipeline] Start of Pipeline (hide)
# [Pipeline] node
# Running on Jenkins in /var/lib/jenkins/workspace/pipeline_job
# [Pipeline] {
# [Pipeline] stage
# [Pipeline] { (Declarative: Checkout SCM)
# [Pipeline] checkout
# Selected Git installation does not exist. Using Default
# The recommended git tool is: NONE
# No credentials specified
# Cloning the remote Git repository
# Cloning repository https://github.com/Kazaraal/jenkins_pipeline.git
#  > git init /var/lib/jenkins/workspace/pipeline_job # timeout=10
# Fetching upstream changes from https://github.com/Kazaraal/jenkins_pipeline.git
#  > git --version # timeout=10
#  > git --version # 'git version 2.43.0'
#  > git fetch --tags --force --progress -- https://github.com/Kazaraal/jenkins_pipeline.git +refs/heads/*:refs/remotes/origin/* # timeout=10
#  > git config remote.origin.url https://github.com/Kazaraal/jenkins_pipeline.git # timeout=10
#  > git config --add remote.origin.fetch +refs/heads/*:refs/remotes/origin/* # timeout=10
# Avoid second fetch
#  > git rev-parse refs/remotes/origin/main^{commit} # timeout=10
# Checking out Revision f4eada9cd5380c4a9a74544f930f0bfcf533a38b (refs/remotes/origin/main)
#  > git config core.sparsecheckout # timeout=10
#  > git checkout -f f4eada9cd5380c4a9a74544f930f0bfcf533a38b # timeout=10
# Commit message: "Edited jenkinsfile to Jenkinsfile"
# First time build. Skipping changelog.
# [Pipeline] }
# [Pipeline] // stage
# [Pipeline] withEnv
# [Pipeline] {
# [Pipeline] stage
# [Pipeline] { (test)
# [Pipeline] sh
# + python3 --version
# Python 3.12.3
# [Pipeline] }
# [Pipeline] // stage
# [Pipeline] stage
# [Pipeline] { (hello)
# [Pipeline] sh
# + python3 first.py
# This is the for lesson 6.
# [Pipeline] }
# [Pipeline] // stage
# [Pipeline] }
# [Pipeline] // withEnv
# [Pipeline] }
# [Pipeline] // node
# [Pipeline] End of Pipeline
# Finished: SUCCESS

# # CHALLENGE
# Started by user ken
# Running as SYSTEM
# Building in workspace /var/lib/jenkins/workspace/job_1
# [job_1] $ /bin/sh -xe /tmp/jenkins17560289561959518681.sh
# + echo The first job
# The first job
# Triggering a new build of job_2
# Finished: SUCCESS