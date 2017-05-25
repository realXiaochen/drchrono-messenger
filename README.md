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

- Go to http://127.0.0.1:8000/, click the link on the page, it will redirect to http://127.0.0.1:8000/accounts/profile/, you can see in celery window that the app is sending email periodically



Because of rate limit, patient filtering logic are not correct, and the programm doesn't really send email to drchrono customoers. 


