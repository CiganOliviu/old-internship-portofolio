# CiganEnterprize

This webapp represents the concept of a business focused on digital solutions with lots of functionalities
and subsystems who are very well automated.

![Website main page](CiganEnterprize_documentation/picture_1.png)
 
## Backend

In the backend I have 9 databases each of them being strong related to a subsystem automated in the webapp.
I have also integrated the CRM plugin ( more details here -> https://github.com/CiganEnterprise/CRMPlugin ) for 
managing the clients and the projects the company is working at. Excluding the databases included by 
the CRM, there are 5 databases.
* BLOG which includes only one table: Posts
* MAINCOMPONENT which includes three tables: Employers, Projects, Studios.
* EVENTS which includes three tables: Host events, Past Events, Sponsor Events
* COMMUNICATION which includes two tables: Contact and Newsletter
* CAREERS which includes four tables: AvailableInternships, AvailableJobs, InternshipsAppliance, JobsAppliance 

A part of the databases can be seen below. 

![Website main page](CiganEnterprize_documentation/picture_2.png)

##### BLOG

The Posts table from the Blog Database includes all the articles which can be seen in the platform
at the company blog section. From this part of the administration system you can actualise, 
change or write articles very easy through a basic form.

##### Checking the articles from the blog system

![Website main page](CiganEnterprize_documentation/picture_3.png)

##### Adding a new article

![Website main page](CiganEnterprize_documentation/picture_4.png)

##### The way it looks in the UI

![Website main page](CiganEnterprize_documentation/picture_5.png)

Also for making the user job simpler I also implemented a search engine through the articles.

![Website main page](CiganEnterprize_documentation/picture_6.png)

This blog system was also implemented in ciganoliviudavid webapp which is my personal website 
( Details here -> https://github.com/CiganEnterprise/ciganoliviudavid).

##### CAREERS

In this database I practically store open jobs and internships in the company as well as appliances for 
those jobs. The administrator is able to add open jobs and check out the appliances for all open jobs
in the company. Because the use case of the webapp was about a company which had different locations in 
the country I had to create open jobs for specific locations. I also wanted to have the same open job 
in different locations. This was a little bit problematic at first sight but it was solvable just by
implementing some logic between the tables Studios and AvailableJobs, AvailableInternships. It's about
a foreignKey relationship.

The AvailableJobs and AvailableInternships tables are pretty much the same thing with just some fields
as difference.

##### This is how listed jobs look like in the administration panel

![Website main page](CiganEnterprize_documentation/picture_7.png)

##### This is how the form looks when adding a new open job

![Website main page](CiganEnterprize_documentation/picture_8.png)

##### This is how the UI with open jobs looks like

![Website main page](CiganEnterprize_documentation/picture_9.png)

##### As a user you can see more details about the job by clicking on it

The system will automatically create a page for every job that was added in the administration panel, 
in one way or another this system is similar with the one implemented in the blog.

![Website main page](CiganEnterprize_documentation/picture_10.png)

The InternshipAppliance table is pretty similar with the JobsAppliance, the differences are just
some special fields every table has but the system behind them is the same. The idea is that you can
apply for the job through a simple form in the webapp.

![Website main page](CiganEnterprize_documentation/picture_11.png)

After filling this form, all the information will be stored in the InternshipAppliance table where
the platform administrator will be able to check it.

##### This is how internship appliances look like in the administration panel

![Website main page](CiganEnterprize_documentation/picture_12.png)

##### Checking the appliance in detail

![Website main page](CiganEnterprize_documentation/picture_13.png)

##### COMMUNICATION

This database represents the direct contact to any user who visits the site. It contains 
two main tables. The Contact table contains messages who are send to the business by a visitor who wants
to offer some feedback, ask something about the business or pretty much say anything he wants.
The message is sent through a form in the UI, more precisely in the Contact section.

##### This is how the form looks like in the UI

![Website main page](CiganEnterprize_documentation/picture_14.png)

##### This is how the administrator sees the messages

![Website main page](CiganEnterprize_documentation/picture_15.png)

In the right side it can be seen the READ field, in the moment you click on a message and
you read it, you also have a check box below. If you check that check box the message
will appear as seen.

##### This is how the message looks when you open it

![Website main page](CiganEnterprize_documentation/picture_16.png)

The newsletter table works the same way, there is a form in the newsletter section 
which you fill and the data is stored in the table.

![Website main page](CiganEnterprize_documentation/picture_17.png)

##### EVENTS

The events database contains three main tables: Host Events, Past Events, Sponsor Events.
In the Host Events and Sponsor Events the administrator just adds the events where
the company is a host or a sponsor. These are active tables which means in the moment
the date of the host events or sponsored events has past, there are automatically moved
to past events table and deleted from host events or sponsor events.

##### This is how the events are in the UI

![Website main page](CiganEnterprize_documentation/picture_18.png)

Also you can click on any event for getting more details about it.

![Website main page](CiganEnterprize_documentation/picture_19.png)

##### MAINCOMPONENT

In the main component database I have three tables who are all independent: Employers,
Projects and Studios.

##### Studios

The Studios table is where the administrator adds the locations of the company. It includes
information like studio image, manager name, address, city and others. There is a section
in the webapp (Studios section) which adapts to how many locations you add in the database.

![Website main page](CiganEnterprize_documentation/picture_20.png)

Again, in the moment you click on a location you can see all the details about it. The
webapp will automatically create a page which contains all the details you added
in the database, in django that page is called a DetailView.

![Website main page](CiganEnterprize_documentation/picture_21.png)

##### Employers

This table includes all the employers who are working in the company. All of them
are added manually by the webapp administrator and are visible in the administration
page with specific information about them like years of experience, a profile image, 
the post where they are working etc.

![Website main page](CiganEnterprize_documentation/picture_22.png)

They are also listed in the UI, more precisely in the Team section of the webapp as 
it can be seen below.

![Website main page](CiganEnterprize_documentation/picture_23.png)

The team section as well as the blog section, studios, careers, internships and any other
who is based on queries from the database are adaptable at any number of instances
in the database with no exception.

##### Projects

This table works exactly like the Studios and Employers table. It stores all the projects
added by the administrator and eventually are posted in the Projects section of the webapp.

##### This is how the projects are listed in the database

![Website main page](CiganEnterprize_documentation/picture_24.png)

## Frontend

The webapp is 100% responsive and it includes basic animations realised with CSS3, Javascript and Jquery.

![Website main page](CiganEnterprize_documentation/picture_25.png) ![Website main page](CiganEnterprize_documentation/picture_26.png)


## Technologies

The technologies I've used for this project are HTML5, SASS, Bootstrap,
JavaScript, Jquery, Python Django, SQL Based Database (sqlite3).

## Future Development

A list with possible and helpful updates that the system may need:

* The time under the name of a city where the business has a studio is the server time, it updates
only when you reload the page. It would be nice an implementation which includes ajax so that the user
will not have to reload the page to see the current time.

* Because we talk about a lot of components which creates the system, a better UX for the page
may be a good idea.

## Requirements

* You should have python3 and django (version 3.0.8 or bigger) installed.

## Setup

* Download this repo
* After downloading this repo you have to get a SECRET_KEY from here -> https://djecrety.ir/ and paste
it in the settings.py file from cigan_enterprize folder. (cigan_enterprize/CiganEnterprize/settings.py)
 
![Website main page responsive](CiganEnterprize_documentation/picture_27.png)

* Open cmd or terminal in cigan_enterprize folder and type 
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