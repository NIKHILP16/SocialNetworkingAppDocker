# Social Networking Application
Create an API for social networking application using Django Rest Framework with below functionalities.


## Prerequisites
- Dokcer, Docker Compose


## Installation

# 1. Clone the repository:
   bash:      
   git clone git@github.com:NIKHILP16/SocialNetworkingAppDocker.git  
   cd project-directory (SocialNetworkingAppDocker) 

# 2. Create Docker Conatiner:
   docker compose -f docker-compose.yml up -d --build

# 3. Run Following cmds:
   To migrate :\
&emsp;&emsp;docker compose -f docker-compose.yml  exec web python3 manage.py migrate

   To collect static folder :\
&emsp;&emsp;docker compose -f docker-compose.yml  exec web python3 manage.py collectstatic

# 4. Access API endpoints:


## User API Endpoints:

● Create User:  
&emsp;- POST http://127.0.0.1:1337/api/account/register   
&emsp;&emsp;eg. { "email":"x@y.xyz","password":"Passport1" ,"name":"XYZ" } 

● Login User to genrate token:   
&emsp;- POST http://127.0.0.1:1337/api/account/login      
&emsp;&emsp;eg. { "email":x@y.xyz","password":"Passport1" } 

● User Logout:   
&emsp;- POST http://127.0.0.1:1337/api/account/logout

● Change Password for User:    
&emsp;- POST http://127.0.0.1:1337/api/account/change-password     
&emsp;&emsp;eg. {"current_password": "string","new_password": "string"}

● Refresh token for User:  
&emsp;- POST http://127.0.0.1:1337/api/account/token-refresh'      
&emsp;&emsp;eg. {"refresh": "string"}




## Profile API Endpoints:

● View Profile:  
&emsp;- POST http://127.0.0.1:1337/api/user_profile/profile/&lt;uuid:profile_id&gt;

● Find Friends (List All):  
&emsp;- POST http://127.0.0.1:1337/api/user_profile/find_friends?search=xyz 

● Search Friend (exact search by email or contains by name):  
&emsp;- POST http://127.0.0.1:1337/api/user_profile/find_friends?search=xyz 

● Send Friend Request (Throttle Limit 3/min):   
&emsp;- POST http://127.0.0.1:1337/api/user_profile/send_request/&lt;uuid:profile_id&gt;

● Accept Frined Request:   
&emsp;- POST http://127.0.0.1:1337/api/user_profile/accept_request/&lt;uuid:friend_request_id&gt;

● Reject Frined Request:   
&emsp;- POST http://127.0.0.1:1337/api/user_profile/reject_request/&lt;uuid:friend_request_id&gt;

● Pending Frined Request:   
&emsp;- POST http://127.0.0.1:1337/api/user_profile/pending_request

● Frineds List:   
&emsp;- POST http://127.0.0.1:1337/api/user_profile/friend_list




# 4. PostMan Collection:
● Global Variables:\   
&emsp;- Postman/workspace_postman_globals.json

● Collection:\   
&emsp;- Postman/SocialNetworkingApp_api_postman_collection.json

