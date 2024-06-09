from enum import StrEnum


class MahjongTileCategory(StrEnum):
    CHARACTER = "Character"
    CIRCLE = "Circle"
    BAMBOO = "Bamboo"
    WIND = "Wind"
    DRAGON = "Dragon"
    FLOWER = "Flower"
    SEASON = "Season"


WIND_TILE_NUMBER_MAP = {1: "East", 2: "South", 3: "West", 4: "North"}
DRAGON_TILE_NUMBER_MAP = {1: "Red", 2: "Green", 3: "White"}
FLOWER_TILE_NUMBER_MAP = {1: "Plum", 2: "Orchid", 3: "Bamboo", 4: "Chrysanthemum"}
SEASON_TILE_NUMBER_MAP = {1: "Spring", 2: "Summer", 3: "Autumn", 4: "Winter"}
