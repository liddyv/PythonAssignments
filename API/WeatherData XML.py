import urllib.request as ur
import xml.etree.ElementTree as etree
import json


# API documentation from:  http://openweathermap.org/API

# Sample, try:  api.openweathermap.org/data/2.5/weather?q=London&mode=xml


API_KEY = '9862530421c42522c076c0a58daab95b'

def getInfo(city):
   
    # '{"cookies": {"sessioncookie": "123456789"}}'

    URL = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&mode=xml' + '&APPID=' + API_KEY
    print("URL request is: " + URL)
    
    URL_AIR = 'http://maps.openweathermap.org/maps/2.0/weather/TA2/{z}/{x}/{y}?'+ "appid=" + API_KEY    
    print("URL_AIR request is: " + URL_AIR)
    
    # Make the request and save the responseAsXML as a string.
    #In Python v3 the "urllib.request" is a module by itself, therefore "urllib" cannot be used here.
    #responseAsXML = urllib.urlopen(URL).read()
    responseAsXML = ur.urlopen(URL).read()
    print(responseAsXML)
    
    with ur.urlopen(URL_AIR) as url:
        responseAIRAsJson = json.loads(url.read().decode())
    print(responseAIRAsJson)

    # Parse as an XML document    
    tree = etree.fromstring(responseAsXML)
    print()
    print(tree)
    print()

    degreesK =  tree.find('temperature').attrib['value']
    degreesK = float(degreesK)
    return degreesK

# Convert from Kelvin degrees to Fahrenheit
def convertKToF(degreesK):
    degreesF = (1.8 * (degreesK - 273.)) + 32
    return degreesF


while True:
    city= input('What city would you like the temperature of? ')
    if city == '':
        break
    tempK = getInfo(city)
    #print "TempK is:", tempK
    tempF = convertKToF(tempK)
    print(tempF)
    print()






