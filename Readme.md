Python application CICD process:-

We have flask application hosted on a port, 5000.
DockerFile which is to contanerized the appliction, I have tried to use both K8s and AWS for deployment .
In k8s , I have used minikube , reason , easy to use and spin up time is less , I was not able to have my personal AWS account activated so had to choose this way.
jenkinsfile(declarative) is our build server, we hae the steps defined , which include:-
    cloning the code, checking for requuired files, mandatory variable that has to be passed in to the pipeline from Job
    resolving dependency from internal server(Ex- Proget), building code , running sonar coverage , publishing the package
    We can have log being push to kibana so to give all team access for the build and deployment log.

    We are also deploying the code in dev environment.

K8s Deployment - based on tag provided it will try to deploy it in either k8s or AWS using Ansible


Techstack used :-

Ansible - CM tool

K8s/ Minikube - Container Orchestrator

App Lang: Python

Server: Flask


`
I will try to answer everything on AWS perspective as most of my experience is on AWS

1. What would you do to ensure the application can handle heavy load?
  We can have service which can scale with minimum , max, and desired count, also we can have ASG in place
  for task based on metric, underline resource (EC2) will be part of ASG which can also scale based on resource
  utilization.
    
2. What tools/strategy would you use for logging?
    We can use cloudwatch agent to enable logging which can be viewed on the kibana, we can 
    also create data source in grafana to have the state visualize.
    
3. How you monitor the application to ensure constant uptime?
   Grafana, we can see how many containers are healthy , what are the utilization , status 
   of underline reaources.
   
4. What security concerns would need to be addressed?
    Instance security group, only LB should be allowed to talk to the service on the given port 
    range, load balancer security group open only to listen on specific port.
    Roles - Instance should have limited access.
    
5. What if the application needed a DB? How would you handle this?
    We can create a DB and then pass the connection string as an environment variable.
    
6. What would your automated testing approach be?
    Once container is deployed , checking the endpoint if it's active , Again Application load
    balancer do this for us.
    
    
7. Could you list the infrastructure tools that you would use?
    Packer, CloudFormation Templates, Ansible.
