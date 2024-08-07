try:
    from .brabantse_gebouwen.settings import *
except ImportError:
    pass


ELASTICSEARCH_HOSTS = [{"scheme": "http", "host": "localhost", "port": 9200}]
GDAL_LIBRARY_PATH = '/opt/homebrew/opt/gdal/lib/libgdal.dylib'
GEOS_LIBRARY_PATH = '/opt/homebrew/opt/geos/lib/libgeos_c.dylib'