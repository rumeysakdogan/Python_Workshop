#!/bin/bash
sudo yum update -y
sudo yum install python3 -y
sudo pip3 install flask
sudo pip3 install flask-mysql
sudo yum install git -y
sudo wget https://raw.githubusercontent.com/rumeysakdogan/Python_Workshop/master/hands-on/flask-05-Handling-SQL-with-Flask-Web-Application/app-with-mysql.py
mkdir templates && cd templates
sudo wget https://raw.githubusercontent.com/rumeysakdogan/Python_Workshop/master/hands-on/flask-05-Handling-SQL-with-Flask-Web-Application/templates/emails.html
sudo wget https://raw.githubusercontent.com/rumeysakdogan/Python_Workshop/master/hands-on/flask-05-Handling-SQL-with-Flask-Web-Application/templates/add-email.html
cd ..
sudo python3 app-with-mysql.py