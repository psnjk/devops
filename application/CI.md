# CI Best practices

## GitHub Actions
1. Keep Actions as small as possible
2. Use GitHub secrets, do not hardcode it
3. Use dependancies with caution
4. Do not run certain actions if previous were failed
5. Handle more actions, not just push (Not implemented for this project)

## Jenkins
1. Do not use it if it is not needed!
2. Backup home directory
3. Build scalable pipeline
4. Maintain higher test code coverage 
5. Run unit tests as part of a pipeline
6. Better to run jenkins on cloud and set up a web hooks for the repository, than to always run it on your machine
7. Avoid calls to Jenkins.getInstance
8. Avoid scheduling all jobs to start at the same time
9. Use shared libraries
10. Don't use input within an agent
