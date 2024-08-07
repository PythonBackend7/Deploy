# Deploy
BlogSite deploy with nginx

1. ssh root@server IP address
2. password: 
3.cd /var/www/
4. git clone reposetory url
5. cd project_name
6. virtualenv venv
7. source venv/bin/activate
8. ./manage.py makemigrations
9. ./manage.py migrate
10. ./manage.py createsuperuser
11. nano /etc/systemd/system/test.service
12. [Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=root
Group=www-data
WorkingDirectory=/root/cloudproject
ExecStart=/root/cloudproject/cloudenv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/root/myproject/myproject.sock myproject.wsgi:application

[Install]
WantedBy=multi-user.target
12. systemctl daemon-reload
13. systemctl start test.service
14.systemctl enable test.service
15. systemctl status test.service
16. nano /etc/nginx/conf_d/test.conf
17. server {
listen 80;
server_name ;

location = /favicon.ico { access_log off; log_not_found off; }
location /static/ {
root /root/cloudproject;
}

location / {
include proxy_params;
proxy_pass http://unix:/root/cloudproject/cloudproject.sock;
}
}
18. systemctl restart nginx.service
19. systemctl status nginx.service
20. sudo nginx -t