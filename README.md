# Airflow Webserver

A proof of concept of moving the Airflow UI to use
[Flask App Builder (FAB)] (https://github.com/dpgaspar/Flask-AppBuilder).

<img width="500" src="http://i.imgur.com/hpNceF6.png" >


## Rational for porting to FAB
- FAB offers support for critical functionality that we need in Airflow
  - Comprehensive support for most [authentication backends] (https://flask-appbuilder.readthedocs.io/en/latest/security.html#authentication-methods)
  - A permission framework, allowing to easily manage roles, attribution of
    of roles to users, and auto-creation of sets of perm for every model
    (can_show, can_edit, can_list, can_delete, ...), and on every view.
  - A REST api, automagically generated based on model and taking permissions
    into account
- An easy migration path for our current views, since it's all Flask,
  SQLAlchemy and Jinja2. Porting to something like Django might require a lot
  more effort

## Approach

Import Airflow's models and wrap a FAB ModelView around them. Try to
match as much as possible of the Flask-Admin modelview feature out of the box.
Ideally models don't need to be copied, just imported from the main
package and referenced. In reality we may need to copy some of this code
for reason stated in the **Roadblocks** section of this file.

Copy templates and javascript file from the current Airflow repository.
That means an effective lock on these files, or some change management.
Keep track of what can be simply copied as is vs what has to be modified to
work. This means that PRs on files that have been copied need to be held up
or manually synchronized in this new repository.

For views, try import the current views and wrap them in FAB-compatible
views. Otherwise, copy the code and somehow keep the repositories in sync.

### Roadblocks & Solution

#### Model incompatibilities

It appears as some of the more advanced *SQLAlchemy* features we use in
Airflow aren't supported by FAB:

- **Multi-field primary key**: solution here is to write DB migration to add
  and `id` field to all models that don't already have one, more specifically
  ``TaskInstance`` and add a unique constraint and btree index on the
  current PK
- **Column starting with ``_``**: somehow FAB doesn't seem to like

## Extras!

While we're doing this, there's the opportunity to improve other things.

- Javascript cleanup!
 - ``npm`` for package dependencies
 - ``webpack`` to minify files
 - ``eslint`` with a decent set of rules
