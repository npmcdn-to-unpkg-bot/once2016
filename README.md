## Introduction
 
Refer to <once2016.com>.

## Deployment

```
sudo apt-get update -y 
sudo apt-get install -y python-dev python-pip git
sudo apt-get install -y libcurl4-openssl-dev

git clone https://github.com/tobegit3hub/once2016.git

cd ./once2016/

pip install -r requirements.txt

cd ./website/

python ./manage.py migrate

python manage.py createsuperuser

vim ./website/settings.py
# MEDIA_ROOT = '/root/once2016/website/home/static/user_photos/'
# MEDIA_URL = '/root/code/once2016/website/home/static/user_photos/'

# nohup python ./manage.py runserver 0.0.0.0:80 &
```
