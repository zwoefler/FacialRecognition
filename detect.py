import json, os, requests

credFile = "credentials"
subscription_key = ""
face_api_url = ""

def readCredentials(credFile):
    with open(credFile, 'r') as f:
        data = f.readlines()
    return data

credentials = readCredentials(credFile)
subscription_key = credentials[0].split("=")[1].strip()
face_api_url = credentials[1].split("=")[1].strip()+ '/face/v1.0/detect'

print(credentials)
print(subscription_key)
print(face_api_url)


image_url = 'https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/faces.jpg'

headers = {'Ocp-Apim-Subscription-Key': subscription_key}

params = {
    'detectionModel': 'detection_03',
    'returnFaceId': 'true'
}


response = requests.post(face_api_url, params=params,
                         headers=headers, json={"url": image_url})
print(json.dumps(response.json()))

