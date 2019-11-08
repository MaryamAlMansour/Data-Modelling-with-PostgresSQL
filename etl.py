import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *
import json 


def process_song_file(cur, filepath):
    # open song file
    if filepath:
        with open(filepath, 'r') as song_json:  
            df = json.load(song_json)
    df = pd.DataFrame.from_dict(df,orient='index').T
    
    # insert song record
    all_song_records = list()
    for index, song_field in df.iterrows():
        songs_rows = [song_field.song_id, song_field.title, song_field.artist_id,
                      song_field.year, song_field.duration]
        all_song_records.append(songs_rows)
    print(len(all_song_records))
    song_data = all_song_records[0]
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    all_artists_records = list()
    for index, artist_field in df.iterrows():
        artists_rows = [artist_field.artist_id, artist_field.artist_name, artist_field.artist_location,
                        artist_field.artist_latitude, artist_field.artist_longitude]
        all_artists_records.append(artists_rows)
    artist_data = all_artists_records[0]
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    # open log file
    if filepath:
        with open(filepath, 'r', encoding='utf-8') as log_json:
            df_log = [json.loads(line) for line in log_json]
            df_log = df_log[0]
    df_log = pd.DataFrame.from_dict(df_log,orient='index').T
    '''
    if filepath:
        with open(filepath, 'r', encoding='utf-8') as log_json:
            df_log = json.load(log_json)
    df_log = pd.DataFrame.from_dict(df_log,orient='index').T
    '''
    # filter by NextSong action
    df_log = df_log[df_log['page'] == 'NextSong']

    # convert timestamp column to datetime
    t = pd.to_datetime(df_log['ts'], unit='ms')
    
    # insert time data records
    time_data = [t, t.dt.hour, t.dt.day, t.dt.weekofyear, t.dt.month, t.dt.year, t.dt.weekday]
    column_labels = ['timestamp', 'ts_hour', 'ts_day', 'ts_weekofyear', 'ts_month', 'ts_year', 'ts_weekday']
    time_df = pd.DataFrame(dict(zip(column_labels, time_data)))

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df_log[['userId', 'firstName', 'lastName', 'gender', 'level']]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df_log.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            song_id, artist_id = results
        else:
            song_id, artist_id = None, None

        # insert songplay record
        songplay_data = (t[0], row.userId, row.level ,song_id, artist_id, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()