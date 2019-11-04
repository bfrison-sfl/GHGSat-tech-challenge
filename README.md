# GHGSat tech challenge

## How to start the app

### With Docker

in the main git repository folder, execute:

```
 docker build -t ghgsat .
```
then execute:

```
 docker run -d -p 5000:5000 --name GHGSat-flask ghgsat
```

### Without Docker

cd into the `Flask` folder. Execute:
```
 export FLASK_APP=ghgsat.py

 flask run
```

The site can be accessed by typing `localhost:5000` in the address bar.