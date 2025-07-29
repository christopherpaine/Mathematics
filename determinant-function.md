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
not_example_matrix = r"\( \begin{bmatrix} a & b \ c & d \ \end{bmatrix}\)" 



```

```python

wrd_intro = """
<h1>
             Understanding the Determinant Function in Mathematics              
</h1>

<p>The determinant is a scalar value that can be computed from the elements of a   
square matrix. It provides important properties of the matrix, such as whether  
the matrix is invertible and the volume scaling factor of the linear            
transformation described by the matrix. For a 2x2 matrix:                       
    </p>
""" + not_example_matrix + """
<p>The determinant is calculated as (ad - bc). For larger matrices, the determinant
is computed using more complex methods, such as Laplace's expansion or row      
reduction. A non-zero determinant indicates that the matrix is invertible, while
a zero determinant means it is singular.                                        </p>
"""

wrd_invertible_functions = """ hi  """


```

```python
display(HTML(wrd_intro))


```

