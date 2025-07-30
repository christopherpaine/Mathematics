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
import notation as ntn



```

```python
wrd_intro_chrct_eqn =""" <h1>Understanding the Characteristic Equation</h1>



<p>The characteristic equation is a fundamental concept in linear algebra and      differential equations. It is derived from a square matrix and is used to find  the eigenvalues of that matrix. For a given ( n \times n ) matrix ( A ), the    characteristic equation is obtained by setting the determinant of ( A - \lambda I ) to zero, where ( \lambda ) represents the eigenvalues and ( I ) is the      identity matrix of the same dimension as ( A ). Mathematically, it is expressed as:                                                                             </p>"""


wrd_sovling_char = "Solving this equation yields the eigenvalues, which are crucial for understanding the properties of the matrix, such as stability and oscillatory behavior in systems." 
```


```python
display(HTML('<a href="https://christopherpaine.github.io/Mathematics">link home</a>'))
display(HTML(wrd_intro_chrct_eqn+ntn.not_char_eqn+wrd_sovling_char))






```

