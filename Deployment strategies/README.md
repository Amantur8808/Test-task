The question was "What is a blue/green deployment strategy for Kubernetes based on deployments, service,and ingress. Please describe how to switch versions."

A blue/green deployment strategy for Kubernetes is a way of deploying new versions of an application without interruption to users. 
It involves creating two identical environments, one called the "blue" environment, and the other called the "green" environment.
The blue environment is the current live version of the application and the green environment is the new version of the application.

To switch versions, we need to:
  - Create a new deployment of the new version of the application in the green environment.
  - Create a new service and ingress that points to the green deployment.
  - Test the new version of the application in the green environment.
  - Once the new version is verified, update the ingress to point to the green service. This effectively routes all new incoming traffic to the green environment.
  - Verify that the new version of the application is working correctly in the green environment with live traffic.
  - Once the new version of the application is stable and working, you can scale down or delete the blue environment.

And it's important to note that this approach requires a load balancer or ingress controller that supports routing based on the hostname or path. 
And also to have enough capacity in your k8s cluster to run both versions of the application.
