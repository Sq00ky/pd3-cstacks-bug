import requests

accesstoken = "youraccesstoken" #JWT can be retrieved from Fiddler or by reviewing (ex.) Burpsuite logs after authenticating to nebula.starbreeze.com, programatically retrieving this is annoying... 
#... Javascript magic to generate a request id and client id that's annoying to reproduce in pythhon. Look for the response of a POST request to iam/v3/oauth/token
refreshtoken = "yourrefreshtoken" # ^
userid = "youruserid" # User id can be retrieved from Fiddler or reviewing (ex.) Burpsuite logs after authenticating to nebula.starbreeze.com... 
#... Look for an URI of iam/v3/public/namespaces/starbreeze/users/[starbreezeuserid]/platforms/justice - Look for the PD3 namespace and user id.

# Set the request headers
headers = {
    'Accept-Encoding': 'deflate, gzip',
    'Cookie': 'access_token=' + accesstoken + '; refresh_token=' + refreshtoken,
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer '+accesstoken,
    'Namespace': 'pd3',
    'Game-Client-Version': '1.0.0.0',
    'AccelByte-SDK-Version': '21.0.3',
    'AccelByte-OSS-Version': '0.8.11',
    'User-Agent': 'PAYDAY3/++UE4+Release-4.27-CL-0 Windows/10.0.19045.1.256.64bit',
}
print("Headers:\n" + str(headers))
# Set the request body
request_body = {
    'itemId': 'dd693796e4fb4e438971b65eecf6b4b7', # Item ID is specific to 10 C-Stacks @ 90,000.
    'quantity': 1,
    'price': 90000,
    'discountedPrice': 90000,
    'currencyCode': 'CASH',
    'region': 'SE',
    'language': 'en-US',
    'returnUrl': 'http://127.0.0.1'
}
print("\n")
print("Request Body:\n" + str(request_body))
print("\n")

# Make the POST request
print("Sending request to https://nebula.starbreeze.com/platform/public/namespaces/pd3/users/" + userid + "/orders")
response = requests.post(
    'https://nebula.starbreeze.com/platform/public/namespaces/pd3/users/' + userid + '/orders',
    headers=headers,
    json=request_body
)

# Check the response status code
if response.status_code == 201:
    # The order was created successfully
    print('Order created successfully!')
else:
    # An error occurred while creating the order
    print('Error creating order:', response.status_code)
