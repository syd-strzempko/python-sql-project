## Bathrooms Project

### About

__TODO__

### Installation

#### Python Version Management

Per [pyenv-win](https://pypi.org/project/pyenv-win/) version management package

```
pyenv versions
pyenv install 3.7.4
pyenv local 3.7.4
```

#### Virtual Environment

Need virtual environment for version management

```
python -m pip install –user virtualenv # This wasn't working -- used python 2.7 regardless of local
```

Per [StackOverflow](https://stackoverflow.com/a/64139341), need to rewrite contents of bash to ensure pyenv installed version corresponds to bash shorthand for python

```
pyenv which python
python --version
```


__C:\Users\Administrator\.bashrc__
```
alias python='winpty c:/Python27/python.exe'
alias PYTHON='winpty c:/Python27/python.exe'
export PATH=$PATH:"/C/Python27/python.exe"
```
__Changed to__
```
alias python='winpty c:/Users/Administrator/.pyenv/pyenv-win/versions/3.7.4/python.exe'
alias PYTHON='winpty c:/Users/Administrator/.pyenv/pyenv-win/versions/3.7.4/python.exe'
export PATH=$PATH:"/C/Users/Administrator/.pyenv/pyenv-win/versions/3.7.4/python.exe"
```

```
python -m pip install virtualenv # Upgrade pip as needed for this step if it fails, skip -u flag
python -m venv env
.\env\Scripts\activate # Failed 
source ./env/Scripts/activate # Succeeded
```

### Running after install (fresh bash)

```
source ./env/Scripts/activate
flask run
```

### TO install any packages

```
python -m pip install <package>
```

### Access SQL DB directly

```
flask shell
from extensions import db
from models.<ex entries> import <etc Entry>
db.create_all()
```

#### References

[Python in Jinja](https://stackoverflow.com/questions/6036082/call-a-python-function-from-jinja2)

[Jinja Templating](https://jinja.palletsprojects.com/en/3.0.x/tricks/#highlighting-active-menu-items)

[Flask CRUD App Tutorial](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3#step-6-displaying-a-single-post)

https://stackoverflow.com/a/74805157

[Flask blueprint pattern](https://flask.palletsprojects.com/en/2.1.x/tutorial/views/)

[Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/)

[preload sqlalchemy](https://stackoverflow.com/a/63291666)

[SQLAlchemy model to_dict](https://www.slingacademy.com/article/sqlalchemy-convert-query-results-into-dictionary/#Basic_Conversion_to_Dictionary)

[session list querying](https://stackoverflow.com/a/48467116)

https://stackoverflow.com/questions/12350807/whats-the-difference-between-model-query-and-session-querymodel-in-sqlalchemy

https://stackoverflow.com/questions/920724/the-right-way-to-auto-filter-sqlalchemy-queries

