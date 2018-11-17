# classy

[![Build Status](https://travis-ci.org/coreygirard/classy.svg?branch=master)](https://travis-ci.org/coreygirard/classy) <br>
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

### What

Easy lightweight text classification via Naive Bayes. Give it a small set
of example data, and it will classify similar inputs with blazing speed and pretty good accuracy.

### Why

Making a basic chatbot? Want to do basic auto-suggestion of misspelled commands? Don't want to bust out [TensorFlow](https://github.com/tensorflow/tensorflow) or [scikit-learn](https://github.com/scikit-learn/scikit-learn)? Classy's got you covered.

### How

Classify some data (probably by hand) into a `dict`:

```python
data = {'lights':['Could you turn my lights off?',
                  'Turn my lights off',
                  'Are my lights off?',
                  'All lights off, please',
                  'Turn some lights on',
                  'Which bulbs are on?'],
        'alarm': ['Set an alarm for tomorrow at 6:00',
                  'What time is my alarm?',
                  'When will I wake up tomorrow?',
                  'What time is wakeup tomorrow?']}
```

Create the Classifier object:

```python
import classy
c = classy.Classifier(data)
```

To classify text, simply use `.classify`:

```python
c.classify('Which of my lights are off?')
```

```python
{'lights': 0.9981515711645101, 'alarm': 0.0018484288354898338}
```

---

---

### Advanced

If you wish to only receive a single classified label, rather than a full `dict` of
probabilities, set the `.threshold` property. The `.classify()` method will then return
the label of the matched class, or `None` if all probabilities are below the threshold (ie, if
the classifier is uncertain). Behavior for `.threshold` values `<= 0.5` is undefined.

```python
c = classy.Classifier(data)
c.threshold = 0.9
c.classify('Which of my lights are off?')
c.classify('Some words we've never seen before')
```

```python
'lights'
None
```

Classy by default performs minimal preprocessing of incoming text, equivalent to:

```python
def parse(text):
    # makes all uppercase characters lowercase
    text = text.lower()

    # removes all except alphanumerics and spaces
    text = re.sub(r'[^a-z0-9 ]',r'',text)

    # splits by spaces, and discards all empty strings
    return [i for i in text.split(' ') if i != '']
```

If you wish to supply a custom string parsing function, simply provide it as the `f` argument when creating a `Classifier` object:

```python
def newParse(t):
    return [i for i in t.split(',') if i != '']

c = classy.Classifier(data,f=newParse)
```

### Tricks

Want a bare-bones spellchecker over a (very) limited set of inputs?

```python
def allSubsets(text):
    temp = []
    for a in range(len(text)):
        for b in range(a,len(text)):
            temp.append(text[a:b+1])
    return temp

data = {'push':['push'],
        'commit':['commit'],
        'pull':['pull'],
        'diff':['diff']}

c = Classifier(data,f=allSubsets,threshold=0.6)

c.classify('commot')
c.classify('cpmmot')
c.classify('pulll')
c.classify('diffg')
```

```
'commit'
'commit'
'pull'
'diff'
```

The `allSubsets` function enumerates all substrings of its input, which does a reasonably decent job
of spellchecking when paired with Naive Bayes. This usage should be considered a ~~~cool trick~~~ temporary hackjob,
as there are many, many better ways to do this, for example [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance).
