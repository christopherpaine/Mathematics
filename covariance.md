---
jupyter:
  jupytext:
    formats: ipynb,py:percent,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.17.2
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

```python
# imports
from IPython.display import display, Markdown, HTML, SVG
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO
```


```python
wrd_covariance = """
<h1>
covariance
</h1>

<h2>
                 Observed Covariance vs. Theoretical Covariance                 
</h2>

<p>Observed Covariance is calculated directly from a dataset. It measures how two  
variables change together in a specific sample. This is an empirical measure and
can be influenced by sample size, outliers, and sampling method.                </p>

<p>Theoretical Covariance, on the other hand, is derived from the probability      
distributions of random variables. It is a parameter of the joint distribution  
and represents the expected value of the product of the deviations of two random
variables from their means. This is a more abstract concept and is used in      
theoretical models to predict relationships between variables.                  
</p>

<p>
In summary, observed covariance is data-driven, while theoretical covariance is 
model-driven.                                                                   
</p>
"""


```

```python
display(HTML(wrd_covariance))










```

