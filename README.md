## End to end Machine Learning project



## Azure CI/CD Deployment 

### Run from terminal:

docker build -t mlprojectregestryname.azurecr.io/mlprojectweb:latest .

docker login mlprojectregestryname.azurecr.io

docker push mlprojectregestryname.azurecr.io/mlprojectweb:latest