## Bathrooms Project

### About

For trans/gender nonconforming individuals, going to public venues such as bars, coffee shops, and restaurants can often be a fraught experience. Public scrutiny, mismatch in name or appearance between identity or payment methods, and being faced with the decision of which bathroom to use when there are only two distinct options is a constant calculation and risk mitigation exercise that is exhausting for people who simply want to exist in public spaces. Although there are often too many factors in the equation to guarantee a feeling of complete safety, one major step is the introduction of gender neutral or gender nonspecific restrooms with signage indicating such. Just the simple existence of these facilities can remove so much anxiety, and yet it is exceedingly difficult to know beforehand what to expect.

The goal of this project is to create a crowdsourcing site for identifying gender neutral/gender nonspecific restrooms. Using a SQLite database, Python Flask middleware, and Jinja templating incorporating Google Maps js API in the frontend, users are able to submit locations which indicate a public venue with these facilities.

Access to restroom facilities with a minimum of anxiety, dysphoria, or feelings of unsafety is an expectation many have but few who do not identify outside the gender binary consider. To make these spaces available and easily identifiable is a step towards a more equitable society where the implicit privelege of some becomes the explicit right for all!

### Access

TODO: Install on website

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

* [Python in Jinja](https://stackoverflow.com/questions/6036082/call-a-python-function-from-jinja2)

* [Jinja Templating](https://jinja.palletsprojects.com/en/3.0.x/tricks/#highlighting-active-menu-items)

* [Flask CRUD App Tutorial](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3#step-6-displaying-a-single-post)

* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/)

* [Preload DB](https://stackoverflow.com/a/63291666)

* [SQLAlchemy model to_dict](https://www.slingacademy.com/article/sqlalchemy-convert-query-results-into-dictionary/#Basic_Conversion_to_Dictionary)

* [SQLAlchemy List Querying](https://stackoverflow.com/a/48467116)

* [SQLAlchemy Model v Session Querying](https://stackoverflow.com/questions/12350807/whats-the-difference-between-model-query-and-session-querymodel-in-sqlalchemy)

[Get device geolocation](https://developers.google.com/maps/documentation/javascript/examples/map-geolocation)

[Set Google Maps Bounds](https://stackoverflow.com/a/19304625)

[Remove marker](https://stackoverflow.com/a/74492809)