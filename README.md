# Website Portfolio
A little portfolio website built to showcase projects I have created, what I have done in school, and advertise my small tech repair business. (WIP)
[Try it out!](https://krupamlab.com)
---
![Code Time](https://hackatime.hackclub.com/api/v1/badge/U0B7G9Z2X7C/Krupamc/portfolio_website)

<img width="1877" height="1210" alt="image" src="https://github.com/user-attachments/assets/9c568f1f-8268-4591-bf35-bc6042ca773d" />

## What is it?
This is a small "mostly" static (for now) website built using FastAPI, HTML, CSS, JS, and Jinja2 Templates. It is hosted using docker (instructions below). 

## Pages:
### Home:
- Immich Server Carousel (updates every days!)
- About Me section with a description
- Coding Widgets
  - Daily: Shows the time coded today out of my goal (currently four hours) with a progress bar that fills up.
  - Weekly: Stats such as total, daiily average, and most used editor/language
  - All time: Total time, most coded language, and the current coding streak.
  - Hackatime Widget: Shows a graph of my coding time by languages.
- Schedule Widget that checks my Google calendar if I am busy or not. Very cool!!!
- My resume
<img width="1116" height="800" alt="image" src="https://github.com/user-attachments/assets/667c976b-43ef-4009-8efc-9cc2074252a4" />
<img width="1085" height="1017" alt="image" src="https://github.com/user-attachments/assets/e5d3afca-08aa-446a-bcf1-9cf2faefda59" />

### MATES (My School):
#### MATES? 
- Logos
- Link to the MATES website
- Dropdowns with what classes I have taken.
#### GIS:
- Explaination of the class and where I have been with pictures of my classwork. Events I have been for GIS.
<img width="1065" height="1020" alt="image" src="https://github.com/user-attachments/assets/613f688a-fddb-4f75-a9cb-456b5535ffaa" />

#### Field Experience:
- Explaination of all my field classes and what skills I learned.
- PDFs of some of my write-ups from class.
- Pictures of the fields.
<img width="1173" height="790" alt="image" src="https://github.com/user-attachments/assets/ef8d8f05-0c7c-4452-b6dd-ef5dc6de7653" />

#### Extracurriculars:
- List of all the clubs I am in (with links to pages if they exist)
- Pictures of some activities
#### MATES Reflection:
- What I really thought of my times at MATES

### My Services & Homelab:
#### Services:
- List of what I do and some info.
- List to contact page.
- Pictures of some stuff I do.
<img width="1170" height="1025" alt="image" src="https://github.com/user-attachments/assets/b8ecd549-f3fe-4b97-a9ce-7d8058c03010" />

#### Homelab:
- What is a home lab?
- Dropdown with my server specs.
- List of all the services I host (links where applicable)

#### My specs and what I use:
- Page of my hardware and software.
- Pictures where applicable
- Dropdowns:
  - My PC Specs
  - Laptop
  - Peripherals
  - Software
<img width="1263" height="937" alt="image" src="https://github.com/user-attachments/assets/80da74a0-1987-4f1c-aac8-009c52416be8" />

#### Websites:
- How and why I run this website
- FAQs about my websites.
- Links to my other websites
<img width="976" height="1023" alt="image" src="https://github.com/user-attachments/assets/1192cbae-8506-4208-8703-01414c2090d0" />

### Experiences:

#### Work & Internships:
- My job experience
- My odd jobs/gigs
- Internship at Save Barnegat Bay, what I did, where I went for them.
- Internship at NJCCIC and what I did.
<img width="1027" height="830" alt="image" src="https://github.com/user-attachments/assets/ae4bc6da-9347-4034-9021-e2e220717cdb" />

#### Hack Club:
- What is Hack Club?
  - Link to their website
- Programs I have done:
  - Explains what they were, when, and what projects I did.
    - Images and links to the projects.
<img width="1000" height="990" alt="image" src="https://github.com/user-attachments/assets/40ae6d74-f41a-4e72-89e3-fcf486e02eb0" />

### Volunteer:
- Where I volenteer and the story behind them.
  - (Library, temple, school for examples)
- Pictures of what I do/the place.


### Indepedent Research:
- My Mentoring experience
- Picture of my research project with all places I took it and awards I won. Links and github repos where applicable. (I have one for sophomore and junior year)
<img width="1473" height="1035" alt="image" src="https://github.com/user-attachments/assets/84c0cd75-99f9-453f-a6b1-719488c9f033" />

### Interests:
#### Band:
- My story about band and why I love it
- Pictures
<img width="1075" height="961" alt="image" src="https://github.com/user-attachments/assets/b8ada086-a141-48f4-9c57-6c339a1bef3c" />

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

## Features:
- All buttons have a transition/transform state when hovered/clicked on.
  - Hamburger menu in mobile
  - Layered menus in html
- Github link footer 
- Being cool

## Installation:
- Download/Clone the repository (if in Linux "git clone https://github.com/Krupamc/portfolio_website") 
- Rename `example.env` to `.env` and fill out the variables.
  - Hackatime Token/ID/Username: Find @ hackatime.hackclub.com
  - Hackatime email: Your hackclub email
  - Google Calendar ID/Service account file: Create a google cloud project and a service account and setup the Google Calendar - API. Download the service account JSON file. Replace the text of `google-calendar.json` with the new file.
  - Immich Url: Url of your Immich instance.
  - Immich Api Key: Create a API key for your account with album.read, asset.view, asset.read rights.
  - Immich Album ID: Create a album for your website and fill it with photos you like. In the url, copy the ID (After `/albums/`).
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
