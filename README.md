# Week-2

# Telecom Data Processing

This project processes telecom xDR records from a PostgreSQL database for data analysis and insights. It includes scripts for data loading, querying, and transforming data to prepare it for downstream analytics.

## Project Structure

```
.
├── notebook/
│   └── postgres_load.ipynb      # Jupyter notebook for PostgreSQL data loading and analysis
├── scripts/
│   ├── load_data.py             # Script to restore and load data into PostgreSQL
│   ├── sql_queries.py           # SQL queries for data extraction and transformation
├── tests/
│   ├── __init__.py              # Initialization file for test modules
│   └── test_load_data.py        # Unit tests for the load_data.py script
├── telecom.sql                  # PostgreSQL database dump file
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
└── LICENSE                      # License information
```

## Setup Instructions

1. **Restore the Database**  
   Ensure PostgreSQL is installed and set up:
   ```bash
   psql -U <username> -d <dbname> -f telecom.sql
   ```

2. **Install Dependencies**  
   Install required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Scripts**  
   Use the provided scripts for loading and querying data:
   - `load_data.py`: Restores and loads data into PostgreSQL.
   - `sql_queries.py`: Contains SQL queries for processing data.

4. **Explore Data**  
   Open the Jupyter notebook (`postgres_load.ipynb`) for interactive exploration.

5. **Run Tests**  
   Use `pytest` to ensure code quality:
   ```bash
   pytest tests/
   ```

## Requirements

- Python 3.8+
- PostgreSQL 12+
- Python libraries listed in `requirements.txt`

## Contributing

Feel free to raise issues or submit pull requests for improvements.

## License

This project is open source and available under the [MIT License](LICENSE).
```
