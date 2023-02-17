#!/usr/bin/env python3
import boto3
import logging
import subprocess

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client("s3")

def upload_to_s3(file_path, bucket_name, object_name):
    try:
        s3.upload_file(file_path, bucket_name, object_name)
        logging.info("Upload Successful")
        return True
    except Exception as e:
        logging.error(e)
        return False

def capture_process_logs_by_iterations():
    try:
        process_logs = subprocess.check_output(["top", "-b", "-n", "5"])
        with open("process.log", "wb") as f:
            f.write(process_logs)
        return True
    except Exception as e:
        logging.error(e)
        return False

def capture_network_sniffer_logs():
    try:
        network_sniffer_logs = subprocess.check_output(["tcpdump", "-c", "10"])
        with open("network_sniffer.log", "wb") as f:
            f.write(network_sniffer_logs)
        return True
    except Exception as e:
        logging.error(e)
        return False

if __name__ == "__main__":
    s3_bucket_name = "my-log-bucket-becu"
    s3_object_name_process = "logs/process.log"
    s3_object_name_network_sniffer = "logs/network_sniffer.log"

    logging.info("Starting to capture process logs")
    if capture_process_logs_by_iterations():
        logging.info("Process logs captured successfully")
        upload_to_s3("process.log", s3_bucket_name, s3_object_name_process)
    else:
        logging.error("Failed to capture process logs")

    logging.info("Starting to capture network sniffer logs")
    if capture_network_sniffer_logs():
        logging.info("Network sniffer logs captured successfully")
        upload_to_s3("network_sniffer.log", s3_bucket_name, s3_object_name_network_sniffer)
    else:
        logging.error("Failed to capture network sniffer logs")
