March 6th, 2019
Maryam Al Mansour 


Sparkify Using Postgres

This Assigment projects the creation of ETL pipline using a schema for analysing two data sets and optimizing queries to build a completed artifact that sums different technologies in one python program. 


Abstract...
Using the song and log datasets, you'll be able to create a star schema optimized for queries on song play analysis. This includes the following tables.

*Fact Table..
1. songplays - records in log data associated with song plays i.e. records with page NextSong
songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

*Dimension Tables..
1. users - users in the app: user_id, first_name, last_name, gender, level
2. songs - songs in music database: song_id, title, artist_id, year, duration
3. artists - artists in music database: artist_id, name, location, lattitude, longitude
4. time - timestamps of records in songplays broken down into specific units: start_time, hour, day, week, month, year, weekday

As you can see the project is divided into different files. .ipynb, and .py. Each file is respnsible for a particular task. 

Intiating the project...

sql_queries.py
1. Write the accurate creation of tables in sql_queries, consider if there is an existance of previous DB(must be dropped before the creation). This will be using postgres syntax. To have a better isea of the data types you will use, take a peak on song_data from the provided directories. 
2. Insert the created columns in the database. 

create_tables.py
Now that you are done with the initial steps, try running the create_tables which will invoke all the tables you created in sql_queries, after dropping any existing columns that has been created or initialized in the database before. 

create_tables will be execusted using <code> python create_tables.py </code> this will create the sparkify database and connects to it. 


Main project work..
etl.ipynb
In this file there is a step by step guides you throgh creation of ETL pipline, while it allows you to see it in action. We will be using pandas for creating a dataframe and manipulating it, using indexing and filtering the songs file. We will also use datetime functionality to convert epoch to timestamp dates. Following indxing for users. Finalizing it with creating the songplay table which will join two tables siong/ artist table using the artist_id in order to create a fact table which will get artist_id and song_id based on song, artist and duration. 

This project touching many aspects on pandas, postgres. So make sure to understand the integration between python and postgres, in addition to understanding the basic of pandas will really ease the flow of this project. 

Remmber to run pythin creat_tables everytime you want to run etl.ipynb or etl.py. 

Use Test.ipynb everytime you want to ensure the insertion accuracy of your tables. 