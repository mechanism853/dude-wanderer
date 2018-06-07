##
# dude
#
# So far, the dude consists merely of an x and a y position, and an
# ascii character
##
class dude:

    WORLD_DIM_NS = 15
    WORLD_DIM_WE = 25

    def __init__(self, x: int, y: int, c: str):
        self.x = int(x)
        self.y = int(y)
        self.c = str(c)

    @staticmethod
    def deserialize(dude_bytes: bytearray) -> 'dude':
        x = int.from_bytes(dude_bytes[0:2], 'big')
        y = int.from_bytes(dude_bytes[2:4], 'big')
        c = str(dude_bytes[4:], 'utf-8')
        return(dude(x, y, c))

    @staticmethod
    def serialize(dude_object: 'dude') -> bytearray:
        dude_bytes = dude_object.x.to_bytes(2, 'big')
        dude_bytes += dude_object.y.to_bytes(2, 'big')
        dude_bytes += bytearray(dude_object.c, 'utf-8')
        return(dude_bytes)

    def move_north(self) -> None:
        self.y = (self.y - 1) % self.WORLD_DIM_NS

    def move_south(self) -> None:
        self.y = (self.y + 1) % self.WORLD_DIM_NS

    def move_west(self) -> None:
        self.x = (self.x - 1) % self.WORLD_DIM_WE

    def move_east(self) -> None:
        self.x = (self.x + 1) % self.WORLD_DIM_WE

    def as_string(self) -> str:
        return "({} at {}, {})".format(self.c, self.x, self.y)
