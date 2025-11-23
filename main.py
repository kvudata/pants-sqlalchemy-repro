# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pybigquery==0.5.0",
#     "sqlalchemy==1.3.22",
# ]
# ///


from sqlalchemy import create_engine
import pybigquery


create_engine("bigquery://test-project")


