## Welcome to GitHub Pages

You can use the [editor on GitHub](https://github.com/crgirard/classy/edit/master/index.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

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

url = 'https://
requests.post(url+'/set',json=data)

query = 'Lights on, please'
response = requests.post(url+'/classify',json={'query':query})
print(response.text)

                      
```

```python
{'lights-on':0.95,'lights-off':0.05}
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
