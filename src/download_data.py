import os
import shutil

s3_path = "s3://srivatsav.databucket"
destination = os.path.abspath(os.path.dirname(__file__))
destination_folder = os.path.join(destination, "..", "data")

if(os.path.exists(destination_folder)):
    shutil.rmtree(destination_folder)

os.makedirs(destination_folder)
final_command = "aws s3 sync " + s3_path + " " + destination_folder
# print(final_command)
os.system(final_command)