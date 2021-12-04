
/*
-- this query selects all suggesters and whether they want suggestions or not
SELECT sug.suggester_name as name, pref.prefference_wants_suggestions as wants_suggestions
FROM suggester sug
INNER JOIN prefferences pref
ON sug.suggester_id = pref.prefference_suggester_id;

-- this query selects all suggesters and their prefferences
SELECT sug.suggester_name as name, pref.prefference_wants_suggestions as wants_suggestions, pref.prefference_wants_feedback as wants_feedback
FROM suggester sug
INNER JOIN prefferences pref
ON sug.suggester_id = pref.prefference_suggester_id;
*/

--this querey selects the name and contact_info for only suggesters that want suggestions
SELECT sug.suggester_name as name, sug.suggester_contact as contact_info
FROM suggester sug
INNER JOIN prefferences pref
ON pref.prefference_suggester_id = sug.suggester_id
WHERE pref.prefference_wants_suggestions = 't'
LIMIT 10;




-- Query to select all song's names, the album the song is on, and the artist the song is by
SELECT song_name, album_name, artist_name FROM song
INNER JOIN album ON album.album_id = song.song_album_id
INNER JOIN artist ON artist.artist_id = album.album_artist_id;


-- Query to insert a song suggestion given the suggester's id, the sugestee's id, the song's name, album and who it is by
WITH selected_song AS (
	SELECT song_id as new_suggestion_song_id 
	FROM song
	INNER JOIN album ON album.album_id = song.song_album_id
	INNER JOIN artist ON artist.artist_id = album.album_artist_id
	WHERE song_name = 'song1' 
	AND album_name = 'album3'
	AND artist_name = 'artist3'
	), suggestion_insert AS (
	INSERT INTO suggestion( 
	suggestion_type, suggestion_suggester_id, suggestion_suggestee_id)
	VALUES ('SO', 10, 5)
	RETURNING suggestion_id as inserted_suggestion_id
)
INSERT INTO song_suggestion(
suggestion_id, song_id)
SELECT inserted_suggestion_id, new_suggestion_song_id
FROM  selected_song, suggestion_insert;


-- Query for when a song suggestion is added. First attempt to insert
-- the song, album and artist and then select the ids of each
-- then insert the new suggestion into the suggestions table
-- then insert the song_suggestion into the song_suggestion table
-- the example is inserting song30 from album30 by artist30 
-- suggested by suggester with id=10 to suggester with id=5
WITH suggested_song(suggested_song_name, suggested_album_name, suggested_artist_name) AS (
    VALUES('song30', 'album30', 'artist30')
    ), suggested_to_and_by( suggested_by_id, suggested_to_id ) AS (
    VALUES(10, 5))
    ), artist_insert AS (
    INSERT INTO artist(artist_name)
    SELECT suggested_artist_name
    FROM suggested_song
    ON CONFLICT DO NOTHING
    ), artist_select AS (
    SELECT artist_id FROM artist
    WHERE artist_name = (SELECT suggested_artist_name FROM suggested_song)
    ), album_insert AS (
    INSERT INTO album(album_name, album_artist_id)
    SELECT suggested_album_name, artist_id
    FROM suggested_song, artist_select
    ON CONFLICT DO NOTHING
    ), album_select AS (
    SELECT album_id FROM album
    WHERE album_name = (SELECT suggested_album_name FROM suggested_song)
    ), song_insert AS (
    INSERT INTO song(song_name, song_album_id)
    SELECT suggested_song_name, album_id
    FROM suggested_song, album_select
    ON CONFLICT DO NOTHING
    ), song_select AS (
    SELECT song_id FROM song
    WHERE song_name = (SELECT suggested_song_name FROM suggested_song)
    ), suggestion_insert AS (
    INSERT INTO suggestion( 
    suggestion_type, suggestion_suggester_id, suggestion_suggestee_id)
    SELECT 'SO', suggested_by_id, suggested_to_id
    FROM suggested_to_and_by
    RETURNING suggestion_id as inserted_suggestion_id
    )   
INSERT INTO song_suggestion(
suggestion_id, song_id)
SELECT inserted_suggestion_id, suggested_song_id
FROM  suggested_song, suggestion_insert;




-- query to select song name, suggestion date, suggester name, and suggestee name
-- of all song suggestions
SELECT song_name, suggestion_date, suggested_by.suggester_id, suggested_to.suggester_id 
FROM suggestion
INNER JOIN song_suggestion ON song_suggestion.suggestion_id = suggestion.suggestion_id
INNER JOIN song ON song.song_id = song_suggestion.song_id
INNER JOIN suggester suggested_by ON suggested_by.suggester_id = suggestion.suggestion_suggester_id
INNER JOIN suggester suggested_to ON suggested_to.suggester_id = suggestion.suggestion_suggestee_id
WHERE suggestion_type = 'SO';

-- query to select song_name, album_name, artist_name
-- of all songs, including those that don't have an associated album.
-- want to do this with another join instead of the union, idk if its possible
SELECT song_name, album_name, artist_name FROM song
JOIN album ON album.album_id = song.song_album_id
JOIN artist ON artist.artist_id = album.album_artist_id
UNION
SELECT song_name, NULL, artist_name FROM song
JOIN artist ON artist.artist_id = song.song_artist_id;

-- Similar to the above query, but with a join instead of the union
-- without the COALESCE it would have a column for artist from the album and a column for artist from the song
-- they would have nulls where the other didn't, the coalesce function combines them into 1 column
SELECT song_name, album_name, COALESCE(artist_of_album.artist_name, artist_of_song.artist_name) AS artist_name FROM song
LEFT JOIN album ON song.song_album_id = album.album_id
LEFT JOIN artist artist_of_album ON artist_of_album.artist_id = album.album_artist_id
LEFT JOIN artist artist_of_song ON artist_of_song.artist_id = song.song_artist_id;