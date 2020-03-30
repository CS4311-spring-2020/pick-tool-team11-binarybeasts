import splunklib.client as client
from ui.common import menu_bar
from config.configurations import Configuration
from config.configurations import ConfigurationsWindow
# or from ui.windows import ConfigurationsWindow

class Validate:

    def __init__(self):

    # Print installed apps to the console to verify login
    #for app in service.apps:
    #print (app.name)

    def start_ingestion(self):

    print("Starting Ingestion..")

    HOST = "localhost"
    PORT = 8089
    USERNAME = "pm511"
    PASSWORD = "binarybeasts"
    # Access scheme (default: https)
    scheme="https"
        # Your version of Splunk (default: 5.0)
    version=5.0

    # Create a Service instance and log in
    service = client.connect(
        host=HOST,
        port=PORT,
        username=USERNAME,
        password=PASSWORD)
    # Retrieve the index for the data
    logFiles = service.indexes["test_validate"]

    # Create a variable with the path and filename
    #ingest = "/Applications/Splunk/README-splunk.txt"
    ingest = r"C:\Users\ponyo\OneDrive\Desktop\hi.txt"

    # trying to automatically ingest this
    ingest = self.rootDirectory.text()

    print("Ingestion Complete!")
    # Upload and index the file
    logFiles.upload(ingest);
    print(logFiles)