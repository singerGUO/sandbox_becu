import os
import uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import subprocess

import datetime

# Get tomorrow's date
tomorrow = datetime.date.today() + datetime.timedelta(days=1)

# Run a shell command and capture its output
generate_sas_command = f"az storage container generate-sas --account-name cs410032001efeadade --name example --permissions acdlrw --expiry {tomorrow.strftime('%Y-%m-%d')} --auth-mode login --as-user"
output = subprocess.check_output(generate_sas_command, shell=True)
print(output.decode())

file_path = "./uploads/network_traffic.pcap"
token = output.decode().strip().replace("\"", "")
url = f"\"https://cs410032001efeadade.blob.core.windows.net/example/?{token}\""
print(url)
azcopy_command = f"./azcopy copy {file_path} {url}"
print(azcopy_command)
output = subprocess.check_output(azcopy_command, shell=True)
print(output.decode())
