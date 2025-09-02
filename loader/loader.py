
from loader import LoadInformation
from snowflake.connector.pandas_tools import write_pandas
import snowflake.connector
import pandas as pd

class Loader:
    def __init__(self, config: LoadInformation):

        self.config = config

        self.conn = snowflake.connector.connect(
            user = config.user_id,
            password = config.password,
            account = config.account,
        )
        self.cs = self.conn.cursor()

        self.is_ready = self.db_schema_table_exists()

        if not self.is_ready:
            print("[Error] Check if Database, Schema, and Table exist")
        else:
            self.cs.execute(f"USE DATABASE {config.database_name}")
            self.cs.execute(f"USE SCHEMA {config.schema_name}")
            print("[Info] Database, Schema and Table are found in Snowflake")

    def db_schema_table_exists(self) -> bool:
        """
            This function checks if the database and schema exists.
        :return:
        """
        db_name = self.config.database_name
        schema_name = self.config.schema_name
        table_name = self.config.table_name

        self.cs.execute(f"""
            SELECT database_name 
            FROM snowflake.information_schema.databases
            WHERE database_name = '{db_name.upper()}'
        """)
        db_row = self.cs.fetchone()

        if not db_row:
            return False

        self.cs.execute(f"""
            SELECT schema_name
            FROM {db_name}.information_schema.schemata
            WHERE schema_name = '{schema_name.upper()}'
        """)
        schema_row = self.cs.fetchone()
        if not schema_row:
            return False

        self.cs.execute(f"""
                  SELECT 1
                  FROM {db_name}.information_schema.tables
                  WHERE table_schema = '{schema_name.upper()}'
                    AND table_name = '{table_name.upper()}'
              """)
        table_row = self.cs.fetchone()
        if not table_row:
            return False

        return True



    def load_data(self, df: pd.DataFrame):
        if self.is_ready:
            success, nchunks, nrows, _ = write_pandas(self.conn, df, self.config.table_name,
                                                      database=self.config.database_name, schema=self.config.schema_name)
            print(f"[info] Upload Status={success}, Number of lows uploaded수={nrows}")



if __name__ == '__main__':
    loader = Loader()
