-- This is a file holding all the functions to be loaded into the database.
-- This is a tentative file, it will be updated as the functions are added
-- also, not all function will be needed in production, so a production file
-- will be created later.

DROP FUNCTION IF EXISTS add_artist(arg_artist_name text);
CREATE OR REPLACE FUNCTION add_artist(arg_artist_name text)
RETURNS integer AS
$$
DECLARE
    new_artist_id integer;
BEGIN
    INSERT INTO artist(artist_name)
    VALUES (arg_artist_name)
    RETURNING artist_id INTO new_artist_id;
    RETURN new_artist_id;
END;
$$ LANGUAGE plpgsql;

DROP FUNCTION IF EXISTS add_album(arg_album_name text, arg_artist_id integer);
CREATE OR REPLACE FUNCTION add_album(arg_album_name text, arg_artist_id integer)
RETURNS integer AS
$$
DECLARE
    new_album_id integer;
BEGIN
    INSERT INTO album(album_name, album_artist_id)
    VALUES (arg_album_name, arg_artist_id)
    RETURNING album_id INTO new_album_id;
    RETURN new_album_id;
END;
$$ LANGUAGE plpgsql;

DROP FUNCTION IF EXISTS add_song_by_album_id(arg_song_name text, arg_song_album_id integer);
CREATE OR REPLACE FUNCTION add_song_by_album_id(arg_song_name text, arg_song_album_id integer)
RETURNS integer AS
$$
DECLARE
    new_song_id integer;
BEGIN
    INSERT INTO song(song_name, song_album_id)
    VALUES(arg_song_name, arg_song_album_id)
    RETURNING song_id INTO new_song_id;
    RETURN new_song_id;
END;
$$ LANGUAGE plpgsql;

DROP FUNCTION IF EXISTS add_song_by_artist_id(arg_song_name text, arg_artist_id integer);
CREATE OR REPLACE FUNCTION add_song_by_artist_id(
    arg_song_name text,
    arg_artist_id integer)
RETURNS integer AS
$$
DECLARE
    new_song_id integer;
BEGIN
    INSERT INTO song(song_name, song_artist_id)
    VALUES(arg_song_name, arg_artist_id)
    RETURNING song_id INTO new_song_id;
    RETURN new_song_id;
END;
$$ LANGUAGE plpgsql;

-- something similar to this has been added in db_setup.sql as 
-- a view that has all song_name(s), album_name(s), artist_name(s)
-- this version doesn't account for songs that are not in an album
-- but the view in db_setup.sql does
DROP FUNCTION IF EXISTS select_all_songs();
CREATE OR REPLACE FUNCTION select_all_songs()
RETURNS TABLE(song_name song.song_name%TYPE, album_name album.album_name%TYPE, artist_name artist.artist_name%TYPE) AS
$$
BEGIN
    RETURN QUERY
        SELECT song.song_name, album.album_name, artist.artist_name
        FROM song
        JOIN album ON song.song_album_id = album.album_id
        JOIN artist ON album.album_artist_id = artist.artist_id;
END;
$$ LANGUAGE plpgsql;



DROP FUNCTION IF EXISTS get_artist_id_by_name(artist_name text);
--This function returns the artist_id of the artist with the given name
-- if no artist with that name exists, it returns NULL
CREATE OR REPLACE FUNCTION get_artist_id_by_name(arg_artist_name text)
RETURNS integer AS
$$
DECLARE
    selected_artist_id integer;
BEGIN
    SELECT artist.artist_id
    FROM artist
    WHERE artist.artist_name = arg_artist_name
    INTO selected_artist_id;
    RETURN selected_artist_id;
END;
$$ LANGUAGE plpgsql;


DROP FUNCTION IF EXISTS get_album_id_by_name_and_artist_id(arg_album_name text, arg_artist_id integer);
CREATE OR REPLACE FUNCTION get_album_id_by_name_and_artist_id(arg_album_name text, arg_artist_id integer)
RETURNS integer AS
$$
DECLARE
    selected_album_id integer;
BEGIN
    SELECT album.album_id
    FROM album
    WHERE album.album_name = arg_album_name AND album.album_artist_id = arg_artist_id
    INTO selected_album_id;
    RETURN selected_album_id;
END;
$$ LANGUAGE plpgsql;

DROP FUNCTION IF EXISTS get_song_id_by_name_and_album_id(arg_song_name text, arg_album_id integer);
CREATE OR REPLACE FUNCTION get_song_id_by_name_and_album_id(arg_song_name text, arg_album_id integer)
RETURNS integer AS
$$
DECLARE
    selected_song_id integer;
BEGIN
    SELECT song.song_id
    FROM song
    WHERE song.song_name = arg_song_name AND song.song_album_id = arg_album_id
    INTO selected_song_id;
    RETURN selected_song_id;
END;
$$ LANGUAGE plpgsql;



