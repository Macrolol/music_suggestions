--the following query creates the music db
--CREATE DATABASE music_suggestion;

-- enable pgcrypto extension
CREATE EXTENSION IF NOT EXISTS pgcrypto;


--drop each table if they exist
DROP VIEW IF EXISTS song_album_artist_id_names;
DROP TABLE IF EXISTS artist_suggestion;
DROP TABLE IF EXISTS album_suggestion;
DROP TABLE IF EXISTS song_suggestion;
DROP TABLE IF EXISTS song;
DROP TABLE IF EXISTS album;
DROP TABLE IF EXISTS artist;
DROP TABLE IF EXISTS suggestion;
DROP TABLE IF EXISTS prefferences;
DROP TABLE IF EXISTS suggester;


--the following query creates the suggester table
CREATE TABLE suggester (
  suggester_id SERIAL PRIMARY KEY,
  suggester_email VARCHAR(100) UNIQUE NOT NULL,
  suggester_username VARCHAR(50) NOT NULL,
  suggester_password TEXT NOT NULL, -- was considering using a fixed length CHAR(X) here as they're all going to be the same length but according to Postgres docs, it's doesn't matter
  suggester_created_date TIMESTAMP NOT NULL DEFAULT NOW()
);

-- the following query creates the prefferences table
CREATE TABLE prefferences (
  prefference_suggester_id INT PRIMARY KEY,
  prefference_wants_feedback BOOLEAN NOT NULL,
  prefference_wants_suggestions BOOLEAN NOT NULL,
  FOREIGN KEY (prefference_suggester_id) REFERENCES suggester(suggester_id)
);


--the following query creates the suggestion table
CREATE TABLE suggestion (
  suggestion_id SERIAL PRIMARY KEY,
  suggestion_rating INTEGER CHECK (suggestion_rating BETWEEN 1 AND 10), --1-10
  suggestion_listened BOOLEAN NOT NULL DEFAULT FALSE,
  suggestion_type CHAR(2) NOT NULL CHECK (suggestion_type IN ('AL', 'AR', 'SO')), -- 'AL' for album, 'AR' for artist, or 'SO' for song
  suggestion_date TIMESTAMP NOT NULL DEFAULT NOW(),
  suggestion_suggester_id INTEGER NOT NULL,
  suggestion_suggestee_id INTEGER NOT NULL,
  FOREIGN KEY (suggestion_suggester_id) REFERENCES suggester(suggester_id),
  FOREIGN KEY (suggestion_suggestee_id) REFERENCES suggester(suggester_id)
);

--the following query creates the artist table
CREATE TABLE artist (
  artist_id SERIAL PRIMARY KEY,
  artist_name VARCHAR(100) NOT NULL UNIQUE
);

--the following query creates the album table
CREATE TABLE album(
    album_id SERIAL PRIMARY KEY,
    album_name VARCHAR(100) NOT NULL,
    album_artist_id INTEGER NOT NULL,
    UNIQUE (album_name, album_artist_id),
    FOREIGN KEY (album_artist_id) REFERENCES artist(artist_id) ON DELETE CASCADE
);

--the following creates the song table
CREATE TABLE song(
    song_id SERIAL PRIMARY KEY,
    song_name VARCHAR(100) NOT NULL,
    song_album_id INTEGER,
    song_artist_id INTEGER,
    UNIQUE (song_name, song_album_id),
    UNIQUE (song_name, song_artist_id),
    FOREIGN KEY (song_album_id) REFERENCES album(album_id) ON DELETE CASCADE,
    FOREIGN KEY (song_artist_id) REFERENCES artist(artist_id) ON DELETE CASCADE,
    CHECK((song_album_id IS NULL) != (song_artist_id IS NULL)) --must have either an album_id or an artist_id but not both because the album will have the artist_id
);

--the following query creates the artist_suggestion table
CREATE TABLE artist_suggestion (
  suggestion_id INTEGER NOT NULL,
  artist_id INTEGER NOT NULL,
  FOREIGN KEY (suggestion_id) REFERENCES suggestion(suggestion_id) ON DELETE CASCADE,
  FOREIGN KEY (artist_id) REFERENCES artist(artist_id) ON DELETE CASCADE
);

--the following query creates the Album_suggestion table
CREATE TABLE album_suggestion (
  suggestion_id INTEGER NOT NULL,
  album_id INTEGER NOT NULL,
  FOREIGN KEY (suggestion_id) REFERENCES suggestion(suggestion_id) ON DELETE CASCADE,
  FOREIGN KEY (album_id) REFERENCES album(album_id) ON DELETE CASCADE
);

--the following query creates the Song_suggestion table
CREATE TABLE song_suggestion (
  suggestion_id INTEGER NOT NULL,
  song_id INTEGER NOT NULL,
  FOREIGN KEY (suggestion_id) REFERENCES suggestion(suggestion_id) ON DELETE CASCADE,
  FOREIGN KEY (song_id) REFERENCES song(song_id) ON DELETE CASCADE
);

-- this view has all song_id(s), song_name(s), album_name(s), artist_name(s)
-- as one table
CREATE OR REPLACE VIEW song_album_artist_id_names AS
SELECT song_id, song_name, album_id, album_name, COALESCE(artist_of_album.artist_id, artist_of_song.artist_id) as artist_id , COALESCE(artist_of_album.artist_name, artist_of_song.artist_name) AS artist_name FROM song
LEFT JOIN album ON song.song_album_id = album.album_id
LEFT JOIN artist artist_of_album ON artist_of_album.artist_id = album.album_artist_id
LEFT JOIN artist artist_of_song ON artist_of_song.artist_id = song.song_artist_id;



GRANT ALL ON ALL TABLES IN SCHEMA public TO music_db_user;
GRANT USAGE ON ALL SEQUENCES IN SCHEMA public TO music_db_user;
