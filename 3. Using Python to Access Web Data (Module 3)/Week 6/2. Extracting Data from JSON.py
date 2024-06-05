import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False

# Define the service URL
if api_key is False:
    serviceurl = 'https://py4e-data.dr-chuck.net/comments_1651099.json'
else:
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# Create SSL context to ignore certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = serviceurl
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: 
        parms['key'] = api_key

    # Construct the URL with the parameters
    url = serviceurl + '?' + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except json.JSONDecodeError:
        js = None

    if not js:
        print('=== Failure to Retrieve ===')
        print(data)
        continue 

    #print(json.dumps(js, indent=4))

    if 'comments' in js:
        comments = js['comments']
        total_count = len(comments)
        print('Count:', total_count)

        comment_values = []
        for comment in comments:
            if 'count' in comment:
                count_value = comment['count']
                comment_values.append(count_value)

        total_sum = sum(comment_values)
        print('Sum:', total_sum)


