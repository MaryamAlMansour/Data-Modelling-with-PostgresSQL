# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay"
user_table_drop = "DROP TABLE IF EXISTS users_table"
song_table_drop = "DROP TABLE IF EXISTS song"
artist_table_drop = "DROP TABLE IF EXISTS artist"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES
songplay_table_create = (
    """
    CREATE TABLE IF NOT EXISTS songplay (
        songplay_id SERIAL PRIMARY KEY,
        timestamp TIMESTAMP NOT NULL,
        userId INT NOT NULL,
        level VARCHAR,
        song_id VARCHAR,
        artist_id VARCHAR,
        sessionId INT NOT NULL,
        location VARCHAR,
        userAgent VARCHAR)
    """
)

user_table_create = (
    """
    CREATE TABLE IF NOT EXISTS users_table (
        userId INT PRIMARY KEY,
        firstName VARCHAR NOT NULL,
        lastName VARCHAR NOT NULL,
        gender VARCHAR,
        level VARCHAR)
    """
)

song_table_create = (
    """
    CREATE TABLE IF NOT EXISTS song (
        song_id VARCHAR PRIMARY KEY,
        title VARCHAR NOT NULL,
        artist_id VARCHAR NOT NULL,
        year INT,
        duration NUMERIC)
    """
)

artist_table_create = (
    """
    CREATE TABLE IF NOT EXISTS artist (
        artist_id VARCHAR PRIMARY KEY,
        artist_name VARCHAR NOT NULL,
        artist_location VARCHAR,
        artist_latitude NUMERIC,
        artist_longitude NUMERIC)
    """
)

time_table_create = (
    """
    CREATE TABLE IF NOT EXISTS time (
        timestamp TIMESTAMP NOT NULL,
        ts_hour INT NOT NULL,
        ts_day INT NOT NULL,
        ts_weekofyear INT,
        ts_month INT NOT NULL,
        ts_year INT NOT NULL,
        ts_weekday VARCHAR)
    """
)


# INSERT RECORDS

songplay_table_insert = ("INSERT INTO songplay(timestamp, userId, level, song_id, artist_id,sessionId, location, userAgent) \
VALUES(%s, %s, %s, %s, %s,%s, %s, %s);"                       
)

user_table_insert = ("INSERT INTO users_table(userId, firstName, lastName, gender, level) \
VALUES(%s, %s, %s, %s, %s) ON CONFLICT (userId) DO NOTHING;"
)

song_table_insert = ("INSERT INTO song(song_id, title, artist_id, year, duration) \
VALUES(%s, %s, %s, %s, %s)ON CONFLICT (song_id) DO NOTHING;"
)

artist_table_insert = ("INSERT INTO artist(artist_id, artist_name, artist_location, artist_latitude, artist_longitude) \
VALUES(%s, %s, %s, %s, %s)ON CONFLICT (artist_id) DO NOTHING;"
)


time_table_insert = ("INSERT INTO time(timestamp, ts_hour, ts_day, ts_weekofyear, ts_month, ts_year, ts_weekday) \
VALUES(%s, %s, %s, %s, %s, %s, %s);"
)

# FIND SONGS

song_select = ("""
    SELECT si.song_id, ar.artist_id 
    FROM song si
    JOIN artist ar
    ON si.artist_id = ar.artist_id
    WHERE si.title = (%s) AND ar.artist_name = (%s) AND si.duration = (%s);
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]