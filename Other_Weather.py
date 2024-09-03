#Stephen Smith
#Description About PM Accelerator: PM Accelerator is the premier AI learning and development hub, 
#featuring award-winning AI products and mentors from top-tier companies such as Google, Meta, and Apple. 
#We offer a dynamic AI PM Bootcamp, designed to empower the next generation of AI professionals through hands-on experience, mentorship, and real-world projects.


import requests

Api_key = '6e6f9659fef62e5c5d1103979100d281'
base_url = 'http://api.openweathermap.org/data/2.5/weather'

city = input('Enter a city/state name: ')

request_url = f"{base_url}?appid={Api_key}&q={city}"
response = requests.get(request_url)

if response.status_code==200:
    
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp']- 273.15,2 ) # for celsius
    
    print('Current Weather is: ', weather)
    print('Current Temperature is: ', temperature)
    print('Current Humidity feels like it is ', data['main']['humidity'], 'percent')
else:
    print("An error occured... ")    
