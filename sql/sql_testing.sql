
--this query inserts several suggesters into the suggester table, with placeholder email addresses
INSERT INTO suggester (suggester_name, suggester_contact)
VALUES ('John', 'john@email.com'), ('Jane', 'jane@email.com'), ('Joe', 'joe@email.com'),     
       ('Jack', 'jack@email.com'), ('Jill', 'jill@email.com'), ('Juan', 'juan@email.com'),
       ('Steve', 'steve@email.com'), ('Sally', 'sally@email.com'), ('Sue', 'sue@email.com'),
       ('Phil', 'phil@email.com'), ('Pam', 'pam@email.com'), ('Paul', 'paul@email.com');


--this query inserts several prefferences into the prefferences table
INSERT INTO prefferences (prefference_suggester_id, prefference_wants_suggestions, prefference_wants_feedback)
VALUES (1, 't', 'f'), (2, 't', 't'), (3, 'f', 'f'),
       (4, 't', 'f'), (5, 't', 't'), (6, 'f', 'f'),
       (7, 't', 'f'), (8, 't', 't'), (9, 'f', 'f'),
       (10, 't', 'f'), (11, 't', 't'), (12, 'f', 'f');
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
