# WeddingInvitation

This project represents a wedding invitation app which contains a virtual
invitation as well as a confirmation system for the guests

![Website main page](wedding_documentation/picture_1.png)

## Backend

In the backend I have two main databases, the first one which is 
Authentication and authorization where an account for all guests will be
created manually by the wedding couple or an administrator. The MainView
database contains two tables, one which is called confirm_answers and another
one called guest_environment_details.

![Website main page](wedding_documentation/picture_2.png)

##### MAINVIEW

This database contains two tables, confirm_answers and guest_environment_details. This database
contains the whole mechanism of the app which is asking the guest after he's authenticated through a
form if he wants to come or not. That's a boolean question, it is only accept or refuse. That answer is
stored in a table where the couple or the app administrator can see through simple queries the people
who accepted, how many of them there are, the people who refused and others.
The table where this form information is stored is called confirm_answers. This table is automatically populated
after a guest is going to authenticate in the platform, the data from which is populated is stored in 
the user table from the authentication and authorization database where the app administrator is creating
an account for every guest. 

What the app administrator will see

![Website main page](wedding_documentation/picture_3.png)

How the form looks like for the guest who did not answered yet to the invitation

![Website main page](wedding_documentation/picture_4.png)

The default answer is no, so if you don't answer at all you will already have the negative answer
for the invitation.
In the moment the guest sends a positive answer to the invitation, the database will be automatically
updated and the interface will change.

What the app administrator will see

![Website main page](wedding_documentation/picture_5.png)

After the answer is sent, the guest_environment_details table comes in place. Here it's stored information
about where is the guest place, at what table and how the table looks like. This information is again
introduced manually by the administrator.

This is what the guest will see after a positive answer is sent.

![Website main page](wedding_documentation/picture_6.png)

## Frontend

In this page there are also images with the place where the wedding is organised, a map with the exact
position and others.

![Website main page](wedding_documentation/picture_7.png)

![Website main page](wedding_documentation/picture_8.png)

The project, like any other I've created, it's responsive, easy to access and use by almost any user.

![Website main page](wedding_documentation/picture_9.png) ![Website main page](wedding_documentation/picture_10.png)

## Technologies

For this project the technologies used are HTML5, CSS3, Bootstrap, 
Javascript, Jquery, Python Django, SQL based database (sqlite3).
 
## Future Development

A list with possible and helpful updates that the system may need:

* I would like as a guest to know with who I'm sitting with at the table so that should be implemented
as well. This requires eventually a new field of type many to many with all the guests from where 
the administrator can choose who is sitting at that specific table but this may get complicated if there are too many 
guests. A better solution may be to collect from the database all the guests who are sitting at a specific 
table and query them in the main page of every user who is sitting at that specific table.

## Requirements

* You should have python3 and django (version 3.0.8 or bigger) installed.

## Setup

* Download this repo
* After downloading this repo you have to get a SECRET_KEY from here -> https://djecrety.ir/ and paste
it in the settings.py file from WeddingInvitation folder. (wedding_invitation/WeddingInvitation/settings.py)
 
![Website main page responsive](wedding_documentation/picture_11.png)

* Open cmd or terminal in wedding_invitation folder and type 
```
    python3 manage.py makemigrations
```

then 

```
    python3 manage.py migrate
```

after that create an admin

```
    python3 manage.py createsuperuser
```

run the app

```
    python3 manage.py runserver
```
* Enjoy

