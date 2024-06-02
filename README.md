# Social Networking Application
Create an API for social networking application using Django Rest Framework with below functionalities.


## Prerequisites
- Dokcer , Docker Compose


## Installation

# 1. Clone the repository:
   bash:      
   git clone git@github.com:NIKHILP16/SocialNetworkingAppDocker.git  
   cd project-directory (SocialNetworkingAppDocker) 

# 2. Create Docker Conatiner:
   docker compose -f docker-compose.yml up -d --build

# 3. Run Following cmds:
   To migrate :
      docker compose -f docker-compose.dev.yml  exec web python3 manage.py migrate

   To collect static folder :
      docker compose -f docker-compose.dev.yml  exec web python3 manage.py collectstatic
