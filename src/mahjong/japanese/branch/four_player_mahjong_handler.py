from mahjong.constants import MahjongTileCategory
from mahjong.japanese.handler import JapaneseMahjongHandler
from mahjong.japanese.model import Tile


class FourPlayerJapaneseMahjongHandler(JapaneseMahjongHandler):

    def generate_full_tiles(self) -> None:
        self._available_tiles = []
        self._available_tiles_counter = []
        # Character
        self._available_tiles += (
            [Tile(category=MahjongTileCategory.CHARACTER, number=i) for i in range(1, 6)]
            + [Tile(category=MahjongTileCategory.CHARACTER, number=5, dora=True)]
            + [Tile(category=MahjongTileCategory.CHARACTER, number=i) for i in range(6, 10)]
        )
        self._available_tiles_counter += [4 for _ in range(1, 5)] + [3, 1] + [4 for _ in range(6, 10)]
        # Circle
        self._available_tiles += (
            [Tile(category=MahjongTileCategory.CIRCLE, number=i) for i in range(1, 6)]
            + [Tile(category=MahjongTileCategory.CIRCLE, number=5, dora=True)]
            + [Tile(category=MahjongTileCategory.CIRCLE, number=i) for i in range(6, 10)]
        )
        self._available_tiles_counter += [4 for _ in range(1, 5)] + [3, 1] + [4 for _ in range(6, 10)]
        # Bamboo
        self._available_tiles += (
            [Tile(category=MahjongTileCategory.BAMBOO, number=i) for i in range(1, 6)]
            + [Tile(category=MahjongTileCategory.BAMBOO, number=5, dora=True)]
            + [Tile(category=MahjongTileCategory.BAMBOO, number=i) for i in range(6, 10)]
        )
        self._available_tiles_counter += [4 for _ in range(1, 5)] + [3, 1] + [4 for _ in range(6, 10)]
        # Wind
        wind_tiles = [Tile(category=MahjongTileCategory.WIND, number=i) for i in range(1, 5)]
        self._available_tiles += wind_tiles
        self._available_tiles_counter += [4] * len(wind_tiles)
        # Dragon
        dragon_tiles = [Tile(category=MahjongTileCategory.DRAGON, number=i) for i in range(1, 4)]
        self._available_tiles += dragon_tiles
        self._available_tiles_counter += [4] * len(dragon_tiles)

    def calculate_score(self):
        pass
