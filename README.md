# Website Portfolio
A little portfolio website built to showcase projects I have created, what I have done in school, and advertise my small tech repair business. (WIP)
![Code Time](https://hackatime.hackclub.com/api/v1/badge/U0B7G9Z2X7C/Krupamc/portfolio_website)
---
<img width="2013" height="1217" alt="image" src="https://github.com/user-attachments/assets/809c98df-7e5d-4d62-bfa1-65b36f41e3c0" />

## What is it?
This is a small mostly static (for now) website built using FastAPI, HTML, CSS, JS, and Jinja2 Templates. It is hosted using docker (instructions below). 

## Pages:
### Home:
- About Me section with a description
- Coding Widgets
  - Daily: Shows the time coded today out of my goal (currently four hours) with a progress bar that fills up.
  - Weekly: Stats such as total, daiily average, and most used editor/language
  - All time: Total time, most coded language, and the current coding streak.
  - Hackatime Widget: Shows a graph of my coding time by languages.
- My resume
<img width="1247" height="912" alt="image" src="https://github.com/user-attachments/assets/47070df9-52af-465e-8706-08e5dc77b479" />

### MATES (My School):
#### MATES? 
- Logos
- Link to the MATES website
- Dropdowns with what classes I have taken.
#### GIS:
- Explaination of the class and where I have been with pictures of my classwork.
#### Field Experience:
- Explaination of all my field classes and what skills I learned.
- PDFs of some of my write-ups from class.
- Pictures of the fields.
### My Services & Homelab:
#### Services:
- List of what I do and some info.
- List to contact page.
- Pictures of some stuff I do
<img width="1560" height="1062" alt="image" src="https://github.com/user-attachments/assets/bd523436-2abc-4c85-9454-9f6fb04270eb" />
#### Homelab:
- What is a home lab?
- Dropdown with my server specs.
- List of all the services I host (links where applicable)
### Indepedent Research:
- My Mentoring experience
- Picture of my research project with all places I took it and awards I won. Links and github repos where applicable. (I have one for sophomore and junior year)
<img width="1473" height="1035" alt="image" src="https://github.com/user-attachments/assets/84c0cd75-99f9-453f-a6b1-719488c9f033" />

### Interests:
#### Band:
- My story about band and why I love it
- Pictures
#### Audio Video, Lighting, and Theater:
- What I do
- Dropdown of all shows I have lighted/been in.
- Picture
### Contact Page:
Has several buttons that take you to:
- My email
- Github account
- LinkedIn page
<img width="793" height="541" alt="image" src="https://github.com/user-attachments/assets/fca02a87-0b53-495e-b185-e1714d6dac7f" />


## PLANNED Pages
### School page:
With sub pages for my extracurricular involvement and leadership roles
### Page with my hackatime data?
### And more!

## Features:
- All buttons have a transition/transform state when hovered/clicked on.
  - Hamburger menu in mobile
  - Layered menus in html
- Github link footer 
- Being cool

## Installation:
- Download/Clone the repository (if in Linux "git clone https://github.com/Krupamc/portfolio_website") 

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
