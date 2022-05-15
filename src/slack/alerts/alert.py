from abc import ABC


class Alert(ABC):

    def get_dict(self) -> dict:
        pass
