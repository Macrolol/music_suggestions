DROP FUNCTION IF EXISTS pg_functions_testing();
CREATE OR REPLACE FUNCTION pg_functions_testing()
RETURNS text AS
$$
DECLARE
    test_value_artist_name CONSTANT text := 'Test Artist';
    test_value_album_name CONSTANT text := 'Test Album';
    test_value_song_name CONSTANT text := 'Test Song';
    result text;
    add_artist_result integer;
    add_album_result integer;
    add_song_result integer;
    selected_song_id integer;
BEGIN

    DELETE FROM artist
    WHERE artist_name = test_value_artist_name;

    SELECT add_artist(test_value_artist_name)
    INTO add_artist_result;

    RAISE NOTICE 'add_artist_result: %', add_artist_result;

    SELECT add_album(test_value_album_name, add_artist_result)
    INTO add_album_result;

    RAISE NOTICE 'add_album_result: %', add_album_result;

    SELECT add_song_by_album_id(test_value_song_name, add_album_result)
    INTO add_song_result;

    RAISE NOTICE 'add_song_result: %', add_song_result;

    SELECT get_song_id_by_name_and_album_name_and_artist_name(test_value_song_name, test_value_album_name, test_value_artist_name)
    INTO selected_song_id;

    RAISE NOTICE 'selected_song_id: %', selected_song_id;

    IF selected_song_id = add_song_result THEN
        RETURN 'success';
    END IF;


    RETURN 'failure';
END;
$$ LANGUAGE plpgsql;