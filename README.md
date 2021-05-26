# API
## Application Programming Interface
- An API, or Application Programming Interface, is a server that you can use to retrieve and send data to using code. APIs are most commonly used to retrieve data, and that will be the focus of this beginner tutorial. When we want to receive data from an API, we need to make a request.
- API call is what UberEats uses (FOod on its way, food delivered etc)

# Post codes Exercise

### Timings
- 30 - 45 Minutes

### Summary
- Use the post codes.io to go fetch some useful data.
- You can also create absrtaction for other APIs.

### Tasks

* Create a program that request a post code
* check if the postcode is valid
* then uses an API call to fetch more data from post code
* display the data in user friendly format 
  * Extra:
  * go explore other APIs

## Acceptance Criteria

* uses get request
* uses post request
* apply OOP
* filter response for useful information and displays
### First iteration
```python
# Use python to make an API call using package called requests
# Dependencies PIP
import requests

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
```
### Second iteration

