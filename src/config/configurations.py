from config.vector import Vector
from config.icon import Icon
from ingestion.splunk import Splunk
import os
from threading import Thread


class Configuration:

    __instance = None

    @staticmethod
    def get_instance():
        if Configuration.__instance == None:
            return Configuration()
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

        self.splunk = None

        Configuration.__instance = self

    def set_team(self, is_lead, lead_IP, established_connections):
        self.is_lead = is_lead
        self.lead_IP = lead_IP
        self.established_connections = established_connections

    def set_event(self, name, description, start_time, end_time):
        self.event_name = name
        self.event_description = description
        self.event_start = start_time
        self.event_end = end_time

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

        self.splunk = Splunk(self.root_files, self.red_files, self.blue_files, self.white_files)
        self.splunk.connect()
        Thread(target=self.splunk.start_ingestion()).start()

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
        self.vectors.append(new_icon)