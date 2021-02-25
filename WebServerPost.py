#! /usr/bin/env python3

import os
import requests


#list .txt files that contain feedback
for file in os.listdir("/data/feedback"):
  #open.txt files
  with open('/data/feedback/' + file) as content:
    #split .txt files and place in feedback dictionary
    fbdict = content.read().split("\n")
    feedback = {
      "title":fbdict[0],
      "name":fbdict[1],
      "date":fbdict[2],
      "feedback":fbdict[3]
    }

    #use POST to post data to webserver
    request = requests.post("http://35.226.134.45/feedback/", json=feedback)
    #print status code for verification
    print(request.status_code)
