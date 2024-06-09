from abc import ABC, abstractmethod


class BaseController(ABC):

    @classmethod
    @abstractmethod
    def run(cls, *args, **kwargs):
        raise NotImplementedError
