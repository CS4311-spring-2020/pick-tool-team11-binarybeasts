class Vector:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.log_entries = []

    def add_log_entry(self, log_entry):
        self.log_entries.append(log_entry)
