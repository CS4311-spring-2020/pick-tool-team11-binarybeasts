class LogEntry:

    def __init__(self, id, data, time, source_index, source_file, source_type):
        self.id = id
        self.data = data
        self.time = time
        self.source_index = source_index
        self.source_file = source_file
        self.source_type = source_type

    def print(self):
        print("id: '%s', data: '%s', time: '%s', source_index: '%s', source_file: '%s', source_type: '%s'" %
              (self.id, self.data, self.time, self.source_index, self.source_file, self.source_type))

    def to_dict(self):
        return {"_id": self.id,
                "data": self.data,
                "time": self.time,
                "source_index": self.source_index,
                "source_file": self.source_file,
                "source_type": self.source_type}
