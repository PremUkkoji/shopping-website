# shopping-website
shopping website with integrated assistive chatbot which helps you find products and helps in you comparing them

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
What things you need to install the software and how to install them
if you are in virtual environment
```
python -m pip3 install -r requirements.txt
```
if not in virtual environment
```
pip3 install -r requirements.txt
```

## Insights
* This project is build on Django framework using Python3.6
* This project uses MongoDB database (you have to change DB credentials in ``` settings.py ``` file in ``` shopping_assistant ``` app)

## Running this project
After setting up the database credentials
You just have to run a command
```
python manage.py runserver
```

## Deployment
This project is deployed on heroku
```
https://shoppingsitechatbot.herokuapp.com
```