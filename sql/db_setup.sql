--the following query creates the music db
--CREATE DATABASE music_suggestion;

--drop each table if they exist
DROP TABLE IF EXISTS artist_suggestion;
DROP TABLE IF EXISTS album_suggestion;
DROP TABLE IF EXISTS song_suggestion;
DROP TABLE IF EXISTS song;
DROP TABLE IF EXISTS album;
DROP TABLE IF EXISTS artist;
DROP TABLE IF EXISTS suggestion;
DROP TABLE IF EXISTS suggester;


--the following query creates the suggester table
CREATE TABLE suggester (
  suggester_id SERIAL PRIMARY KEY,
  suggester_contact VARCHAR(255) NOT NULL,
  suggester_name VARCHAR(30) NOT NULL
);

--the following query creates the suggestion table
CREATE TABLE suggestion (
  suggestion_id SERIAL PRIMARY KEY,
  suggestion_rating INTEGER,
  suggestion_listened BOOLEAN NOT NULL DEFAULT FALSE,
  suggestion_type CHAR(2) NOT NULL, -- 'AL' for album, 'AR' for artist, or 'SO' for song
  suggestion_suggester_id INTEGER NOT NULL,
  suggestion_suggestee_id INTEGER NOT NULL,
  FOREIGN KEY (suggestion_suggester_id) REFERENCES suggester(suggester_id),
  FOREIGN KEY (suggestion_suggestee_id) REFERENCES suggester(suggester_id)
);

--the following query creates the artist table
CREATE TABLE artist (
  artist_id SERIAL PRIMARY KEY,
  artist_name VARCHAR(30) NOT NULL
);

--the following creates the album table
CREATE TABLE album(
    album_id SERIAL PRIMARY KEY,
    album_name VARCHAR(30) NOT NULL,
    album_artist_id INTEGER NOT NULL,
    FOREIGN KEY (album_artist_id) REFERENCES artist(artist_id)
);

--the following creates the song table
CREATE TABLE song(
    song_id SERIAL PRIMARY KEY,
    song_name VARCHAR(30) NOT NULL,
    song_album_id INTEGER NOT NULL,
    FOREIGN KEY (song_album_id) REFERENCES album(album_id)
);

--the following query creates the artist_suggestion table
CREATE TABLE artist_suggestion (
  suggestion_id INTEGER NOT NULL,
  artist_id INTEGER NOT NULL,
  FOREIGN KEY (suggestion_id) REFERENCES suggestion(suggestion_id),
  FOREIGN KEY (artist_id) REFERENCES artist(artist_id)
);

--the following query creates the Album_suggestion table
CREATE TABLE album_suggestion (
  suggestion_id INTEGER NOT NULL,
  album_id INTEGER NOT NULL,
  FOREIGN KEY (suggestion_id) REFERENCES suggestion(suggestion_id),
  FOREIGN KEY (album_id) REFERENCES album(album_id)
);

--the following query creates the Song_suggestion table
CREATE TABLE song_suggestion (
  suggestion_id INTEGER NOT NULL,
  song_id INTEGER NOT NULL,
  FOREIGN KEY (suggestion_id) REFERENCES suggestion(suggestion_id),
  FOREIGN KEY (song_id) REFERENCES song(song_id)
);



