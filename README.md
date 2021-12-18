# BenfordLaw

**Django app installation:**

python -m venv venv
source venv/bin activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


**Docker installation:**

docker build -t benford_law:1 .
docker-compose up
