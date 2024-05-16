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
