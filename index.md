# {class:y}

### Python

```python
import requests

headers = {'Authorization': 'token YOUR-API-KEY'}

data = {'lights-off':['Turn my lights off',
                      'Please turn my lights off',
                      'Could you turn my lights off',
                      'Lights off',
                      'Off'],
        'lights-on': ['Turn my lights on',
                      'Please turn my lights on',
                      'Could you turn my lights on',
                      'Lights on',
                      'On']}

url = 'https://api.classy.services'
requests.post(url+'/set', json=data, headers=headers)

query = 'Lights on, please'
response = requests.post(url+'/classify', json={'query':query}, headers=headers)
print(response.text)

                      
```

```python
{'lights-on':0.95,'lights-off':0.05}
```
