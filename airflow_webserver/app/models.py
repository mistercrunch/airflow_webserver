from flask.ext.appbuilder import Model
from flask.ext.appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from airflow.models import *


print('-='*50)
print(dir())
