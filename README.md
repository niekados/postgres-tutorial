# PostgreSQL Turorial

## Start PostgreSQL and Initialise/ Install DB

1. Download raw github repo using terminal:
    `wget https://raw.githubusercontent.com/Code-Institute-Solutions/postgresql-and-python/main/01_installing_the_chinook_database/Chinook_PostgreSql.sql`
2. Start the Postgres command-line interface, or shell, in order to get the Chinook
database installed, and the data populated.
[for this CI template we need to type `set_pg` before `psql`]
To launch the Postgres CLI, we can simply type "`psql`" and hit enter.

- To view, or list, any databases in our environment, we can type `\l`.
- By default, the Postgres CLI comes with 3 databases out of the box; '`postgres`', '`template0`', and '`template1`'.

3. Instead of using any of these default databases, let's create a new database for our Chinook lessons.
`CREATE DATABASE chinook;` (Don't forget the semicolon at the end of the command,
which is the standard way to separate each SQL statement), since you can theoretically
combine multiple commands in a single entry.
- If you've hit enter without adding the semicolon, it will assume you're wanting to add additional
commands, so just add your semicolon now, and hit enter.

4. To switch between databases, we can simply type `\c` followed by `the name of the database` we want to switch over to.
- `\c postgres` - now we're on the default postgres database.
- `\c chinook `- and now we're connected to our new database.
    - *The \c stands for 'connect' in case you're wondering, telling it which database to connect to.*
5. Finally, while we're connected to our new chinook database, we need to initialize or
install the downloaded sample Chinook PostgreSQL database.
`\i Chinook_PostgreSql.sql` The `\i` generally means include, integrate, install, or initialize.
Essentially, this file is an SQL script that contains all of the instructions needed to
create tables, and populate our database with information so that we have useful data for practice.

## Basic Query Searches

- To quit Postgres type `\q` or `quit`
- To start the Postgres shell with specific database open, we can actually include a flag to specify which database we'd
like to connect to once Postgres is loaded.
'`psql -d chinook`' . This will start the server, and tell it that the database we want to connect to is the one called "chinook", as declared by using the `-d` flag to specify a database name.
- `\dt` will allow us to display tables on our database. (We can use this to check and confirm that all tables and data were successfully added to the database.) Press `q` to go back to main DB menu in CLI.
- `SELECT * FROM "Artist";` retrieve all data from the Artist table.
    - *Technically you don't need to write the SQL commands in capital letters, but it's standard
practice to distinguish between the different pieces of your query string.*
    - *The asterisk is a common programming method to signify a wildcard, which essentially means
    to select anything and everything.
    Also note, I've used double-quotes intentionally, because using single-quotes will throw a 'syntax error',*
    - *Finally, the command must end with a semicolon, to specify that this is the end of our query.
    If you omit the semicolon and hit enter, nothing happens, but in reality, it's waiting for
    you to finish building your query, which can span multiple lines.*
- `SELECT "Name" FROM "Artist";` query the same table, but this time, only retrieve the "Name" column.
- `SELECT * FROM "Artist" WHERE "Name" = 'Queen';` search the same table, but this time specify
a particular artist name using the `WHERE` clause. As you may have noticed, I've used double-quotes again, **except when it comes to the specific value I'd like to search for, which must be in single-quotes.**
This is to distinguish between the various table and column names, versus the specific
context or value I need to find. 
- `SELECT * FROM "Artist" WHERE "ArtistId" = 51;` perform the same exact query, but this time we'll specify the ArtistId of 51 instead of the artist name. Since 51 is a primary key and integer, we don't need the single-quotes, but it will
still work if you include them.
- `SELECT * FROM "Album" WHERE "ArtistId" = 51;` perform the same exact query one more time, but instead of looking within the Artist table, look at the Album table.
- `SELECT * FROM "Track" WHERE "Composer" = 'Queen';` look within the table called "Track", and use the
column header of "Composer" to search for all tracks by Queen.

