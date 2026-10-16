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
- Download/Clone the repository (if in Linux "git clone https://github.com/Krupac/portfolio_website") 

### Docker (linux)
- Make sure docker is installed (this is not a docker guide. Check out their [https://docs.docker.com/engine/install/](docs)). - Open folder
  - Edit the .env file for what port you want the website run on. Edit the "FASTAPI_PORT" value (default is 8001)
<img width="1105" height="135" alt="image" src="https://github.com/user-attachments/assets/c9f94908-0da2-4b80-ad19-374937d18eaa" />

-Run docker compose up -d (-d flag is for detached mode or running in background. To watch for any errors, run without flag) 
  - If it does not work, try running it with "sudo in front of it.
  - To turn off, run docker compose down (-v flag will delete all of the containers fully. Does not delete the repo folder) 
<img width="1458" height="240" alt="image" src="https://github.com/user-attachments/assets/31c2365b-c8d9-421e-b2ab-635f9f4e94f9" />
- Navigate to your browser and then to http://127.0.0.1:8001 (or change the port or the numbers after the colon)
- TADA you are now running the website. (I would question why you would want to run a website of me, but you do you ig).

### Python (Windows/Mac):
- Make sure python is installed (this is not a python guide. Check out their [https://www.python.org/downloads/](docs)). - Open folder
- Unzip the folder.
- Open `CMD` on windows (type CMD) or open terminal in Mac.
- Do the command `cd` (change directory also known as a folder`) and move to where the unzipped folder is.
- Make a virtual environment `python -m venv env`
  - You can replace python with `python3` if it doesn't work. You can also change the name of the environment by replacing `env`
- Now we must activate the virtual environment. Run: `<env_name>\Scripts\activate.bat` (Make sure you use \'s and not /)
  - `source .venv/bin/activate` for mac
- Run: pip install -r requirements.txt to install from the list in requirements.txt.
- cd into the `app` folder
- Run  `uvicorn main:app --reload --port 8001` (can also change the port)
- Navigate to your browser and then to http://127.0.0.1:8001 (or change the port or the numbers after the colon)
- TADA you are now running the website. (I would question why you would want to run a website of me, but you do you ig).
