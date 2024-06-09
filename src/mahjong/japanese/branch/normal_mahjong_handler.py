from mahjong.constants import MahjongTileCategory
from mahjong.japanese.handler import JapaneseMahjongHandler
from mahjong.japanese.model import Tile


class NormalJapaneseMahjongHandler(JapaneseMahjongHandler):

    def generate_full_tiles(self) -> None:
        self._available_tiles = [
            *[
                Tile(category=MahjongTileCategory.CHARACTER, number=i, dora=True if i == 5 and j == 1 else False)
                for i in range(1, 10)
                for j in range(4)
            ],
            *[
                Tile(category=MahjongTileCategory.CIRCLE, number=i, dora=True if i == 5 and j == 1 else False)
                for i in range(1, 10)
                for j in range(4)
            ],
            *[
                Tile(category=MahjongTileCategory.BAMBOO, number=i, dora=True if i == 5 and j == 1 else False)
                for i in range(1, 10)
                for j in range(4)
            ],
            *[Tile(category=MahjongTileCategory.WIND, number=i) for i in range(1, 5) for _ in range(4)],
            *[Tile(category=MahjongTileCategory.DRAGON, number=i) for i in range(1, 4) for _ in range(4)],
        ]

    def calculate_score(self):
        pass