DROP FUNCTION IF EXISTS get_song_id_by_name_and_artist_id(arg_song_name text, arg_artist_id integer);
CREATE OR REPLACE FUNCTION get_song_id_by_name_and_artist_id(arg_song_name text, arg_artist_id integer)
RETURNS integer AS
$$
DECLARE
    selected_song_id integer;
BEGIN
    -- using the song_album_artist_id_names view defined in db_setup.sql 
    SELECT song.song_id
    FROM song_album_artist_id_names
    WHERE song_name = arg_song_name AND song_artist_id = arg_artist_id
    INTO selected_song_id;
    RETURN selected_song_id;

    -- SELECT song.song_id
    -- FROM song
    -- WHERE song.song_name = arg_song_name AND song.song_artist_id = arg_artist_id
    -- INTO selected_song_id;
    -- RETURN selected_song_id;
END;
$$ LANGUAGE plpgsql;

DROP FUNCTION IF EXISTS get_song_id_by_name_and_artist_name(arg_song_name text, arg_artist_name text);
CREATE OR REPLACE FUNCTION get_song_id_by_name_and_artist_name(arg_song_name text, arg_artist_name text)
RETURNS integer AS
$$
DECLARE
    selected_song_id integer;
BEGIN
    --using the song_album_artist_id_names view created in db_setup.sql 
    SELECT song_id
    FROM song_album_artist_id_names
    WHERE song_name = arg_song_name AND artist_name = arg_artist_name
    INTO selected_song_id;
    RETURN selected_song_id;
END;
$$ LANGUAGE plpgsql;




DROP FUNCTION IF EXISTS get_song_id_by_name_and_album_name_and_artist_name(arg_song_name text, arg_album_name text, arg_artist_name text);
CREATE OR REPLACE FUNCTION get_song_id_by_name_and_album_name_and_artist_name(arg_song_name text, arg_album_name text, arg_artist_name text)
RETURNS integer AS
$$
DECLARE
    selected_song_id integer;
BEGIN

    --using the song_album_artist_id_names view created in db_setup.sql
    SELECT song_id
    FROM song_album_artist_id_names
    WHERE song_name = arg_song_name AND album_name = arg_album_name AND artist_name = arg_artist_name
    INTO selected_song_id;
    RETURN selected_song_id;
END;
$$ LANGUAGE plpgsql;

DROP FUNCTION IF EXISTS add_song_suggestion_by_song_id( arg_song_id integer, arg_suggester_id integer, arg_suggestee_id integer);
CREATE OR REPLACE FUNCTION add_song_suggestion_by_song_id(
    arg_song_id integer,
    arg_suggester_id integer,
    arg_suggestee_id integer)
RETURNS integer AS
$$
DECLARE
    suggestion_id integer;
BEGIN
    INSERT INTO suggestion(       
        suggestion_suggester_id,
        suggestion_suggestee_id)
    VALUES(
        arg_suggester_id,
        arg_suggestee_id)
    RETURNING suggestion.suggestion_id INTO suggestion_id;
    INSERT INTO song_suggestion(
        suggestion_id,
        arg_song_id)
    VALUES(
	suggestion_id,
	arg_song_id)
    RETURNING song_suggestion.suggestion_id INTO suggestion_id;
    RETURN suggestion_id;
END;
$$ LANGUAGE plpgsql;

DROP FUNCTION IF EXISTS add_song_suggestion_by_artist_name_album_name_song_name(arg_artist_name text, arg_album_name text, arg_song_name text, arg_suggester_id integer, arg_suggestee_id integer);
CREATE OR REPLACE FUNCTION add_song_suggestion_by_artist_name_album_name_song_name(
    arg_artist_name text,
    arg_album_name text,
    arg_song_name text,
    arg_suggester_id integer,
    arg_suggestee_id integer)
RETURNS integer AS 
$$
DECLARE
    new_suggestion_id integer;
    suggested_song_id integer;
    suggested_album_id integer;
    suggested_artist_id integer;
BEGIN

    SELECT get_artist_id_by_name(arg_artist_name) 
    INTO suggested_artist_id;
    IF suggested_artist_id IS NULL THEN
        RAISE NOTICE 'Suggested Artist % does not exist, adding', arg_artist_name;
        suggested_artist_id = add_artist(arg_artist_name);
        suggested_album_id = add_album(arg_album_name, suggested_artist_id);
        suggested_song_id = add_song(arg_song_name, suggested_album_id);
    ELSE
        SELECT get_album_id_by_name_and_artist_id(arg_album_name, suggested_artist_id) 
        INTO suggested_album_id;
        IF suggested_album_id IS NULL THEN
            RAISE NOTICE 'Suggested Album % does not exist, adding', arg_album_name;
            suggested_album_id = add_album(arg_album_name, suggested_artist_id);
            suggested_song_id = add_song(arg_song_name, suggested_album_id);
        ELSE
            SELECT get_song_id_by_name_and_album_id(arg_song_name, suggested_album_id)
            INTO suggested_song_id;
            IF suggested_song_id IS NULL THEN
                RAISE NOTICE 'Suggested Song % does not exist, adding', arg_song_name;
                suggested_song_id = add_song(arg_song_name, suggested_album_id);
            END IF;
        END IF;
    END IF; 

    SELECT add_song_suggestion_by_song_id(suggested_song_id, arg_suggester_id, arg_suggestee_id) 
    INTO new_suggestion_id;

    RETURN new_suggestion_id;
