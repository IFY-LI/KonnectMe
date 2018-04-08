import json

data = {}  
data['people'] = []  
data['people'].append({  
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({  
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({  
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})
# 
with open('data.txt', 'w') as outfile:  
    json.dump(data, outfile)
#    
with open('data.txt') as json_file:  
    data = json.load(json_file)
    for p in data['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')

def updateJsonFile():
    jsonFile = open("replayScript.json", "r") # Open the JSON file for reading
    data = json.load(jsonFile) # Read the JSON into the buffer
    jsonFile.close() # Close the JSON file

    ## Working with buffered content
    tmp = data["location"] 
    data["location"] = path
    data["mode"] = "replay"

    ## Save our changes to JSON file
    jsonFile = open("replayScript.json", "w+")
    jsonFile.write(json.dumps(data))
    jsonFile.close()