import requests
import json

response = requests.get("https://swapi.dev/api/starships/10/")

if response.status_code == 200:
    content = response.json()
    info = json.loads(response.text)
    resultDict = {}
    keysName = ["name", "starship_class", "max_atmosphering_speed", "pilots"]
    for key in keysName:
        resultDict[key] = info[key]
    pilotKeysName = ["name", "height", "mass", "homeworld"]
    pilotsList = []
    for pilot in resultDict["pilots"]:
        pilotResponse = requests.get(pilot)
        if pilotResponse.status_code == 200:
            pilotContent = json.loads(pilotResponse.text)
            pilotResultDict = {}
            for key in pilotKeysName:
                pilotResultDict[key] = pilotContent[key]
            homeworldUrl = pilotResultDict["homeworld"]
            homeworldResponse = requests.get(homeworldUrl)
            if homeworldResponse.status_code == 200:
                homeworldContent = json.loads(homeworldResponse.text)
                pilotResultDict["homeworld"] = homeworldContent["name"]
            pilotResultDict["homeworld-url"] = homeworldUrl
            pilotsList.append(pilotResultDict)

    resultDict["pilots"] = pilotsList
    result = json.dumps(resultDict, indent=4)
    print(result)
    with open("starship_info.json", "w") as f:
        json.dump(resultDict, f, indent=4)

else:
    print("Error")