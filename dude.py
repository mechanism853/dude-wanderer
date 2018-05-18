#dude.py

##
# dude
#
# So far, the dude consists merely of an x and a y position, and an
# ascii character
##
class dude:
    def __init__(self, x: int, y: int, c: str):
        self.x = int(x)
        self.y = int(y)
        self.c = str(c)

    @staticmethod
    def deserialize(dude_bytes):
        x = int.from_bytes(dude_bytes[0:2], 'big')
        y = int.from_bytes(dude_bytes[2:4], 'big')
        c = str(dude_bytes[4:], 'utf-8')
        return(dude(x, y, c))

    @staticmethod
    def serialize(dude_object):
        dude_bytes = dude_object.x.to_bytes(2, 'big')
        dude_bytes += dude_object.y.to_bytes(2, 'big')
        dude_bytes += bytearray(dude_object.c, 'utf-8')
        return(dude_bytes)
