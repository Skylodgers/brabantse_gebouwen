# try:
#     from .archives.settings import *
# except ImportError:
#     pass


##################################################################
#
#  Local docker backends for
#
#    PostgreSQL + PostGIS
#    ElasticSearch
#
##################################################################

#
#  DB Config template, fields marked "Don't change!" should remain, unless
#  the corresponding changes to the docker-compose file is done
#
DATABASES = {
    "default": {
        "ATOMIC_REQUESTS": False,
        "AUTOCOMMIT": True,
        "CONN_MAX_AGE": 0,
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "HOST": "localhost",  # Don't change!
        "NAME": "brab_geb",  # <<<---  Make sure to change!
        "OPTIONS": {},
        "PASSWORD": "postgis",  # Don't change!
        "PORT": "5432",  # Don't change!
        "POSTGIS_TEMPLATE": "template_postgis",
        "TEST": {
            "CHARSET": None,
            "COLLATION": None,
            "MIRROR": None,
            "NAME": None,
        },
        "TIME_ZONE": None,
        "USER": "postgres",  # Don't change!
    }
}

#
#  Use local elasticsearch docker
#

ELASTICSEARCH_HOSTS = [
    {
        "scheme": "http",
        "host": "localhost",
        "port": 9200,
    }
]

ELASTICSEARCH_CONNECTION_OPTIONS = {
    "request_timeout": 30,
    "basic_auth": ("elastic", "E1asticSearchforArche5"),
}
