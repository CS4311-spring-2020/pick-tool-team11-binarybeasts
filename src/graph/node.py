from ingestion.logentry import LogEntry
from configuration.icon import Icon


class Node:

    def __init__(self, id, name, log_entry, icon = None):
        self.id = id
        self.name = name
        self.log_entry = log_entry
        self.icon = icon

    def set_details(self, id, name, log_entry, icon = None):
        self.id = id
        self.name = name
        self.log_entry = log_entry
        self.icon = icon

    def get_name(self):
        return self.name

    def get_log_entry(self):
        return self.log_entry

    def get_icon(self):
        return self.icon
