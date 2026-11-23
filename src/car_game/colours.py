from dataclasses import dataclass
from enum import Enum

RGB = tuple[int, int, int]


class Palette(Enum):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREY = (128, 128, 128)
    DARK_GREEN = (45, 89, 32)
    CRIMSON = (220, 20, 60)


@dataclass(frozen=True)
class Theme:
    background: RGB = Palette.DARK_GREEN.value
    road: RGB = Palette.GREY.value
    lane_line: RGB = Palette.WHITE.value
    border: RGB = Palette.BLACK.value
    text: RGB = Palette.BLACK.value
    text_background: RGB = Palette.WHITE.value