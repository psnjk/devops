## Kubernetes with minikube

1. Tutorials have been read
2. ```kubectl``` and minikube ```installed``` with ```chocolatey```
3. Application deployed (Screenshots are below)
   1. ```kubectl create deployment app-node --image=psnjk/devops:latest```
   2. ```kubectl get pods``` - to check it
4. Service is created and the app is accesible. (Screenshots are below)
   1. ```kubectl expose deployment app-node --type=LoadBalancer --port=5000```
   2. ```minikube service app-node```
5. Folder created and this is a readme with screenshots
   1. ![deploy](dep_pod_svc.png)
6. Cleaned up
   1. ![clean](deleted.png)