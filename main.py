import os

directoryName = ""
option = True

while option:
    try:
        print("Enter directory name: ")
        directoryName = input()
        if not directoryName.islower():
            print("please enter directory name in lower case")
            option = True
        elif directoryName.islower():
            break
    except IOError:
        print("Please enter valid directory name")
        option = True

modelName = directoryName.capitalize()

print("Enter your unique Id type")
uniqueId = input()

try:
    os.mkdir(os.getcwd() + "/" + directoryName)
except FileExistsError:
    print("Folder already exists")

os.chdir(os.getcwd() + "/" + directoryName + "/")
pathList = os.getcwd().split("/")
packageName = pathList.pop(len(pathList) - 2)

main = open("{}.java".format(modelName), "x")
service = open("{}Service.java".format(modelName), "x")
controller = open("{}Controller.java".format(modelName), "x")
repository = open("{}Repository.java".format(modelName), "x")

main.write("package com." + packageName + "." + directoryName + ";" + "\npublic class " + modelName + " {}")
service.write("package com." + packageName + "." + directoryName + ";" + "\npublic class " + modelName + "Service {}")
controller.write(
    "package com." + packageName + "." + directoryName + ";" + "\npublic class " + modelName + "Controller {}")
repository.write(
    "package com." + packageName + "." + directoryName + ";" + "\npublic interface " + modelName + "Repository"
                                                                                                   " extends "
                                                                                                   "JpaRepository<"
    + modelName + "," + uniqueId + "> {}")

print("\t\t\t\t ______________________________________")
print("\t\t\t\t|                                      |")
print("\t\t\t\t|              Completed               |")
print("\t\t\t\t|______________________________________|")
