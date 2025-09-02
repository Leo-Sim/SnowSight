
from config import Config

class LoadInformation:
    """
    This class defines required information for loading data to data warehouse
    """

    def __init__(self):
        config = Config()

        self.user_id = config.get_user_id()
        self.password = config.get_password()
        self.account = config.get_account()
        self.batch_size = config.get_batch_size()
        self.database_name = config.get_database_name()
        self.schema_name = config.get_schema_name()
        self.table_name = config.get_table_name()
        self.common_fields = config.get_common_fields()

