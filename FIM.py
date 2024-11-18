#Import the necessary modules
import hashlib
import sys
import os
import time
import re

# Consts
BASELINE_PATH = r"Insert filepath for Baseline.txt to be stored in/" #Use backslashes when specifying filepath
FILE_PATH = r"Insert filepath for directory of files to be monitored/" #Use backslashes when specifying filepath
FILES = os.listdir(FILE_PATH)
IS_EXISTING = os.path.exists(BASELINE_PATH)
BUF_SIZE = 65536

def baselineExists():

    if IS_EXISTING is False:
        print("Creating new baseline...")
        #os.remove("Baseline.txt")
        createBaseline()
        
        #print(file)

def calculateHashForGivenFile(filename):
    md5 = hashlib.md5()
    sha512 = hashlib.sha512()
    #print(os.stat(FILE_PATH + filename))
    if os.path.isfile(FILE_PATH + filename):
        with open(FILE_PATH + filename, 'rb') as binaryFile:
            data = binaryFile.read(BUF_SIZE)
            if not data:
                return
            md5.update(data)
            sha512.update(data)
            return sha512
    else:
        pass

def createBaseline():
    with open(BASELINE_PATH + "Baseline.txt", 'w') as f:
        for file in FILES:
            #print(file)
            hashStore = calculateHashForGivenFile(file)
            #print("SHA512: {0}".format(hashStore.hexdigest()))
            f.write(FILE_PATH + file + "|" + hashStore.hexdigest() + "\n")
            #Will break if file is empty

    '''
        For each file in FILE_PATH
            calculate the file hash
            save in the format of FILE_PATH + file name + | + calculated hash
            eg: "C:\filepath\test.txt|E2BD7A81FA150195C30ABD5B34CB7DCEE29B3A4AB4C878334E0FB277EAEE0EFEE80F9B3AE42CC63235D987E48BEF4E9E885DD70955AF3017D1B120F8810C5B91"
    '''

def File_Integrity_Check():
    while True:  
        #fileHashDict = {}
        q = 1
        t = 0
        y = 1

        with open(BASELINE_PATH + "Baseline.txt", "r") as file:
            hashAndPath = re.split("[\n|]",file.read())
            for f in FILES:
                fileList = os.listdir(FILE_PATH)
                #f = FILES[0]
                fileStillExists = os.path.exists(hashAndPath[t]) #Variable to check if file exists 
                hash = calculateHashForGivenFile(f).hexdigest()         
                if fileStillExists == False:
                    try:
                        fileHashDict = {fileList[q]}
                        #print(filePath[t])
                        #Errors out if hashAndPath[y] has a list out of range, which occurs when a new file is created
                        #If a file has been modified, do the following:
                        
                    except IndexError as e:
                        print("New file has been created")
                            #New file has been created   
                #If a file has been created, do the following:       
                # if hash != hashAndPath[y]:
                    
                #     #File has been created
                #     print("File has been created")
                # else:
                #     #File has not been created
                #     pass
                else:
                     pass

                # if hashAndPath[y] == hash:
                #     # If file hashes match, do nothing
                #     pass
                # else:
                #     print("File has been modified")
                #     # File has been modified            
                    


                        #If a file has been deleted, do the following:
                        # for i in hashAndPath[t]:
                        #     fileStillExists = os.path.exists(hashAndPath[t])
                        #     if fileStillExists:
                        #         #File hasn't been deleted
                        #         # print("File hasn't been deleted")
                        #         pass   
                        # print("File has been deleted")

                q +=1 #Increments for each file in directory
                t +=2 #Increments dictionary values, so the file path and hash value stay in line 
                y +=2 

            #Checks whether file has been deleted
            # for key in fileList:               
            #     fileStillExists = os.path.exists(hashAndPath[t])
            #     if fileStillExists:
            #         #File hasn't been deleted
            #         print("File hasn't been deleted")
            #         pass
            #     else:      
            #         #File has been deleted
            #         print("File has been deleted")
                


                  


        time.sleep(2)
             

        
    



print("Please select an option")
print ("A) Create new baseline")
print ("B) Monitor existing baseline")
user_input = input("").upper()

if user_input == "A":
    baselineExists()
    createBaseline()
elif user_input =="B":
        File_Integrity_Check()

    #File_Integrity_Check()
#elif user_input =="C":
else:
    print(user_input + " is not a valid option")


