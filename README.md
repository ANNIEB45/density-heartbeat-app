# Density Heartbeat Assignemnt by Annie Bellefleur

### Goal is to build a web application that displays the latest "heartbeat" from a number of sensors. 

## PROCESS:

* 1.Began by installing Django
 (_had trouble w/python, had to reinstall python3, pip, pipenv_)
* 2.Installed all dependencies
* 3.Created project and app folder
* 4.Installed Postgres for database
* 5.Added database setting and depencies to settings
* 6.created models- sensor and heartbeat
(_heartbeat is child of sensor, has foreign keys_)
* 7.created migrations
* 8.registered models to admin
* 9.Created superuser for admin
* 10.ran python server (_works_)
* 11.Checked admin route, logged in (_works_)
* 12.Started configuring URL for density_heartbeat_app and index(main page)
* 14.Created Serializer(_added feed data to show all sensors on main page_),Views, Routes
* 15.configured url for routes
* 16.ran into bug-could not import views 
* 17.added views file in project folder- fixed bug
* 18.navigated to api/v1 url- (_works_)
* 19.added fake data
## BACKEND WORKS

* 20.installed react client folder
* 21.configured app.js, created component folder and home.jsx file
* 22.imported home to app.js, added home component
* 23.npm start(_works_)
* 24.installed axios to call data from backend
* 25.added state, componentdidmount, 
* 26.rendered feed data to page(_not working_)
* 27.bug-404 error and network error(_took a while to get solution_)
* 28.solution: added proxy for localhost:8000 to package.json(_this is the url for the feed api_)
* 29.data is now rendering on page(_and the crowd goes wild_)
## FRONT END WORKS

#### _biggest focus was on backend, ran into the most bugs_