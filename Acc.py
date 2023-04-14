import requests

import json

import location

while True:

    URL = 'https://jsonplaceholder.typicode.com/todos/1'

    response = requests.get(URL)

    obj = json.loads(response.content)

    obj_data = obj['title']

    print(obj_data)

    

    # Example threshold values

    miv = 5

    mav = 10

    

    if obj_data > mav or obj_data < miv:

        location.main()

        break

    else:

        print("Safe")

