class Icon:

    def __init__(self, name, source):
        self.name = name
        self.source = source

    def set_name(self, name):
        self.name = name

    def set_source(self, source):
        self.source = source

    def get_name(self):
        return self.name

    def get_source(self):
        return self.source

    def get_dict(self):
        return {"name": self.name,
                "source": self.source}