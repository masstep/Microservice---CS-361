# CS 361
# Mason Stephenson
# Microservice for Google Places ID to specific place's URL
#

import requests
import json
import time

# pull places ids from results.json
def retrieve_IDs():
    """ pulls places id from  google text search results stored in results.json"""
    with open('results.json', 'r') as text_results:
        json_object = json.load(text_results)
        data = json_object['results']

    #iterate through all search results in results.json
    for item in data:
        place_ID = item["place_id"]
        url = retrieve_URL(place_ID)
        #print(url)
        # append url to json object dictionary
        item["url"] = url
    # updates the json objects stored under "results", inserting the url into each restaurtant search result
    json_object['results'] = data

    # store update into results.json file
    with open('results.json', 'w') as overwrite:
        json.dump(json_object, overwrite, indent=4)




# take places id and request google.maps url
def retrieve_URL(place_ID):
    """ Uses places ID to perform google places details request to retrieve URL """

    api_key = # YOUR API KEY
    # url for places details request
    url = "https://maps.googleapis.com/maps/api/place/details/json?place_id="+place_ID+"&fields=url&key="+api_key
    payload ={}
    headers = {}

    # json response object containing url
    response = requests.request("GET", url, headers=headers, data=payload).json()
    #print(response)
    website = response["result"]["url"]

    return website






if __name__ == "__main__":

    while True:
        time.sleep(5.0)  # sleep 5 seconds

        with open('ready.txt', 'r') as file:
            results = file.readline()

        if results == '':
            # text file is empty, results not ready
            continue

        else:
            # text file has results populated
            retrieve_IDs()

            # after update clear file to prevent running
            with open('ready.txt', 'w') as file:
                file.write('')