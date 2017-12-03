# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 20:20:31 2017

@author: Juchen
"""

#!/usr/bin/env python

import requests
import untitled2
import codecs

# TODO: If you have your own Client ID and secret, put down their values here:
clientId = "FREE_TRIAL_ACCOUNT"
clientSecret = "PUBLIC_SECRET"
#text to translate, import from javascript
texttotranslate = input("Enter text to translate: ")
#language translating to, import from javascript application
country = input("Language to translate to: ")

# TODO: Specify your translation requirements here:
#always english
fromLang = "en"

toLang = untitled2.newlangdict[country]
text = texttotranslate

jsonBody = {
    'fromLang': fromLang,
    'toLang': toLang,
    'text': text
}

headers = {
    'X-WM-CLIENT-ID': clientId, 
    'X-WM-CLIENT-SECRET': clientSecret
}

r = requests.post('http://api.whatsmate.net/v1/translation/translate', 
    headers=headers,
    json=jsonBody)
results = str(r.content.decode("UTF-8"))
if "error" in results.lower():
    results = "ERROR"
file_object = codecs.open("resulttext.txt",'w', encoding = "UTF-8")

file_object.write(results)