## Installin psycopg2 and wiring it with Python

PsycoPG2 is by far the most popular, and stable library for connecting Python to Postgres.

- To install it into our workspace.
`pip3 install psycopg2`
- Create a new Python file `touch sql-psycopg2.py`. (*It's important to note that you shouldn't call your file psycopg2.py, as this is a default
file already used by the package, and will cause your queries to always fail.*)
- first thing that we need to do now, is to '`import psycopg2`' at the top of our file.
```python
import psycopg2
```
- Then, we need to have psycopg2 connect to our Postgres database called Chinook, using
the `.connect()` method, and we'll assign that to a variable of '`connection`'.
We are only specifying the name of our database, `"chinook"`, **in double-quotes**, but you could
include additional connection values such as `host`, `username`, `password`, and so on.
```python
# Connect to "chinook" database
connection = psycopg2.connect(database="chinook")
```
- Next, our connection needs an instance of a Cursor Object. A cursor object is another way of saying a 'set' or 'list', similar to an 'array' in JavaScript.
Essentially, anything that we query from the database will become part of this cursor object,
and to read that data, we should iterate over the cursor using a for-loop, as an example.
```python
# Build a cursor object of the database
cursor = connection.cursor()
```
- we need to set up a way for our data to be retrieved, or fetched, from the cursor.
Assign this to a variable of '`results`' since it'll fetch any result that gets queried.
*Please note, if we need to query multiple records from our database, we should use the*
`.fetchall()` *method*.
*Otherwise, if we're intentionally looking for one particular record, we could use the*
`.fetchone()` *method, which I will comment-out for now using the CTRL+/ command*.
```python 
# fetch the results (multiple)
results = cursor.fetchall()

# EXASMPLE of fetching single result
# fetch the result (single)
# results = cursor.fetchone()
```
- Next, once our results have been fetched, we need to end the connection to the database,
so the connection isn't always persistent.
```python
# Close the connection
connection.close()
```
- In order to retrieve each record individually, we need to iterate over the results using a for-loop.
For each individual result in the results list, print the result.
```python
# Print results
for result in results:
    print(result)
```
- After our cursor variable is defined, but before our results are fetched, we need to
perform our queries using the `.execute()` method.
Query #1 that we tested in the last video, was to simply select all records from the "Artist" table.
PsycoPG2 commands are actually quite similar to native SQL commands, with one little twist;
the precise use of quotations. **It's extremely important to note that we absolutely MUST use single-quotes to wrap our query, and double-quotes to specify particular values.**
```python
# Connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# Build a cursor object of the database
cursor = connection.cursor()

# QUERY 1 - select all records from the "Artist" table .
# MUST use single qoutes to wrap querry and double qoutes to specify particular values
cursor.execute('SELECT * FROM "Artist"')

# fetch the results (multiple)
results = cursor.fetchall()

# output:
# ('Michele Campanella',)
# ('Gerald Moore',)
# ('Mela Tenenbaum, Pro Musica Prague & Richard Kapp',)
# ('Emerson String Quartet',)
# ('C. Monteverdi, Nigel Rogers - Chiaroscuro; London Baroque; London Cornett & Sackbu',)
# ('Nash Ensemble',)
# ('Philip Glass Ensemble',)
```
-  Query #3, we're searching for only "Queen" from the Artist table.
Since we need to specify a particular record, **unfortunately any combination of single or
double quotes just won't work. We need to use a Python string placeholder, and then define the desired string within a list.** You can technically have multiple placeholders, depending on how detailed your query needs
to be, and each placeholder would be added to this list. Technically, since we know there should only be one result, we could use the `.fetchone()` method. This would print each column individually, instead of part of a tuple of column results. Save the file and let's run the same command to print our results.
```python
# Query 3 - select only "Queen" from "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# fetch the result (single)
results = cursor.fetchone()

# output:
# 51
# Queen
```