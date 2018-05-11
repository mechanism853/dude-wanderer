#dude.py

#imports?

##
# dude
#
# So far, the dude consists merely of an x and a y position, and an
# ascii character
##
#dude class definition
#TODO: Define dude in seperate file and import in both server and client. This helps keep any changes in sync if nothing else.
class dude:
    def __init__(self, *args):
        if len(args) == 1:
            # case for generating dude from serialized dude
            dude_bytes = args[0]
            self.x = int.from_bytes(dude_bytes[0:2])
            self.y = int.from_bytes(dude_bytes[2:4])
            self.c = str(dude_bytes[4:], 'utf-8')
        elif len(args) == 3:
            # case for generating dude from non-serialized dude parts
            #TODO: Fix these args[#]
            self.x = x_pos
            self.y = y_pos
            self.c = c_type
        else:
            #TODO: THROW TANTRUM
            #TODO: Actually add something here so it works ;)
            self = 0

    def serialize(self):
        return self.x.to_bytes(2, 'big') + self.y.to_bytes(2, 'big') + bytearray(self.c, 'utf-8')


