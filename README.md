# Catalog App



Catalag Web App catalogs the Music bands and albums, with the capability of adding music bands and their corresponding 
albums. The albums can bed edited or deleted, and can be associated with a registered user. The web app can be accessed via google plus and facebook login. The webapp can also be called for API data regarding the albums of the band and the registered user of the App.
  - Catalogs bands and their Albums
  - Bands and Albums can be easily added, edited and deleted.
  - Responds to API calls.




You can also:
  - Log in via public accounts such as facebook and google plus.

### Installation - on local host.

Web app requires setting up the database model.
Helper script attached to pre-populate some data.


Run the following commands in the order and start the server.

```sh
$ python models.py
$ python dbhelper.py
```

For starting server

```sh
$ python view.py
```



Verify the deployment by navigating to your server address in your preferred browser.

```sh
127.0.0.1:5000
```

### Installation - on Linux Webserver

Web app requires setting up the database model.
Helper script attached to pre-populate some data.
The webserver is configured for the Amazon Web Service LightSail Instance.
The server name is http://ec2-52-91-31-136.compute-1.amazonaws.com/
The alias (public IP Address for the webserver is http://52.91.31.136/.
The server uses Apache2 and the web app is in python2.7.
The port used is 2200.


Run the following commands in the order and start the server.

```sh
$ python models.py
$ python dbhelper.py
```

For starting server

```sh
$ python view.py
```
















