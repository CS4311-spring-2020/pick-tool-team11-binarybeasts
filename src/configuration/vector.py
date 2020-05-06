from ingestion.logentry import LogEntry
from configuration.database_writer import DatabaseWriter


class Vector:

    def __init__(self, name, description, log_entries=None):
        if log_entries is None:
            self.log_entries = []
        else:
            self.log_entries = None
        self.name = name
        self.description = description

    def add_log_entry(self, log_entry: LogEntry):
        self.log_entries.append(log_entry)
        # TODO Add log entry to database

    def get_dict(self):
        return {"name": self.name,
                "description": self.description,
                "log_entries": [log_entry.to_dict() for log_entry in self.log_entries]}
