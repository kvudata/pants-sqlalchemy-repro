
from sqlalchemy import create_engine
import pybigquery


def test_engine_init():
    create_engine("bigquery://test-project")

