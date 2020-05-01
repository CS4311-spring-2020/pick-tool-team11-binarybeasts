import os
from association.vector import Vector
from configuration.icon import Icon
from ingestion.splunk_interface import SplunkInterface
from threading import Thread
from configuration.database_writer import DatabaseWriter


class Configuration:

    __instance = None

    @staticmethod
    def get_instance():
        if Configuration.__instance == None:
            Configuration.__instance = Configuration()
        return Configuration.__instance

    def __init__(self):
        self.is_lead = False
        self.lead_IP = "0.0.0.0"
        self.established_connections = 0

        self.event_name = ""
        self.event_description = ""
        self.event_start = ""
        self.event_end = ""

        self.root_directory = ""
        self.red_directory = ""
        self.blue_directory = ""
        self.white_directory = ""

        self.vectors = []

        self.icons = []

        directories = DatabaseWriter.get_all_documents_in_collection(DatabaseWriter.COLLECTION_DIRECTORY)
        self.splunk = None
        if len(directories) != 0:
            document = directories[0]
            self.splunk = SplunkInterface(document["root_directory"], document["red_directory"], document["blue_directory"], document["white_directory"])
            self.splunk.connect()

        Configuration.__instance = self

    def set_team(self, is_Lead, lead_IP, established_connections):
        self.is_lead = is_Lead
        self.lead_IP = lead_IP
        self.established_connections = established_connections
        DatabaseWriter.write_dict_to_collection(self.get_team_dict(), DatabaseWriter.COLLECTION_TEAM)
        DatabaseWriter.print_collection(DatabaseWriter.COLLECTION_TEAM)

    def set_event(self, name, description, start_time, end_time):
        self.event_name = name
        self.event_description = description
        self.event_start = start_time
        self.event_end = end_time
        DatabaseWriter.write_dict_to_collection(self.get_event_dict(), DatabaseWriter.COLLECTION_EVENT)
        DatabaseWriter.print_collection(DatabaseWriter.COLLECTION_EVENT)

    def set_directories(self, root_dir, red_dir, blue_dir, white_dir):
        self.root_directory = root_dir
        self.red_directory = red_dir
        self.blue_directory = blue_dir
        self.white_directory = white_dir

        print("root files")
        self.root_files = self.get_filepaths_from_directory(root_dir)
        print(self.root_files)

        print("red files")
        self.red_files = self.get_filepaths_from_directory(red_dir)
        print(self.red_files)

        print("blue files")
        self.blue_files = self.get_filepaths_from_directory(blue_dir)
        print(self.blue_files)

        print("white files")
        self.white_files = self.get_filepaths_from_directory(white_dir)
        print(self.white_files)

        DatabaseWriter.write_dict_to_collection(self.get_directories_dict(), DatabaseWriter.COLLECTION_DIRECTORY)
        DatabaseWriter.print_collection(DatabaseWriter.COLLECTION_DIRECTORY)

        self.splunk = SplunkInterface(self.root_files, self.red_files, self.blue_files, self.white_files)
        self.splunk.connect()
        Thread(target=self.splunk.start_ingestion).start()

    def get_filepaths_from_directory(self, dir):
        file_paths = []
        if len(dir) == 0:
            return file_paths
        for path in os.listdir(dir):
            full_path = os.path.join(dir, path)
            if os.path.isfile(full_path):
                file_paths.append(full_path)
        return file_paths

    def add_vector(self, name, description):
        new_vector = Vector(name, description)
        self.vectors.append(new_vector)

    def add_icon(self, name, source):
        new_icon = Icon(name, source)
        self.icons.append(new_icon)

    def get_team_dict(self):
        return {"isLead": self.is_lead,
                "lead_IP": self.lead_IP,
                "established_connections": self.established_connections}

    def get_event_dict(self):
        return {"event_name": self.event_name,
                "event_description": self.event_description,
                "event_start": self.event_start,
                "event_end": self.event_end}

    def get_directories_dict(self):
        return {"root_directory": self.root_directory,
                "red_directory": self.red_directory,
                "blue_directory": self.blue_directory,
                "white_directory": self.white_directory}

    def get_list_of_vector_dicts(self):
        return [vector.get_dict() for vector in self.vectors]

    def get_list_of_icon_dicts(self):
        return [icon.get_dict() for icon in self.icons]
