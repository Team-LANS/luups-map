# Luups Map


## Development

Luups Map has a number of dependencies. Install them using 

```
pip install < requirements.txt
```

Confirm that you can start the application by running

```bash
flask run
```

### Environment Variables

Luups Map requires a number of environment variables to run. Create a `.env` file in the application root and add at least
the following variables:

```
APP_SETTINGS="luupsmap.config.DevelopmentConfig"

SECRET_KEY=<application-key>

DB_USER = <db-user>
DB_PW = <db-password>
DB_NAME = <db-name>

GMAPS_API_KEY=<api-key>
```

### Database 

Luups Map requires PostgreSQL to be running under `localhost:5432`. The development database is named `luups_map_dev` and 
needs to be created manually. 

After changing the model create migrations and upgrade the database using:

```bash
flask db migrate
flask db upgrade
```

