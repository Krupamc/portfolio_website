# Website Portfolio
A little portfolio website built to showcase projects I have created, what I have done in school, and advertise my small tech repair business. (WIP)
---
<img width="2525" height="1050" alt="image" src="https://github.com/user-attachments/assets/d78e3839-458e-41cb-810d-5652ac056537" />

## What is it?
This is a small mostly static (for now) website built using FastAPI, HTML, CSS, JS, and Jinja2 Templates. It is hosted using docker (instructions below). 

## Pages:
### Home Page:
About Me section with a description (needs photos)
### Contact Page:
Has several buttons that take you to:
- My email
- Github account
- LinkedIn page
<img width="1797" height="1022" alt="image" src="https://github.com/user-attachments/assets/5dfad6c4-00fc-40b7-a71a-89d402300fb1" />

## PLANNED Pages
### School page:
With sub pages for my extracurricular involvement and leadership roles, my GIS skills, field and research experience
### Research:
Show my research projects and link to them.
### Interests page:
Have several sub pages with links to band, theatre, and all the other stuff I do.
### Page with my hackatime data?
### And more!

## Features:
- All buttons have a transition/transform state when hovered/clicked on.
  - Hamburger menu in mobile
  - Layered menus in html
- Github link footer 
- Being cool

## Installation:
- Clone the repository (if in Linux "git clone https://github.com/Krupac/portfolio_website")

### Docker (linux)
- Make sure docker is installed (this is not a docker guide. Check out their [https://docs.docker.com/engine/install/](docs)). - Open folder
  - Edit the .env file for what port you want the website run on. Edit the "FASTAPI_PORT" value (default is 8001)
<img width="911" height="127" alt="image" src="https://github.com/user-attachments/assets/e5182249-2934-4788-841-5930016ab62" />
-Run docker compose up -d (-d flag is for detached mode or running in background. To watch for any errors, run without flag) 
  - If it does not work, try running it with "sudo in front of it.
  - To turn off, run docker compose down (-v flag will delete all of the containers fully. Does not delete the repo folder) 
<img width="1041" height="256" alt="image" src="https://github.com/user-attachments/assets/33c9f5ca-7444-4a65-baeb-d5f9cb414443"/>
- Navigate to your browser and then to [http://127.0.0.1:8001]([http://127.0.0.1:80011) (or change the port or the numbers after the colon)
