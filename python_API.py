# Use python to make an API call using package called requests
# Dependencies PIP
import requests

# post_api_response = requests.get("https://api.postcodes.io/postcodes/dy60lg")
# if post_api_response.status_code == 200:
#     print(f'Thank you for your request: {post_api_response.status_code}')
# else:
#     print('oh no! Incorrect postcode')
# create function to return location/ postcode if status code is 200
# get the user to input postcode
# validate postcode, before making api call

def check_postcode():
    user_postcode = input('Please enter a valid postcode: ')
    url = 'https://api.postcodes.io/postcodes/'
    post_api_response = requests.get(url+user_postcode)
    print(post_api_response.status_code)
    if post_api_response.status_code == 200:
        print(f'Thank you for your request: {post_api_response.status_code}')
    else:
        print('oh no! Incorrect postcode')
check_postcode()



















# response_bbc = requests.get('https://www.bbc.co.uk/shahrukh')  # returns 404, error
# response_itv = requests.get('https://www.itv.com/')  # returns 200, successful
# print(f'ITV is {response_itv}, BBC is {response_bbc}')

# print(response_bbc.status_code)  # shows the number in a user friendly way
# print(response_bbc.headers)  # shows everything in the header of the url
# print(response_bbc.content)
# print(type(response_bbc.content))  # prints the data type (bytes)
# data_headers = response_bbc.headers
# for data in data_headers.values():
#     print(data)
# print(type(response_bbc.headers))
