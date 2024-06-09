from abc import ABC, abstractmethod

from mahjong.base_model import Hand, Tile


class BaseHandler(ABC):

    def __init__(self):
        self._available_tiles: list[Tile] = []
        self._current_hand: Hand | None = None

        self.generate_full_tiles()

    def get_available_tiles(self) -> list[Tile]:
        return self._available_tiles.copy()

    @abstractmethod
    def generate_full_tiles(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def evaluate_mahjong_hand(self, hand: Hand):
        raise NotImplementedError

    @abstractmethod
    def calculate_score(self):
        raise NotImplementedError
