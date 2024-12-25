import pandas as pd
from sqlalchemy import create_engine

# Database credentials
DB_HOST = "locahost"
DB_NAME = "telecom_data"
DB_USER = "postgres"
DB_PASSWORD = "aman"

# Connect to the PostgreSQL database
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")

# SQL query to extract data
query = """
SELECT * FROM xdr_records;  -- Replace 'xdr_records' with the actual table name
"""

# Load data into a Pandas DataFrame
df = pd.read_sql(query, engine)

# Save the data locally for reuse
df.to_csv("xdr_data.csv", index=False)

print("Data extracted successfully!")
