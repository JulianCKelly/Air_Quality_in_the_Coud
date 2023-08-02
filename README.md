## Air_Quality_in_the_Coud
Air Quality in the Cloud is a Flask-powered web app displaying real-time air quality data from the Open AQ API with filtering capabilities.

# Introduction
During the sprint challenge, I built a Flask-powered web application that displayed data about air quality. I used various tools, including Flask, Flask-SQLAlchemy, and Requests, to create the application and interact with the Open AQ API to retrieve air quality measurements.

# Part 1 - If I could put Flask in a File
I set up the basic structure of the Flask web application by creating a new file called aq_dashboard.py. I defined a root route that returned a placeholder message.

# Part 2 - Breathe Easy with OpenAQ
To fetch air quality data, I utilized the provided openaq.py file, which allowed me to communicate with the Open AQ API. I successfully pulled data from the API and integrated it into the application.

# Part 3 - That Data Belongs In A Model!
I used Flask-SQLAlchemy to create a Record model to store air quality data in a local database. I defined the necessary table columns and implemented the __repr__ method to display the data in a user-friendly manner.

# Part 4 - Dashboard to the Finish
In the final part, I modified the main route to query the database for "potentially risky" PM 2.5 data. I filtered the results and displayed them in the web application's dashboard.

The Air Quality in the Cloud web application was fully functional, offering real-time air quality data and historical records to users.
