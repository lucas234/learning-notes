1. docker-compose  运行

   ```sh
   # Start the jenkins-local container
   docker-compose up -d
   
   # Get the initial admin password
   docker exec jenkins-local cat /var/jenkins_home/secrets/initialAdminPassword
   
   # Confirm the jenkins-local container is running
   docker ps
   
   # stop container 
   docker-compose down
   ```

2. 直接运行

   ```sh
   docker run --rm -d -p 8080:8080 -p 50000:50000 -v C:\work\jenkins:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock --name jenkinslocal  jenkins/jenkins
   ```

   