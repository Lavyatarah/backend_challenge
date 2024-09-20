Backend Challenge
Description
This is a Django-based web application designed to manage customer and order information through a RESTful API. The project utilizes Django REST Framework for building the API and includes authentication via OAuth2.

Technologies Used
Django 5.1.1
Django REST Framework
PostgreSQL
dotenv
Whitenoise
OAuth2 Provider
Installation
Clone the repository:
git clone <repository-url>
cd backendchallenge
Create a virtual environment:
python -m venv venv
source venv/bin/activate
Install the requirements:
pip install -r requirements.txt
Set up the environment variables: Create a .env file in the project root and add the following:
Set up the database: Make sure you have PostgreSQL installedand create the database as specified in setting.py
python manage.py migrate
Run the development server:
python manage.py runserver
Usage
Navigate to http://localhost:8000/ in your web browser to access the application.
Use the /api/customers/ and /api/orders/ endpoints to interact with the API.
License
This project is licensed under the MIT License. See the LICENSE file for details.
Contributing
LAVENIA ATARAH
