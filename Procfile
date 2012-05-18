web: newrelic-admin run-program twistd --reactor=epoll web --port=tcp:$PORT:interface=localhost --wsgi wsgi.twisted_application
scheduler: python manage.py celeryd -B -E --maxtasksperchild=1000
worker: python manage.py celeryd -E --maxtasksperchild=1000
