<p align="center">
  <img src="https://github.com/Team-LANS/luups-map/blob/master/luupsmap/static/img/logo.png"/>
</p>
<h1 align="center">LUUPSMAP</h1>
<p align="center">
  <a href="https://shields.io/">
    <img src="https://img.shields.io/badge/written_in-python3-3498db.svg?style=for-the-badge" />
  </a>
  <a href="https://shields.io/">
    <img src="https://img.shields.io/badge/using-postgres-909090.svg?style=for-the-badge" />
  </a>
</p>
<p align="center">
  <a href="https://forthebadge.com/">
    <img src="https://forthebadge.com/images/badges/built-with-grammas-recipe.svg" />
  </a>
</p>


A helpful tool for users of [LUUPS](https://www.luups.net/shop/gutscheinbuch/luups-wien/):
* Display all venues on a map
* Filter by voucher type, opening hours,...

## Development

LUUPSMAP has a number of dependencies. Install them using

```bash
pip install -r requirements.txt
```

### Environment Variables

LUUPSMAP requires a number of environment variables to run. Create a `.env` file in the application root and add at
least the following variables:

```bash
APP_SETTINGS="luupsmap.config.DevelopmentConfig"

SECRET_KEY=<application-key>

DB_USER = <db-user>
DB_PW = <db-password>

GMAPS_API_KEY=<api-key>
```

Confirm that you can start the application by running

```bash
flask run
```

You might need to set the environment variable `FLASK_APP` first:
```bash
# UNIX
export FLASK_APP=luupsmap

# WINDOWS
set FLASK_APP=luupsmap
```

### Database 

LUUPSMAP requires PostgreSQL to be running under `localhost:5432`. The development database is named `luups_map_dev`
and needs to be created manually.

Initialize with the following command:

```bash
flask db init
````

After changing the model create migrations and upgrade the database using:

```bash
flask db migrate -m <descriptive-message>
flask db upgrade
```

To seed the database with data run:

```bash
flask data seed
```


Seed data is taken from the csv files in `data`. These files need to be edited manually, however some data can be
auto-completed using the [Google Place API](https://developers.google.com/places/web-service/intro) by running:

```bash
flask data update
```

This will update the CSV with missing location data and venue data. For more information see
[update.py](/luupsmap/cli/commands/update.py).
