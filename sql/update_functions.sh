#!/bin/bash



all_output=$( (psql --host="$DB_HOST" --username="postgres" -w --dbname="$DB_NAME" --file=."/pg_functions.sql")  2>&1)

errors=$(echo "$all_output" | grep 'ERROR')
notices=$(echo "$all_output" | grep 'NOTICE')
query_output=$(echo "$all_output" | grep -v 'psql:')

if [ -n "$errors" ]; then
    echo "There were errors running pg_functions.sql:"
    echo $errors
    exit 1
fi
echo "$*" | grep -qFe "-v"
if [ $? -eq 0 ]; then
    echo "pg_functions.sql output:"
    echo "$query_output"
fi
