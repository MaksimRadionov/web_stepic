sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/mysite
sudo ln -s /home/box/web/gunicorn.conf  /etc/gunicorn.d/myconf
sudo /etc/init.d/nginx restart
