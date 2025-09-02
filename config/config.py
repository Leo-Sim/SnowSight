import yaml
import os


class Config:
    def __init__(self, config_path=None):

        if config_path is None:

            current_dir = os.path.dirname(os.path.abspath(__file__))
            config_path = os.path.join(current_dir, "../config.yaml")

        self.config_path = config_path
        self.config = self._load_yaml()

        self.config_path = config_path
        self.config = self._load_yaml()

    def _load_yaml(self):
        with open(self.config_path, "r") as file:
            try:
                config = yaml.safe_load(file)
                return config
            except yaml.YAMLError as e:
                print(f"Error loading YAML file: {e}")
                return {}

    def _get_receiver(self):
        return self.config.get("receiver")
    def get_is_kafka(self):
        return self._get_receiver()["is-kafka"]
    def get_kafka_ip(self):
        return self._get_receiver()["kafka-ip"]
    def get_inbound_port(self):
        return self._get_receiver()["port"]

    def get_kafka_topic(self):
        return self._get_receiver()["topic"]

    def _get_loader(self):
        return self.config.get("loader")
    def get_batch_size(self):
        return self._get_loader()["batch-size"]

    def get_database_name(self):
        return self._get_loader()["database-name"]

    def get_schema_name(self):
        return self._get_loader()["schema-name"]

    def get_table_name(self):
        return self._get_loader()["table-name"]

    def get_common_fields(self):
        return self._get_loader()["common-fields"]

    def get_user_id(self):
        return self._get_loader()["user-id"]

    def get_password(self):
        return self._get_loader()["password"]

    def get_account(self):
        return self._get_loader()["account"]

