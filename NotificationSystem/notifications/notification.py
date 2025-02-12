from abc import ABC, abstractmethod
class Notification(ABC):
    @abstractmethod
    def validate_notification():
        pass
    
    @abstractmethod
    def send_notification():
        pass


