# Django Rest Api for Cbc69 website

This API contains the following CRUD features for :
- users
- tournaments
- posts
- volunteering events
- interclub teams

This API is a lot based on the work and course of London App Developer and other django rest api tutorials.

## Requirements

In order to make this API work, you may need the following requirements : 

- virtualbox
- vagrant
- python3

## Running

In order to run this API, you may want to use the following commands inside a git bash or your ubuntu local terminal : 

- Step in the directory
`cd cbc69_rest_api`
- Run vagrant Ubuntu server with the VagrantFile
`vagrant up`
- Connect to vagrant server
`vagrant ssh`
- Create new virtual environment 
`virtualenv cbc69_rest_api -p python3`
- Activate the virtual environment
`source cbc69_rest_api/bin/activate`
- Install the requirements 
`pip install -r requirements.txt`
- Step in the app folder
`cd src/cbc69_project`
- Run the server
`python manage.py runserver 0.0.0.0:8080`

Then finally connect to a web interface and go to : `https://localhost:8080`
