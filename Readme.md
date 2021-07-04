Techstack used :-

Ansible - CM tool

K8s/ Minikube - Container Orchestrator

App Lang: Python

Server: Flask`

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
