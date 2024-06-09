from typing import Literal

from pydantic import BaseModel, Field, computed_field, conint

from mahjong.constants import (
    DRAGON_TILE_NUMBER_MAP,
    FLOWER_TILE_NUMBER_MAP,
    SEASON_TILE_NUMBER_MAP,
    WIND_TILE_NUMBER_MAP,
    MahjongTileCategory,
)


class Tile(BaseModel):
    category: MahjongTileCategory
    number: conint(ge=1, le=9)

    @computed_field
    def abbreviation(self) -> str:
        match self.category:
            case MahjongTileCategory.CHARACTER:
                return f"{self.number}m"
            case MahjongTileCategory.CIRCLE:
                return f"{self.number}p"
            case MahjongTileCategory.BAMBOO:
                return f"{self.number}s"
            case MahjongTileCategory.WIND:
                return WIND_TILE_NUMBER_MAP[self.number][0]
            case MahjongTileCategory.DRAGON:
                return DRAGON_TILE_NUMBER_MAP[self.number][0]
            case MahjongTileCategory.SEASON:
                return SEASON_TILE_NUMBER_MAP[self.number][:2]
            case MahjongTileCategory.FLOWER:
                return FLOWER_TILE_NUMBER_MAP[self.number][:2]


class Hand(BaseModel):
    tiles: list[Tile] = Field(title="Tiles", description="List of tiles in hand.")


class EvaluateResult(BaseModel):
    dealer: bool = Field(False, title="Dealer", description="The player is dealer or not.")


class WinningResult(EvaluateResult):
    winning: Literal[True] = Field(title="Winning", description="You win this round.")
    self_draw: bool = Field(False, title="Self-Draw", description="Self-Draw or Chunk.")


class NonWinningResult(EvaluateResult):
    winning: Literal[False] = Field(False, title="Winning", description="Keep going.")
