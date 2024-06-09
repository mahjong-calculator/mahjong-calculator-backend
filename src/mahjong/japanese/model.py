from pydantic import Field, computed_field

from mahjong.base_model import Tile as BaseTile


class Tile(BaseTile):
    dora: bool = Field(False, title="Dora", description="The tile is dora or not.")

    @computed_field
    def abbreviation(self) -> str:
        return f"{super().abbreviation}{'d' if self.dora else ''}"
