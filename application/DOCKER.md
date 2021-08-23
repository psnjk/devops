# Docker best practices
1. Use .dockerignore
2. Don't use ```Copy . .```
3. Use stages for builds, use proper stage names (Not implemented for my Dockerfile)
4. Use one container for one process (Don't run differrent apps in one container)
5. Less layers is better
6. Use Rootless containers
7. Use trusted base images
8. Expose ports
9. Use Linting
10. Locally scan images during development 
11. Run as non root
12. Include health / liveness checks (Not implemented for my Dockerfile)
