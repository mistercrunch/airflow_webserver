from flask import Flask
from flask.ext.appbuilder import SQLA, AppBuilder

app = Flask(__name__)
app.config.from_object('config')
db = SQLA(app)
appbuilder = AppBuilder(
    app,
    db.session,
    base_template='airflow_webserver/base.html',
)

from app import views
