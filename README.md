## How to run Django on your local machine

1. `git clone https://github.com/imzisy/python-app.git`
2. Make sure you have pip installed if not follow step 3
3. sudo apt -install python (Linux) or sudo easy_install pip

4. install `sudo apt install virtualenv` (Linux) or `pip install virtualenv` so that you can activate the environment later on
4. run `virtualenv env`
5. run `source env/bin/activate`
6. run `pip install -r requirements.txt`
6. run `pip install -r requirements.txt`
7. run `python manage.py migrate`
8. run `python manage.py createsuperuser`
9. Enjoy :)

## How to add new hotel price ?

| You need to access the following url : http://127.0.0.1:8000/admin/hotels/hotel/add/

## How to get RESTFUL api documentation ?

| You need to access http://127.0.0.1:8000/

