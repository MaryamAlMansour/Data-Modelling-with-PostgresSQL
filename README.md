# Sparkify Using Postgres

## What is Sparkify 
Sparkify is music streaming app who is trying to upscale their business by collecting user's songs and understand what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app. Therefore, I analyzed their data so I create a Postgres database with tables designed to optimize queries on song play analysis, by using a database schema and ETL pipeline for this analysis.

## Pre-requisets
This project touches on many aspects of pandas, postgres. So make sure you understand the integration between python and postgres, in addition to understanding the basic of pandas that will really ease your understanding of Sparkify.  

## Sparkify Schema Structure 
There are two datasets song and log datasets, you'll be able to create a star schema optimized for queries on song play analysis. This includes the following tables.

#### Fact Table
1. songplays - records in log data associated with song plays i.e. records with page NextSong
songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

#### Dimension Tables
1. users - users in the app: user_id, first_name, last_name, gender, level
2. songs - songs in music database: song_id, title, artist_id, year, duration
3. artists - artists in music database: artist_id, name, location, lattitude, longitude
4. time - timestamps of records in songplays broken down into specific units: start_time, hour, day, week, month, year, weekday


## Sparkify Files Objectives

* sql_queries.py
Write the accurate creation of tables in sql_queries, consider if there is an existance of previous DB(must be dropped before the creation). This will be using postgres syntax. To have a better of the data types you will use, take a peak on song_data from the provided directories. Running it will allow you to insert the created columns in the database. 

* create_tables.py
Now that you are done with the initial steps, try running the create_tables which will invoke all the tables you created in sql_queries, after dropping any existing columns that has been created or initialized in the database before. 

* etl.ipynb
In this file there is a step by step guides you throgh creation of ETL pipline, while it allows you to see it in action. We will be using pandas for creating a dataframe and manipulating it, using indexing and filtering the songs file. We will also use datetime functionality to convert epoch to timestamp dates. Following indxing for users. Finalizing it with creating the songplay table which will join two tables siong/ artist table using the artist_id in order to create a fact table which will get artist_id and song_id based on song, artist and duration. 

## Commands to Run Sparkify

**Note:** run <code> python creat_tables.py </code> before running <code> etl.ipynb </code> or <code> etl.py </code>

1. <code> python3 create_tables.py </code> : Create the sparkify database and connects to it by invoking <code> sql_queries.py </code>
2. <code> etl.ipynb </code> : Run Sparkify ETL Pipeline to outcast the most listened song between users. 
3. <code> Test.ipynb </code> : Run it everytime you want to ensure the insertion accuracy of your tables. 
