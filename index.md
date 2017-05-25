# {class:y}

### Python

```python
import requests

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
requests.post(url+'/set',json=data)

query = 'Lights on, please'
response = requests.post(url+'/classify',json={'query':query})
print(response.text)

                      
```

```python
{'lights-on':0.95,'lights-off':0.05}
```
