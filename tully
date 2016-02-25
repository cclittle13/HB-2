"""Yoga pose types.

This provides a Pose class, helper methods to get all poses, find a
pose by id.

It reads pose data in from a text file.
"""
class Pose(object):
    """All poses."""

    def __init__(self,
                 id,
                 common_name,
                 sanskrit_name,
                 breathe,
                 image_url,
                 category,
                 random,
                 ):
        self.id = id
        self.common_name = common_name
        self.sanskrit_name = sanskrit_name
        self.breathe = breathe
        self.image_url = image_url
        self.category = category
        self.random = random

# class Melon(object):
#     """An Ubermelon Melon type."""

#     def __init__(self,
#                  id,
#                  melon_type,
#                  common_name,
#                  price,
#                  image_url,
#                  color,
#                  seedless,
#                  ):
#         self.id = id
#         self.melon_type = melon_type
#         self.common_name = common_name
#         self.price = price
#         self.image_url = image_url
#         self.color = color
#         self.seedless = seedless

    # def price_str(self):
    #     """Return price formatted as string $x.xx"""

    #     return "$%.2f" % self.price

    # def __repr__(self):
    #     """Convenience method to show information about melon in console."""

    #     return "<Melon: %s, %s, %s>" % (
    #         self.id, self.common_name, self.price_str())


def read_pose_types_from_file(filepath):
    """Read pose type data and populate dictionary of pose types.

    Dictionary will be {id: Pose object}
    """

    pose_types = {}

    for line in open(filepath):
        (id,
         common_name,
         sanskrit_name,
         breathe,
         img_url,
         category,
         random) = line.strip().split("|")

        id = int(id)
        # price = float(price)

        # For seedless, we want to turn "1" => True, otherwise False
        random = (random == "1")

        pose_types[id] = Pose(id,
                                common_name,
                                sanskrit_name,
                                breathe,
                                img_url,
                                category,
                                random)

    return pose_types


def get_all():
    """Return list of poses."""

    # This relies on access to the global dictionary `melon_types`

    return pose_types.values()


def get_by_id(id):
    """Return a pose, given its ID."""

    # This relies on access to the global dictionary `melon_types`

    return pose_types[id]


# Dictionary to hold types of melons.
#
# Format is {id: Melon object, ... }

pose_types = read_pose_types_from_file("poses.txt")