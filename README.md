
### Recommended Start
```bash

$ cd path/to/your/dev/folder
$ mkdir django-channels-chat
$ cd django-channels-chat
$ git clone https://github.com/mwikya/django-channels-chat.git .
$ git reset --hard
$ git remote remove origin
$ virtualenv -p python3 .
$ source bin/activate
(django-channels-chat) $ pip install -r requirements.txt
(django-channels-chat) $ cd src
(django-channels-chat) $ python manage.py migrate
(django-channels-chat) $ python manage.py createsuperuser
... do the creation
(django-channels-chat) $ python manage.py createsuperuser
... create second super user 
```


### Install Redis
1. Download Redis

        ```
        bash          
        sudo apt-get update
        sudo apt-get upgrade
        sudo apt-get install redis-server
        sudo systemctl enable redis-server.service
        ```


    - Direct [Download](http://redis.io/download)

2. Open & Test Redis:
    - open Terminal

    - **redis-cli ping**
        ```
        $ redis-cli ping
        PONG
        ```

        **Close Redis** with `control` + `c` to quit