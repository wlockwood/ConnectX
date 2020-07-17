from collections import namedtuple

# Define the coord named tuple. Basically a micro-class
Coord = namedtuple("Coord", "x y")
Coord.__str__ = lambda self: f"({self.x},{self.y})"

# Define transforms to happen in each direction
dir_dict = {}
# Cardinal directions
dir_dict["up"]         = lambda ic,a=1: Coord(ic.x, ic.y + a)
dir_dict["down"]       = lambda ic,a=1: Coord(ic.x, ic.y - a)
dir_dict["left"]       = lambda ic,a=1: Coord(ic.x - a, ic.y)
dir_dict["right"]      = lambda ic,a=1: Coord(ic.x + a, ic.y)

# Hardcoded diagonals
dir_dict["up-left"]    = lambda ic,a=1: Coord(ic.x - a, ic.y + a)
dir_dict["up-right"]   = lambda ic,a=1: Coord(ic.x + a, ic.y + a)
dir_dict["down-left"]  = lambda ic,a=1: Coord(ic.x - a, ic.y - a)
dir_dict["down-right"] = lambda ic,a=1: Coord(ic.x + a, ic.y - a)

def get_directions():
    return dir_dict.keys()

def translate(origin: Coord, direction: str, amount: int):
    return dir_dict[direction](origin, amount)

def simple_translate(ox, oy, direction: str, amount: int):
    origin = Coord(ox, oy)
    return dir_dict[direction](origin, amount)

#Overly-complex invocation example
def demo_directions():
    longest_dir_name_len = max([len(x) for x in dir_dict.keys()])
    origin = Coord(0, 0)
    for k, v in dir_dict.items():
        key_string = "{k:>{ldn}}".format(k=k, ldn=longest_dir_name_len)
        print(f"{key_string} from {origin}: {v(origin)}")