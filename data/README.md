# Import data into database

In this directory you'll see a Shape file called *openflights_airports.shp*. Using the free OGR2OGR tool, you can import the spatial data into a PostgreSQL database.

```
ogr2ogr -f PostgreSQL PG:"host=localhost user=postgres password=postgres dbname=yourdatabase" openflights_airports.shp
```

You'll need to install PostGIS (latest version) and PLPython (only needed for LPGA)

