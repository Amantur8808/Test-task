The task was "Make a Kubernetes deployment strategy which contains an Azure function in python (with source code) which puts a message to Azure Storage Queue every minute.
Then make another Azure function that should load a message from a queue and run aprepared container service to print "Hello World"."

First of all:
  i will create an Azure Function in Python using the Azure Functions Core Tools. 
  This function will be responsible for putting a message to the Azure Storage Queue every minute.
    - I will write suitable source code for this function. 
  Example of such code you can see in the first.py file.
  
Then:
  I will create a Kubernetes Deployment for this Azure Function, using a Kubernetes manifest file. 
    - I can use the official Microsoft image for Azure Functions in the Docker Hub.
  You can see an example in the deployment.yaml file. That deployment will create a pod that runs the Azure Function.
  
And the third step:
  I need to create another Azure Function in Python, which will be responsible for loading a message from the queue and running a container service to print "Hello World".
    - Example of such code you can see in the second.py file.
