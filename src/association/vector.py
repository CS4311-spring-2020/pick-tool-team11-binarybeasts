from ingestion.logentry import LogEntry

class Vector:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.log_entries = []

    def add_log_entry(self, log_entry: LogEntry):
        self.log_entries.append(log_entry)

    def get_dict(self):
        return {"name": self.name,
                "description": self.description,
                'log_entries': [{"_id": log_entry.id,
                                 "data": log_entry.data,
                                 "time": log_entry.time,
                                 "source_index": log_entry.source_index,
                                 "source_file": log_entry.source_file,
                                 "source_type": log_entry.source_type}
                                for log_entry in self.log_entries]}
