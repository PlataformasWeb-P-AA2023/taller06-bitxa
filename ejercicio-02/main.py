from data_insertion import insertAllData
import queries

if __name__ == "__main__":
    # Comment insertAllData to avoid uploading data again
    insertAllData()
    # queries.run_queries_with_postgres()
    queries.run_queries_with_sqlite()
