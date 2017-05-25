# drchrono Hackathon


### Setup
  - Setup a virtualenv
  - Go to virutalenv, downlaod this project
  - Install dependencies

### Key Components
- messenger app: query the api and send email
- celery + redis: periodically run the send_email() task
- bakcend.py: store token in the only messenger object

### How to Start

- Go to your virtualenv/src

- Do migrations

- Start Redis: 
```redis-server```

- Start Server: 
```python manage.py runserver```

- Start Celery: 
```celery -A drchrono worker -l info```

Because of rate limit, patient filtering logic are not correct, and the programm doesn't really send email to drchrono customoers. 


