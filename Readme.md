# Ghibli

Restful API

This project catalogs the movies name found in the worlds of [Ghibli](http://www.ghibli.jp/)

It was created using [Flask](https://flask.palletsprojects.com/en/1.1.x/).

### Prerequisites

- [Python3](https://www.python.org/) - Python 3.6 or later
- [Pymongo](https://www.python.org/)

## Getting Started

2. **Clone** the fork with HTTPS, using your local terminal to a preferred location, and **cd** into the project.

```bash
git clone https://github.com/hyaovi/ghibli.git

Cloning into 'ghibli'...
remote: Enumerating objects...

cd ghibli/
```

3. Create your virtual environment, and activate it.

```bash
python -m venv env

source env/bin/activate  # Linux/Mac
env/Scripts/activate  # Windows
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Run local server, and **DONE**!

```bash
python app.py

 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 195-467-363
```

## Built With

- [Flask](https://flask.palletsprojects.com/en/1.1.x/) Flask is a lightweight WSGI web application framework.
- [Pymongo](https://www.python.org/) PyMongo is a Python distribution containing tools for working with MongoDB

## Data Sources

- [Studio Ghibli API](https://ghibliapi.herokuapp.com/) The Studio Ghibli API catalogs the people, places, and things found in the worlds of [Ghibli](http://www.ghibli.jp/).
