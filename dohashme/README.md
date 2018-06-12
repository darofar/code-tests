# DoHashMe

## Statement 
Write code to find a six letter string of characters that contains only letters from
    
    'acdefgilmnoprstuwy'

Such that the hash('the string') is

    '18754844497'

If hash is defined as:

```python
def hash(st):
    global alphabet
    h = 7
    letters = alphabet
    for i in range(len(st)):
        h = h * 37 + letters.index(st[i])
    return h
```

## Analysis
Hashes obtained from this function will be a set of ordered numbers if strings are constructed 
of consecutively characters for the given alphabet. For example:

    hash("a") = 259
    hash("c") = 260

So we can find the candidates moving from right to left and checking if is near the result as 
show in dehash function.

## Usage

    $> python3 dehashme.py
    hash('pydoof') gives '18754844497' hash.
