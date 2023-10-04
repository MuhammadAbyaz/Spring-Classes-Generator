import os

print("Enter package name: ")
packageName = input()

print("Enter model name: ")
modelName = input()

os.mkdir(os.getcwd() + "/" + packageName)

os.chdir(os.getcwd()+"/" + packageName)
print(os.getcwd())