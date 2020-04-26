# Arguments are as follows: python File-Backup.py FromDir ToDir -Compress
import sys, os, zipfile, shutil, datetime


class FileBackup:

    def __init__(self, fromDir: str, toDir: str, compress: bool):
        
        self.fromDir = fromDir

        self.toDir = toDir

        self.compress = compress

        self.__CheckTypes()

    def __CheckTypes(self):

        if type(self.fromDir) == str and type(self.toDir) == str and type(self.compress) == bool:

            return True

        raise TypeError("One or more arguments are not of correct type. Must be -> string, string, boolean")

    def Begin(self):

        if os.path.exists(self.fromDir):
            
            if self.compress:

                self.__Compress()
            
            else:
                
                date = datetime.datetime.now()

                shutil.copytree(self.fromDir, os.path.join(self.toDir, "{}-{}-{}".format(date.year, date.month, date.day)))
            
        else:

            raise FileNotFoundError("The specified file or directory was not found.")
    
    def __Compress(self):
                
        date = datetime.datetime.now()
        
        zipFile = zipfile.ZipFile(os.path.join(self.toDir, "{}.zip".format("{}-{}-{}".format(date.year, date.month, date.day))), "w", zipfile.ZIP_DEFLATED)

        for root, _, files in os.walk(self.fromDir):

            for fileName in files:

                zipFile.write(os.path.join(root, fileName))

        zipFile.close()



if __name__ == "__main__":

    if len(sys.argv) == 3:

        FileBackup(sys.argv[1], sys.argv[2], False).Begin()

    elif len(sys.argv) == 4:

        FileBackup(sys.argv[1], sys.argv[2], sys.argv[3].lower() == "-compress").Begin()
    
    else:

        print("Invalid Parameters. Example Use: \n\n\tpython File-Backup.py 'C:/Users/Me/Desktop/Files' 'E:/Backups' -compress")

        os._exit(2)


# Tests:
#
#   - Backup from location: Folder and file
#   - Backup to location: Folder and file
#   - Compression on and off for both above