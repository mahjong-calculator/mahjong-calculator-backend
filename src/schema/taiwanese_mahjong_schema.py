from typing import Literal

from pydantic import BaseModel

from constants import MahjongType


class TaiwaneseMahjongSchema(BaseModel):
    mahjong_type: Literal[MahjongType.TAIWANESE]
