import os

def ensure_dir(file_path):
  directory = os.path.dirname(file_path)
  if not os.path.exists(directory):
    os.makedirs(directory)


def printdirs(path):
  for filename in os.listdir(path):
    if os.path.isdir(base_path + "/" + filename):
      if filename is None:
        print("wtf")
      print(filename)


print("Please input the directory you want to take files from:")
base_path = input()

if not os.path.exists(base_path):
  raise Exception("Directory does not exist")

if not os.path.isdir(base_path):
  raise Exception("Path does not belong to a directory")

if base_path[-1] != "/":
  base_path += "/"

for filename in os.listdir(base_path):
  file_path = base_path + "/" + filename
  if os.path.isfile(file_path):
    with open(file_path, 'r') as f:
      read = f.read()
      print ("Available categories:")
      printdirs(base_path)
      print ("File content:")
      print(read)
      print("Please input the category")
      userInput = input()
      if not userInput == "":
        new_path = base_path + userInput + "/"
        print(new_path)
        ensure_dir(new_path)
        os.rename(file_path, new_path + filename)
