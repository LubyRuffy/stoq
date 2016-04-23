## Broker settings.
BROKER_URL = 'amqp://guest:guest@localhost:5672//'

# List of modules to import when celery starts.
CELERY_IMPORTS = ('StoCelery.tasks',)

## Using the database to store task state and results.
CELERY_RESULT_BACKEND = 'db+postgresql://stoq:stoq-password@127.0.0.1/stoq'
