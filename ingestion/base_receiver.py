from abc import ABC, abstractmethod

class BaseReceiver(ABC):
    """
    Base class for log ingestion modules.

    This abstract class defines a common interface and shared functionality
    for different types of log receivers (e.g., TCP, Kafka).

    """
    def __init__(self):
        pass

    @abstractmethod
    def start(self):
        """Start receiving data."""
        pass

    @abstractmethod
    def stop(self):
        """Stop receiving data."""
        pass

    @abstractmethod
    def handle_message(self, message: str):
        pass

