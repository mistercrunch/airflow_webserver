from flask import render_template
from flask.ext.appbuilder.models.sqla.interface import SQLAInterface
from flask.ext.appbuilder import ModelView
from app import appbuilder, db, models


class TaskInstanceMV(ModelView):
    datamodel = SQLAInterface(models.TaskInstance)
    #list_columns = ['dag_id', 'task_id', 'execution_date']
    list_columns = (
        'state', 'dag_id', 'task_id', 'execution_date', 'operator',
        'start_date', 'end_date', 'duration', 'job_id', 'hostname',
        'unixname', 'priority_weight', 'queue', 'queued_dttm', 'try_number',
        'pool', 'log_url')

appbuilder.add_view(
    TaskInstanceMV, "Task Instances", icon="fa-table", category="Manage")

@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404

db.create_all()


