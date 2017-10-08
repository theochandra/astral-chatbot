
class DictToObj(object):

    def __init__(self, dictionary):
        # self.__dict__ = dictionary
        # for dict in dictionary:
        for key in dictionary:
            setattr(self, key, dictionary[key])

    def __repr__(self):
        return "<obj: %s>" % self.__dict__
