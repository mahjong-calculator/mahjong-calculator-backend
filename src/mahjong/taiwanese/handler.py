from mahjong.base_handler import BaseHandler
from mahjong.base_model import Hand
from mahjong.constants import MahjongTileCategory
from mahjong.taiwanese.model import Tile


class TaiwaneseMahjongHandler(BaseHandler):
    def generate_full_tiles(self) -> None:
        self._available_tiles = []
        # Character
        self._available_tiles += [Tile(category=MahjongTileCategory.CHARACTER, number=i) for i in range(1, 10)]
        # Circle
        self._available_tiles += [Tile(category=MahjongTileCategory.CIRCLE, number=i) for i in range(1, 10)]
        # Bamboo
        self._available_tiles += [Tile(category=MahjongTileCategory.BAMBOO, number=i) for i in range(1, 10)]
        # Wind
        self._available_tiles += [Tile(category=MahjongTileCategory.WIND, number=i) for i in range(1, 5)]
        # Dragon
        self._available_tiles += [Tile(category=MahjongTileCategory.DRAGON, number=i) for i in range(1, 4)]
        # Season
        self._available_tiles += [Tile(category=MahjongTileCategory.SEASON, number=i) for i in range(1, 5)]
        # Flower
        self._available_tiles += [Tile(category=MahjongTileCategory.FLOWER, number=i) for i in range(1, 5)]

        self._available_tiles_counter = [4] * (len(self._available_tiles) - 8) + [1] * 8

    def evaluate_mahjong_hand(self, hand: Hand):
        pass

    def calculate_score(self):
        pass
