from flask import render_template
from flask.ext.appbuilder.models.sqla.interface import SQLAInterface
from flask.ext.appbuilder import Model, ModelView

from . import appbuilder
from airflow.models import ID_LEN, PickleType, State
from airflow import models

from sqlalchemy import Boolean, Column, Integer, DateTime, String, func

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

class Connection(Model):
    """
    Placeholder to store information about different database instances
    connection information. The idea here is that scripts use references to
    database instances (conn_id) instead of hard coding hostname, logins and
    passwords when using operators or hooks.
    """
    __tablename__ = "connection"

    id = Column(Integer(), primary_key=True)
    conn_id = Column(String(ID_LEN))
    conn_type = Column(String(500))
    host = Column(String(500))
    schema = Column(String(500))
    login = Column(String(500))
    password = Column('password', String(5000))
    port = Column(Integer())
    is_encrypted = Column(Boolean, unique=False, default=False)
    is_extra_encrypted = Column(Boolean, unique=False, default=False)
    extra = Column('extra', String(5000))


class ConnectionMV(ModelView):
    datamodel = SQLAInterface(Connection)
    list_columns = ['conn_id', 'conn_type', 'host', 'is_encrypted']
    search_columns = []
appbuilder.add_view(
    ConnectionMV, "Connections", icon="fa-lock", category="Admin")

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

class Variable(ModelView):
    datamodel = SQLAInterface(models.Variable)
appbuilder.add_view(Variable, "Variable", icon="fa-lock", category="Admin")

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


class TaskInstance(ModelView):
    datamodel = SQLAInterface(models.TaskInstance)
    list_columns = (
        'state', 'dag_id', 'task_id', 'execution_date', 'operator',
        'start_date', 'end_date', 'duration', 'job_id', 'hostname',
        'unixname', 'priority_weight', 'queue', 'queued_dttm', 'try_number',
        'pool', 'log_url')
appbuilder.add_view(TaskInstance, "Task Instances", icon="fa-table", category="Manage")

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


class DagRun(Model):
    """
    DagRun describes an instance of a Dag. It can be created
    by the scheduler (for regular runs) or by an external trigger
    """
    __tablename__ = "dag_run"

    id = Column(Integer, primary_key=True)
    dag_id = Column(String(ID_LEN))
    execution_date = Column(DateTime, default=func.now())
    start_date = Column(DateTime, default=func.now())
    end_date = Column(DateTime)
    state = Column('state', String(50), default=State.RUNNING) # Modified
    run_id = Column(String(ID_LEN))
    external_trigger = Column(Boolean, default=True)
    conf = Column(PickleType)


class DagRunMV(ModelView):
    datamodel = SQLAInterface(DagRun)
    search_columns = ['execution_date']
    list_columns = (
        'dag_id', 'execution_date', 'state', 'run_id', 'external_trigger')
    edit_columns = (
        'dag_id', 'execution_date', 'run_id', 'state', 'external_trigger')
appbuilder.add_view(DagRunMV, "DAG Runs", icon="fa-table", category="Manage")

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404

