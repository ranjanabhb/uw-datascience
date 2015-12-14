import urllib
import json

def geoCode(latLng):
    serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

    #url = serviceurl + urllib.urlencode({'sensor':'false', 'latlng': '37.7845, -122.4415'})
    url = serviceurl + urllib.urlencode({'sensor':'false', 'latlng': latLng})
    #print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    # 'Retrieved',len(data),'characters'

    try: 
        js = json.loads(str(data))
    except: 
        js = None
        
    if ('status' not in js) or (js['status'] != 'OK'):
        print '==== Failure To Retrieve ===='
        #print data
        return

    #print json.dumps(js, indent=4)
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    #print 'lat',lat,'lng',lng
    location = js["results"][0]["formatted_address"]
    #print location
    place_id = js['results'][0]['place_id']
    #print place_id
    
    components = js["results"][0]["address_components"]
    zip_code = [component[u'long_name'] for component in components if component[u'types'][0] == u"postal_code" ]
    return zip_code[0]

if __name__ == "__main__":
    geoCode()