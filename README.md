VENDOR-MANAGEMENT-SYSTEM

Follow these instructions to set up and run the Django project locally:

Windows Setup

- download python

1. clone the project to local system
git clone https://github.com/Amin7473/vendor-ms.git

2. pull from DEV branch
git pull origin DEV

3. go into project directory

4. Create virtual environment and install requirements
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

5. migrations
python manage.py makemigrations
python manage.py migrate

6. import the json file , Vendor MS.postman_collection.json into postman.
all apis are available along with success responses as documentation.

Feel free to reach out to amin07473@gmail.com concerning any queries you may face.

Thank You.