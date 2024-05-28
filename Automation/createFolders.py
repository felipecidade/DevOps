import os

def createFolderStructure(basePath, folderStructure):
  for folderName, folderContent in folderStructure.items():
    folderPath = os.path.join(basePath, folderName)
    os.makedirs(folderPath)

    if "files" in folderContent:
        for fileName, fileContent in folderContent["files"].items():
            filePath = os.path.join(folderPath, fileName)
            with open(file_path, "w") as file:
                file.write(fileContent)

    if "subfolders" in folderContent:
      createFolderStructure(folderPath, folderContent["subfolders"])

print("What's the resource name?")
resourceName = input()
print("Type 1-Component or 2-Module")
typeChoice = input() 
print("Please inform the path to template create e.g. c:\\project\\folder")
baseDirectory = input()

while(True):
  if typeChoice == '1':
    folderType = "component"
    break
  elif typeChoice == '2':
    folderType = "module"
    break
  else:
    print("Please inform the correct type: 1 for component or 2 for module")
    typeChoice = input()

if folderType == "module":
    folderTemplate =  {
      resourceName : {
            "files":{
              "deploy.json" : "",
              "readme.md" : "",
              "testCases.md" : ""
            },
            "subfolders": {
              "Parameters": {
                  "files": {
                    "parameters.json" : ""
                  },
                },
            "Pipeline": {
                  "files": {
                    "pipeline.yml" : ""
                },
            },
            "Scripts":{
              "files":{
                "git_placeholder.md" : "",
              }
            },
            "Tests":{
              "files":{
                "module.tests.ps1" : ""
              }
            }
            },
        }
    }
else:
    folderTemplate =  {
      resourceName : {
            "files":{
              "deploy.json" : "",
              "readme.md" : "",
              "testCases.md" : ""
            },
            "subfolders": {
              "Parameters": {
                  "files": {
                    "parameters.json" : ""
                  },
                },
            "Pipeline": {
                  "files": {
                    "pipeline.yml" : ""
                },
            },
            "Tests":{
              "files":{
                "module.tests.ps1" : ""
              }
            }
            },
        }
    }

createFolderStructure(baseDirectory, folderTemplate)
