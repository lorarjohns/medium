---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.4.1
---

```python
import numpy as np
import random
```

```python
import ipytest
ipytest.config(rewrite_asserts=True, magics=True)

__file__ = "hello.ipynb"
```

```python
def sigmoid(x):
    """
    Compute the sigmoid function for the input here.
    Arguments:
    x -- A scalar or numpy array.
    Return:
    s -- sigmoid(x)
    """

    s = np.exp(x)/(np.exp(x)+1)

    return s
```

```python
test_sigmoid_data = {
        'x': np.array([-0.46612273, -0.87671855, 0.54822123, -0.36443576, -0.87671855, 0.33688521
                          , -0.87671855, 0.33688521, -0.36443576, -0.36443576, 0.54822123]).astype(float),
        's': np.array(
            [0.38553435, 0.29385824, 0.63372281, 0.40988622, 0.29385824, 0.5834337, 0.29385824, 0.5834337, 0.40988622,
             0.40988622, 0.63372281]).astype(float),
    }
```

```python
%%run_pytest[clean] -vv

def test_sigmoid():

    test_sigmoid_data = {
        'x': np.array([-0.46612273, -0.87671855, 0.54822123, -0.36443576, -0.87671855, 0.33688521
                          , -0.87671855, 0.33688521, -0.36443576, -0.36443576, 0.54822123]).astype(float),
        's': np.array(
            [0.38553435, 0.29385824, 0.63372281, 0.40988622, 0.29385824, 0.5834337, 0.29385824, 0.5834337, 0.40988622,
             0.40988622, 0.63372281]).astype(float),
    }
    assert np.allclose(test_sigmoid_data['s'], sigmoid(test_sigmoid_data['x']))
```

```python
print(In, Out)
```

```python
print(Out)
```

```python
print(In)
```

```python
%hist -g
```

```python
%history -g
```

```python
%hist -g
```

```python
%history -p -l 3
```

```python
import numpy as np
import random
```

```python
import ipytest
ipytest.config(rewrite_asserts=True, magics=True)

__file__ = "hello.ipynb"
```

```python
def sigmoid(x):
    """
    Compute the sigmoid function for the input here.
    Arguments:
    x -- A scalar or numpy array.
    Return:
    s -- sigmoid(x)
    """

    s = np.exp(x)/(np.exp(x)+1)

    return s
```

```python
test_sigmoid_data = {
        'x': np.array([-0.46612273, -0.87671855, 0.54822123, -0.36443576, -0.87671855, 0.33688521
                          , -0.87671855, 0.33688521, -0.36443576, -0.36443576, 0.54822123]).astype(float),
        's': np.array(
            [0.38553435, 0.29385824, 0.63372281, 0.40988622, 0.29385824, 0.5834337, 0.29385824, 0.5834337, 0.40988622,
             0.40988622, 0.63372281]).astype(float),
    }
```

```python
%%run_pytest[clean] -vv

def test_sigmoid():

    test_sigmoid_data = {
        'x': np.array([-0.46612273, -0.87671855, 0.54822123, -0.36443576, -0.87671855, 0.33688521
                          , -0.87671855, 0.33688521, -0.36443576, -0.36443576, 0.54822123]).astype(float),
        's': np.array(
            [0.38553435, 0.29385824, 0.63372281, 0.40988622, 0.29385824, 0.5834337, 0.29385824, 0.5834337, 0.40988622,
             0.40988622, 0.63372281]).astype(float),
    }
    assert np.allclose(test_sigmoid_data['s'], sigmoid(test_sigmoid_data['x']))
```

```python
%history -l 3
```

```python
%history -l -o 3
```

```python
%history -u
```

```python
%history -u -n
```

```python
%history -u -t
```

```python
%history -u 
```

```python
%history -u -t
```

```python
%history -u 
```

```python
!echo $PATH
```

```python
%history -u -T
```

```python
%history -u -t
```

```python
%history -1/1-4 -p -o
```

```python
%history ~1/1-4 -p -o
```

```python
%history ~2/1-4 -p -o
```

```python
%history ~3/1-4 -p -o
```

```python
%history ~3/4-6 -p -o
```

```python
%history ~3/7 -p -o
```

```python
%history ~4/7 -p -o
```

```python
%history ~4 -p -o
```

```python
%history ~2 -p -o
```

```python
%history ~2/1-5 -p -o
```

```python
%history ~2/1-8 -p -o
```

```python
%history ~3/1-8 -p -o
```

```python
%history ~3/1-8 -n -p -o
```

```python
%history -n -g "pytorch"
```

```python
%history -n -g "sklearn"
```

```python
%history -n -g "sigmoid"
```

```python
%history -n -g pytorch
```

```python
%history -n -g torch
```

```python
%notebook hello_history.ipynb
```
