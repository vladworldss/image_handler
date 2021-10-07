import os
import sys


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(PROJECT_ROOT, 'logs')

BIGINT_MAX_VALUE = sys.maxsize
BIGINT_MIN_VALUE = -1 * sys.maxsize - 1
LOG_LEVEL = 'DEBUG'

# DB SECTION
DB_CONNECTION = 'postgresql+psycopg2://image_handler:image_handler@db/image_handler'
# DB_CONNECTION = 'postgresql+psycopg2://billing:billing@localhost:6432/billing'
TESTING_DB_CONNECTION = 'postgresql+psycopg2://image_handler:image_handler@localhost:6433/image_handler'
DB_CONNECTION_YOYO = DB_CONNECTION.replace('+psycopg2', '')
TESTING_DB_CONNECTION_YOYO = TESTING_DB_CONNECTION.replace('+psycopg2', '')


# BACKEND ROUTES
IMAGE_SOURCE_ROUTE = '/images/{image_id}'
