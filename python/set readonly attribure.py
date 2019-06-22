class Foo(object):
    def __init__(self):
        self.readonly = set()

    def set_readonly(self, attr, value):
        setattr(self, attr, value)
        self.readonly.add(attr)

    def __setattr__(self, attr, value):
        if hasattr(self, "readonly") and attr in self.readonly:
            raise AttributeError("Read only attribute: %s" % (attr,))
        object.__setattr__(self, attr, value)


# f = Foo()
# f.x = 5
# f.set_readonly("y", 9)
# f.x, f.y
# f.x = 7
# f.y = 1
