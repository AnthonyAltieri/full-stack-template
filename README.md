# Full Stack Application Template
  
  
### Data
* Postgres Database via Docker Compose
### Backend
* Language: Python
* Frameworks: Flask, Flask-Restful, Flask-SQLAlchemy, Alembic (DB migration manager)
* Dependency Management: Poetry
* Scripts: format, run
* Features: Environment based configuration
### Frontend
Bootstrapped with [create-react-app](https://reactjs.org/docs/create-a-new-react-app.html)
* Language: Javascript / HTML / CSS
* Frameworks: React, Redux, axios
* Dependency Management: npm
  
  
## Operation
### Backend
###### Running Application
```
# ensure script files are executable
chmod +x ./backend/script/*

# run flask server
./backend/script/run.sh
```
###### Formatting Code
```
# ensure script files are executable
chmod +x ./backend/script/*

# run black and isort formatters
./backend/script/format.sh
```
