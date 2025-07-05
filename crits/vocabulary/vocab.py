import six
class vocab(object):
    """
    Base CRITs vocabulary object. Does nothing right now.
    """

    @classmethod
    def values(cls, sort=False):
        """
        Get available values in a list.

        :param sort: Should the list be sorted.
        :type sort: bool
        :returns: list
        """

        l = []
        for k,v in six.iteritems(cls.__dict__):
            if ('__' not in k and
                isinstance(v, six.string_types) and
                '__' not in v and
                'vocabulary' not in v):
                l.append(v)
        if sort:
            l.sort()
        return l
