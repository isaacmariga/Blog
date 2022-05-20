# export SECRET_KEY='12345'

export MAIL_USERNAME='aizakmariga@gmail.com'
export MAIL_PASSWORD='@temporarypassword123'

heroku config:set SECRET_KEY='12345'
heroku config:set MAIL_PASSWORD='@temporarypassword123'
heroku config:set MAIL_USERNAME='aizakmariga@gmail.com'

python3.10 manage.py server