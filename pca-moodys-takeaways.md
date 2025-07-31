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
# GRAMMAR STATEMENTS 
grm_out_of_sample = "out of sample yield curves  -  those not used in the analysis to derive yield curves"
grm_centering_scaling = "centering and scaling"
grm_role_of_transformations = "role of transformations"
grm_inverse_problem_determining_magnitudes = " inverse problem of determining pc magnitudes given a yield curve"
grm_modelling_yield_curve_dynamics = "modelling yield curve dynamics  -  is this the same as modelling yield curve changes given a base curve"
grm_population = "population is the total population from which the sample set is obtained. For the examples in this paper this could also be called the universe of possible yield curves"
grm_sample_set = "data set on which the PCA is performed. For the examples presented in this paper this is just a set of absolute yield curves in terms of forward rates"
```


```python
# LOGIC LISTS
lgc_out_of_sample = [
"out of sample yield curves  -  those not used in the analysis to derive yield curves",
"his is shown to potentially require many more PCs than we might first think.",
"perhaps bayesian inference gets around this...."

]

lgc_adjacent_points_on_curve_do_not_move_independently = [
"adjacent points on the yield curve do not move independently",
"why is this-when considering the forward yield curve specifically"
]
lgc_central_tendency = [
"since pca derived from covariance matrix we are talking about deviation from the mean",
"what does the mean represent in this context",
        ]        

lgc_population_and_sample = [
"more is made of difference between population and sample than i would",
"i would go for largest available dataset that is relevant and to me that is the population",
"the paper seems to see validity in not using whole population to calibrate"
]




```

```python
# RHETORICAL STATEMENTS 
rht_pc_intuitive = "intuitively, PCs represent ways in which the forward rates making up a yield curve can deviate from their mean levels"
rht_reproduce_if_keep_all_pcs =  "A model including all of the PCs turns can perfectly reproduce all of the yield curves on which the PCA analysis was performed."
```

```python
# CRITICISMS

crt_99_pct = [
"it might be appropriate to use two PCs in a reduced model as these should cover around 99% of the yield curve variability",
"this 99% seems arbitrary since my first run gave high 80% using a 50year dataset",
"perhaps a shorter dataset is this reliable",

]

crt_simulating_curve_not_changes = [
"it looks like they are simulating the whole curve rather than modelling changes from one period to the next",
"as evidence by statement 'The solid black line is the mean yield curve at the 𝑡 = 1 projection horizon.'"
"the chart with solid black line and the dotted black as movement suggests they are treating mean curve as the current yield curve which cannot see has pratical usage",
]









```

```python

display(HTML("<h1>Rough notes on moodys paper</h1>"))
display(HTML("<h2>grammar</h2>"))
filtered_list = [s for s in fnc.list_variables(globals()) if s.startswith("grm")]                    
for html in filtered_list:                                                         
     display(HTML(eval(html)))                                                                
display(HTML("<h2>logic</h2>"))
logi_list = [s for s in fnc.list_variables(globals()) if s.startswith("lgc")]                    
for html in logi_list:                                                         
     display(HTML(fnc.combine_strings_with_heading(eval(html),3)))                                                                
display(HTML("<h2>rhetoric</h2>"))
rhet_list = [s for s in fnc.list_variables(globals()) if s.startswith("rht")]                    
for html in rhet_list:                                                         
     display(HTML(eval(html)))                                                                
display(HTML("<h2>criticisms</h2>"))
crt_list = [s for s in fnc.list_variables(globals()) if s.startswith("crt")]                    
for html in crt_list:                                                         
     display(HTML(fnc.combine_strings_with_heading(eval(html),3)))                                                                









```

