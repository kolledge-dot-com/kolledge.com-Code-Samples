# The shutil.copyfile() method
import shutil

source_file = "/path/to/source/file"
destination_file = "/path/to/destination/file"
shutil.copyfile(source_file, destination_file)




# The shutil.copy() method
import shutil

source_file = "/path/to/source/file"
destination_file = "/path/to/destination/file"
shutil.copy(source_file, destination_file)






# The shutil.copy2() method
import shutil

source_file = "/path/to/source/file"
destination_file = "/path/to/destination/file"
shutil.copy2(source_file, destination_file)




# The shutil.copyfileobj() method
import shutil

source_file = open("/path/to/source/file", "rb")
destination_file = open("/path/to/destination/file", "wb")
shutil.copyfileobj(source_file, destination_file, length=16*1024*1024, offset=0)
source_file.close()
destination_file.close()



# The os.popen() method
import os

source_file = "/path/to/source/file"
destination_file = "/path/to/destination/file"
os.popen("cp {0} {1}".format(source_file, destination_file))




# The os.system() method
import os

source_file = "/path/to/source/file"
destination_file = "/path/to/destination/file"
os.system("cp {0} {1}".format(source_file, destination_file))




# The subprocess.call() method
import subprocess

source_file = "/path/to/source/file"
destination_file = "/path/to/destination/file"
subprocess.call(['cp', source_file, destination_file])




# The subprocess.check_output() method
import subprocess

source_file = "/path/to/source/file"
destination_file = "/path/to/destination/file"
subprocess.check_output(['cp', source_file, destination_file])




# copy all files from a directory
import os
import shutil

source_directory = "/path/to/source_directory"
destination_directory = "/path/to/destination_directory"
for file_name in os.listdir(source_directory):
   source = os.path.join(source_directory, file_name)
   destination = os.path.join(destination_directory, file_name)
   shutil.copy(source, destination)




# copy entire directory in python
import shutil

source_directory = "/path/to/source_directory"
destination_directory = "/path/to/destination_directory"
shutil.copytree(source_directory, destination_directory)