END;
$$ LANGUAGE plpgsql;

DROP FUNCTION IF EXISTS add_song_suggestion_by_artist_name_song_name(arg_artist_name text, arg_song_name text, arg_suggester_id integer, arg_suggestee_id integer);
CREATE OR REPLACE FUNCTION add_song_suggestion_by_artist_name_song_name(
    arg_artist_name text,
    arg_song_name text,
    arg_suggester_id integer,
    arg_suggestee_id integer)
RETURNS integer AS
$$
DECLARE
    new_suggestion_id integer;
    suggested_song_id integer;
    intermediate_album_id integer;
    suggested_artist_id integer;
BEGIN
    
    SELECT get_artist_id_by_name(arg_artist_name) 
    INTO suggested_artist_id;
    IF suggested_artist_id IS NULL THEN
        RAISE NOTICE 'Suggested Artist % does not exist, adding', arg_artist_name;
        suggested_artist_id = add_artist(arg_artist_name);
        suggested_song_id = add_song(arg_song_name, suggested_artist_id);
    ELSE
        SELECT get_song_id_by_name_and_artist_id(arg_song_name, suggested_artist_id)
        INTO suggested_song_id;
        IF suggested_song_id IS NULL THEN
            RAISE NOTICE 'Suggested Song % does not exist, adding', arg_song_name;
            suggested_song_id = add_song(arg_song_name, suggested_artist_id);
        END IF;
    END IF;
    
    SELECT add_song_suggestion_by_song_id(suggested_song_id, arg_suggester_id, arg_suggestee_id) 
    INTO new_suggestion_id;
    
    RETURN new_suggestion_id;
END;
$$ LANGUAGE plpgsql;


DROP FUNCTION IF EXISTS try_login(arg_email text, arg_password text);
CREATE OR REPLACE FUNCTION try_login(arg_email text, arg_password text)
RETURNS record AS
$$
DECLARE
    logging_in_suggester_with_password record;
    logging_in_suggester record;
BEGIN
    SELECT *
    INTO logging_in_suggester_with_password
    FROM suggester
    WHERE suggester_email = arg_email;

    IF logging_in_suggester_id IS NULL THEN
        RETURN NULL;
    END IF;
    IF crypt(arg_password, logging_in_suggester.suggester_password) THEN
        SELECT suggester_id, suggester_email, suggester_username, suggester_created_date
        FROM  logging_in_suggester
        INTO logging_in_suggester;
        RETURN logging_in_suggester;
    END IF;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

DROP FUNCTION IF EXISTS create_new_suggester(arg_username text, arg_email text, arg_password text);
CREATE OR REPLACE FUNCTION create_new_suggester(arg_username text, arg_email text, arg_password text)
RETURNS record AS
$$
DECLARE
    existing_suggester_id integer;
    new_suggester record;
BEGIN
    SELECT suggester_id FROM suggester
    WHERE suggester_email = arg_email
    INTO existing_suggester_id;

    IF existing_suggester_id IS NULL THEN
        INSERT INTO suggester (suggester_username, suggester_tag_discriminator, suggester_password, suggester_email)
        VALUES (arg_username, generate_tag_discriminator(arg_username), crypt(arg_password, gen_salt('bf')), arg_email)
        RETURNING suggester_id, suggester_username, suggester_email, suggester_created_date INTO new_suggester;
        RETURN new_suggester;
    END IF;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

DROP FUNCTION IF EXISTS generate_tag_discriminator(arg_username text);
CREATE OR REPLACE FUNCTION generate_tag_discriminator(arg_username text)
RETURNS smallint AS
$$
DECLARE
    MAX_TAG_DISCRIMINATOR CONSTANT smallint := 9999;
    MIN_TAG_DISCRIMINATOR CONSTANT smallint := 1000;
    potential_discriminator smallint;
    existing_discriminators smallint[] := ARRAY( SELECT suggester_tag_discriminator
                                            FROM suggester
                                            WHERE suggester_username = arg_username);
BEGIN

    LOOP

    -- randomly generate a discriminator between MIN_TAG_DISCRIMINATOR(1000) and MAX_TAG_DISCRIMINATOR(9999)
    SELECT FLOOR(RANDOM() * (MAX_TAG_DISCRIMINATOR - MIN_TAG_DISCRIMINATOR + 1) + MIN_TAG_DISCRIMINATOR)
    INTO potential_discriminator;

    -- check if the discriminator already in use by another suggester with the same username    
    IF potential_discriminator = ANY(existing_discriminators) THEN
        CONTINUE;
    END IF;
    RETURN potential_discriminator;
    END LOOP;
END;
$$ LANGUAGE plpgsql;