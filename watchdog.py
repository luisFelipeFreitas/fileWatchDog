import os
import time
import shutil
import logging
import sys

def start_logging(log_file):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ])

def watch_dog(interval,source,replica):
    while True:
        try:
            # Add new files and delete removed files.
            sync_folders(source, replica)
            
            
            
            # Add information to the log
            
            print("Sync happened.")
            time.sleep(interval)
        except KeyboardInterrupt:
            print("Synchronization stopped.") 
            return 

def sync_folders(source, replica):
    source_files = {}
    replica_files = {}
    
    
    # Adds all files in the source path to a source dictionary structured as: {Path : fileName} 
    for root, _, files in os.walk(source):
        for file in files:
            relative_path = os.path.relpath(os.path.join(root, file), source)
            source_files[relative_path] = os.path.join(root, file)
    
    # Adds all files in the replica path to a replica dictionary structured as: {Path : fileName} 
    for root, _, files in os.walk(replica):
        for file in files:
            relative_path = os.path.relpath(os.path.join(root, file), replica)
            replica_files[relative_path] = os.path.join(root, file)
            
    for relative_path, src_path in source_files.items():
        replica_path = os.path.join(replica, relative_path)
        # For every file in the source_files dictionary, check if it exists in replica or, if it's modification time is newer than the replica's
        if (relative_path not in replica_files or not os.path.exists(replica_path) or os.path.getmtime(src_path) > os.path.getmtime(replica_path)):
            
            # Copies the files and creates folder if necessary
            os.makedirs(os.path.dirname(replica_path), exist_ok=True)
            shutil.copy2(src_path, replica_path)
            logging.info(f"Copied file: {src_path} to {replica_path}")
    
    for relative_path, replica_path in replica_files.items():
        if (relative_path not in source_files):
            os.remove(replica_path)
            logging.info(f"Removed file: {replica_path}")


start_logging("log.txt")
if( len(sys.argv) < 4):
    print("This program needs at least three arguments to be executed. They are in order, update time, original folder and replica folder")
    exit(1)

interval = int(sys.argv[1])
source_folder = sys.argv[2]
replica_folder = sys.argv[3]

watch_dog(interval, source_folder, replica_folder)