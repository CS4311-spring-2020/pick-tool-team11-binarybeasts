class Icon:

    def __init__(self, name, source):
        self.name = name
        self.source = source

    def get_dict(self):
        return {"name": self.name,
                "source": self.source}