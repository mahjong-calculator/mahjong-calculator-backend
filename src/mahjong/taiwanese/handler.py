from mahjong.base_handler import BaseHandler
from mahjong.base_model import Hand
from mahjong.constants import MahjongTileCategory
from mahjong.taiwanese.model import Tile


class TaiwaneseMahjongHandler(BaseHandler):
    def generate_full_tiles(self) -> None:
        self._available_tiles = [
            *[Tile(category=MahjongTileCategory.CHARACTER, number=i) for i in range(1, 10) for _ in range(4)],
            *[Tile(category=MahjongTileCategory.CIRCLE, number=i) for i in range(1, 10) for _ in range(4)],
            *[Tile(category=MahjongTileCategory.BAMBOO, number=i) for i in range(1, 10) for _ in range(4)],
            *[Tile(category=MahjongTileCategory.WIND, number=i) for i in range(1, 5) for _ in range(4)],
            *[Tile(category=MahjongTileCategory.DRAGON, number=i) for i in range(1, 4) for _ in range(4)],
            *[Tile(category=MahjongTileCategory.SEASON, number=i) for i in range(1, 4)],
            *[Tile(category=MahjongTileCategory.FLOWER, number=i) for i in range(1, 4)],
        ]

    def evaluate_mahjong_hand(self, hand: Hand):
        pass

    def calculate_score(self):
        pass
