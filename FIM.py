#Importing necessary modules
import hashlib
import os
import time
import re

#Constants
BASELINE_PATH = r"Insert filepath for Baseline.txt to be stored in/" #Ensure backslash is used in path and present at end of filepath otherwise it won't work
FILE_PATH = r"Insert filepath for Baseline.txt to be stored in/" #Ensure backslash is used in path and present at end of filepath otherwise it won't work
BUF_SIZE = 65536

#Checks if a baseline file exists
def baselineExists():
    if not os.path.exists(os.path.join(BASELINE_PATH, "Baseline.txt")):
        print("Creating new baseline...")
        createBaseline()
    else:
        print("Baseline already exists, would you like to overwrite it (Y/N)?")
        overwrite_input = input("").upper()
        if overwrite_input == "Y":
            createBaseline()

#Calculate the hash for a given file
def calculateHashForGivenFile(filename):
    sha512 = hashlib.sha512()
    filepath = os.path.join(FILE_PATH, filename)

    if os.path.isfile(filepath):
        with open(filepath, 'rb') as binaryFile:
            while True:
                data = binaryFile.read(BUF_SIZE)
                if not data:
                    break
                sha512.update(data)
        return sha512.hexdigest()
    return None

#Create a baseline file
def createBaseline():
    with open(os.path.join(BASELINE_PATH, "Baseline.txt"), 'w') as f:
        for file in os.listdir(FILE_PATH):
            hash_value = calculateHashForGivenFile(file)
            if hash_value:
                f.write(f"{os.path.join(FILE_PATH, file)}|{hash_value}\n")
        print("New baseline successfully created")

#Main file integrity check
def fileIntegrityCheck():
    while True:
        if not os.path.exists(os.path.join(BASELINE_PATH, "Baseline.txt")):
            print("Baseline not found. Please create one first.")
            return

        #Read the baseline file
        with open(os.path.join(BASELINE_PATH, "Baseline.txt"), 'r') as baseline_file:
            baseline_data = [line.strip().split('|') for line in baseline_file.readlines()]

        current_files = os.listdir(FILE_PATH)
        monitored_files = {os.path.basename(item[0]): item[1] for item in baseline_data}

        #Check each file within the monitored directory
        for file in current_files:
            full_path = os.path.join(FILE_PATH, file)
            if os.path.isfile(full_path):
                current_hash = calculateHashForGivenFile(file)

                #If a new file has been created
                if file not in monitored_files:
                    print(f"New file detected: {file}")

                #If a file has been modified
                elif monitored_files[file] != current_hash:
                    print(f"File modified: {file}")

        #Check for deleted files
        for file in monitored_files.keys():
            if file not in current_files:
                print(f"File deleted: {file}")

        time.sleep(2)  #Checks every 2 seconds

#Options given to user
print("Please select an option:")
print("A) Create new baseline")
print("B) Monitor existing baseline")
user_input = input("").strip().upper()

if user_input == "A":
    baselineExists()
elif user_input == "B":
    fileIntegrityCheck()
else:
    print(f"{user_input} is not a valid option")
