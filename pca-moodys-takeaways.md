---
jupyter:
  jupytext:
    formats: ipynb,py:percent,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.4
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
import functions as fnc


```

```python
grm_out_of_sample = "out of sample yield curves  -  those not used in the analysis to derive yield curves"
grm_centering_scaling = "centering and scaling"
grm_role_of_transformations = "role of transformations"
grm_inverse_problem_determining_magnitudes = " inverse problem of determining pc magnitudes given a yield curve"
grm_modelling_yield_curve_dynamics = "modelling yield curve dynamics  -  is this the same as modelling yield curve changes given a base curve"



lgc_out_of_sample = [
"out of sample yield curves  -  those not used in the analysis to derive yield curves",
"his is shown to potentially require many more PCs than we might first think.",
"perhaps bayesian inference gets around this...."

]

lgc_adjacent_points_on_curve_do_not_move_independently = [
"adjacent points on the yield curve do not move independently",
"why is this-when considering the forward yield curve specifically"

        ]        
```

```python

display(HTML("<h2>grammar</h2>"))
filtered_list = [s for s in fnc.list_variables(globals()) if s.startswith("grm")]                    
for html in filtered_list:                                                         
     display(HTML(eval(html)))                                                                
display(HTML("<h2>logic</h2>"))
logi_list = [s for s in fnc.list_variables(globals()) if s.startswith("lgc")]                    
for html in logi_list:                                                         
     display(HTML(eval(html)))                                                                


```

