import json5
import os.path

def resourcesTable(resources):
  resourceTypes = []
  table = "| Resource Type | ApiVersion         |\n"
  table += "| ------------ | ------------------ |\n"
  
  for resourcesInfo in resources:
    resourceType = resourcesInfo['type']
    resourceApiVersion = resourcesInfo['apiVersion']
    if resourceType not in resourceTypes:
      table += f"| `{resourceType}` | {resourceApiVersion} |\n"
      resourceTypes.append(resourceType)
    try:
          resourceInsideResource = resourcesInfo.get("resources", {})
          for resourceInResource in resourceInsideResource:
            resourceInsideResourceType = resourceInResource['type']
            resourceInsideResourceApiVersion = resourceInResource['apiVersion']
            if resourceInsideResourceType != '' or resourceInsideResourceApiVersion != {}:
              if resourceInsideResourceApiVersion not in resourceTypes:
                table += f"| `{resourceInsideResourceType}` | {resourceInsideResourceApiVersion} |\n"
                resourceTypes.append(resourceInsideResourceType)
    except :
      itsError = NameError    


    try:
      resourceResource = resourcesInfo.get("properties", {}).get("template", {}).get("resources", {})
      for resourceInResource in resourceResource:
        resourceResourceType = resourceInResource['type']
        resourceResourceApiVersion = resourceInResource['apiVersion']
        if resourceResourceType != '' or resourceResourceType != {}:
          if resourceResourceType not in resourceTypes:
            table += f"| `{resourceResourceType}` | {resourceResourceApiVersion} |\n"
            resourceTypes.append(resourceResourceType)
    except :
      itsError = NameError
  return table

def parameterTable(parameters):
  table = "| Parameter Name | Type   | Description  | DefaultValue  | Possible values |\n"
  table += "|-------------- | -------| ------------ | ------------  | ----------------|\n"
  for paramName, paramInfo in parameters.items():
    paramType = paramInfo['type']

    try: 
      paramDefaultValue = paramInfo['defaultValue'] 
    except: 
      paramDefaultValue = ""
    
    try:
      paramAllowedValues = paramInfo['allowedValue'] 
    except:
       paramAllowedValues = ""

    paramDescription = paramInfo.get("metadata", {}).get("description", "")
    
    if "Required" in paramDescription:
      paramDescriptionBold = paramDescription.replace("Required", "**Required**", 1)
    else:
      paramDescriptionBold = paramDescription.replace("Optional", "**Optional**", 1)

    table += f"| `{paramName}` | {paramType} | {paramDescriptionBold} | {paramDefaultValue} | {paramAllowedValues} |\n"
  return table

def parameterUsage(parameters):
  usage = ""
  for paramName, paramInfo in parameters.items():
    if paramInfo['type'] == "array" or paramInfo['type'] == "object":
      usage += "### Parameter Usage: " + paramName + "\n"
      usage += "\n"
      usage += "```json"
      usage += "\n\n"
      usage += "```"
      usage += "\n\n"
  return usage

def outputsTable(output):
  table = "| Output Name | Type   | Description |\n"
  table += "| ---------- | ------ | ------------ |\n"
  for outputName, outputInfo in output.items():
    outputType = outputInfo['type']
    outputDescription = outputInfo.get("metadata", {}).get("description",)
    table += f"| `{outputName}` | {outputType} | {outputDescription} | \n"
  return table

def generateReadme(armTemplate, resourceName):
  readme = "# "+ resourceName + "\n\n"
  readme += "## Resource types \n\n"
  readme += resourcesTable(armTemplate.get("resources"))
  readme += "\n"
  readme += "## Parameters \n\n"
  readme += parameterTable(armTemplate.get("parameters"))
  readme += "\n"
  readme += parameterUsage(armTemplate.get("parameters"))
  readme += "## Outputs \n\n"
  readme += outputsTable(armTemplate.get("outputs"))
  readme += "\n"
  readme += "## Considerations \n\n"
  readme += "## Additional resources \n\n"


  return readme

print("What's the resource name?")
resourceName = input()
print("Please inform the path to template create e.g. c:\\project\\folder")
baseDirectory = input()

with open(baseDirectory  + "\\deploy.json", "r") as armTemplateFile:
  armTemplate = json5.load(armTemplateFile)

readmeContent = generateReadme(armTemplate, resourceName)

if(os.path.exists(baseDirectory + "\\readme.md")):
  print("Exist a readme file this operation will overwrite it. Do you want to proceed (y/n)?")
  proceed = input()
  if proceed == "y":
    f = open(baseDirectory + "\\readme.md", "w")
    f.write(readmeContent)
    f.close()
  else:
    exit()
else:
  f = open(baseDirectory + "\\readme.md", "a")
  f.write(readmeContent)
  f.close()


