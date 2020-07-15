from collections import namedtuple

# Define the coord named tuple. Basically a micro-class
Coord = namedtuple("Coord", "x y")
Coord.__str__ = lambda self: f"({self.x},{self.y})"

# Define transforms to happen in each direction
dir_dict = {}
# Cardinal directions
dir_dict["up"]         = lambda ic: Coord(ic.x, ic.y + 1)
dir_dict["down"]       = lambda ic: Coord(ic.x, ic.y - 1)
dir_dict["left"]       = lambda ic: Coord(ic.x - 1, ic.y)
dir_dict["right"]      = lambda ic: Coord(ic.x + 1, ic.y)

# Hardcoded diagonals
dir_dict["up-left"]    = lambda ic: Coord(ic.x - 1, ic.y + 1)
dir_dict["up-right"]   = lambda ic: Coord(ic.x + 1, ic.y - 1)
dir_dict["down-left"]  = lambda ic: Coord(ic.x - 1, ic.y - 1)
dir_dict["down-right"] = lambda ic: Coord(ic.x + 1, ic.y - 1)

# Overly complex diagonals
dir_dict["up-left"]    = lambda ic: dir_dict["up"](dir_dict["left"](ic))
dir_dict["up-right"]   = lambda ic: dir_dict["up"](dir_dict["right"](ic))
dir_dict["down-left"]  = lambda ic: dir_dict["down"](dir_dict["left"](ic))
dir_dict["down-right"] = lambda ic: dir_dict["down"](dir_dict["right"](ic))

longest_dir_name_len = max([len(x) for x in dir_dict.keys()])
origin = Coord(0, 0)
for k, v in dir_dict.items():
    key_string = "{k:>{ldn}}".format(k=k, ldn=longest_dir_name_len)
    print(f"{key_string} from {origin}: {v(origin)}")