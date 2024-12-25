# sql_queries.py

# Query to fetch all data from a table
FETCH_ALL_USER_DATA = "SELECT * FROM user_data;"

# Query to fetch top 10 handsets
TOP_10_HANDSETS = """
SELECT handset, COUNT(*) AS usage_count
FROM user_data
GROUP BY handset
ORDER BY usage_count DESC
LIMIT 10;
"""

# Query to fetch top 3 manufacturers
TOP_3_MANUFACTURERS = """
SELECT manufacturer, COUNT(*) AS device_count
FROM user_data
GROUP BY manufacturer
ORDER BY device_count DESC
LIMIT 3;
"""

# Query to fetch top 5 handsets per top 3 manufacturers
TOP_5_HANDSETS_PER_MANUFACTURER = """
WITH top_manufacturers AS (
    SELECT manufacturer
    FROM user_data
    GROUP BY manufacturer
    ORDER BY COUNT(*) DESC
    LIMIT 3
)
SELECT manufacturer, handset, COUNT(*) AS usage_count
FROM user_data
WHERE manufacturer IN (SELECT manufacturer FROM top_manufacturers)
GROUP BY manufacturer, handset
ORDER BY manufacturer, usage_count DESC
LIMIT 5;
"""
