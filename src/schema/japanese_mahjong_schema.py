from typing import Literal

from pydantic import BaseModel

from constants import MahjongType
from mahjong.japanese.constants import JapaneseMahjongBranch


class JapaneseMahjongSchema(BaseModel):
    mahjong_type: Literal[MahjongType.JAPANESE]
    mahjong_branch: JapaneseMahjongBranch
