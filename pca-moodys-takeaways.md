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
import functions as fnc
import takeaways as tka
```


```python
tka.f_css()







```

```python
# GRAMMAR STATEMENTS 
grm_centering_scaling = "centering and scaling"
grm_role_of_transformations = "role of transformations"
invprob_inverse_problem_determining_magnitudes = " inverse problem of determining pc magnitudes given a yield curve"
grm_modelling_yield_curve_dynamics = "modelling yield curve dynamics  -  is this the same as modelling yield curve changes given a base curve"
popnsmpl_out_of_sample = "out of sample yield curves  -  those not used in the analysis to derive yield curves"
popnsmpl_population = "population is the total population from which the sample set is obtained. For the examples in this paper this could also be called the universe of possible yield curves"
popnsmpl_sample_set = "data set on which the PCA is performed. For the examples presented in this paper this is just a set of absolute yield curves in terms of forward rates"
popnsmpl_synthetic = fnc.f_wrap_in_span("i don't see purpose of synthetic population generation","darkred")
datatrans_svt = "mean centering essential when singular value decomposition used" 
```


```python
# LOGIC LISTS
lgc_out_of_sample = [
"out of sample yield curves ", 
"those not used in the analysis to derive yield curves",
"this is shown to potentially require many more PCs than we might first think.",
"perhaps bayesian inference gets around this...."

]

lgc_adjacent_points_on_curve_do_not_move_independently = [
"adjacent points on the yield curve",  
"do not move independently",
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

data_translgc = [
"data transformations",
"not necessary to centre data when eigenvalue decomposition is used",
"scaling involves dividing by standard deviation"
"scaling is particularly useful if the variables have quite different orders of magnitude, although this is not likely to be the case for yield curves. ",
fnc.f_wrap_in_span("how to plot different orders of magnitude at various stages of own analysis and see effect of logarithmic transformation","darkred"),
" if both centring and scaling are performed then the covariance matrix is the same as the correlation matrix. "
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
tka.f_convert_string_vars_to_htmls(globals(),"grm",2,"grammar")
tka.f_convert_string_vars_to_htmls(globals(),"popnsmpl",3,"populations and samples")
tka.f_convert_string_vars_to_htmls(globals(),"invprob",3,"inverse problem")
tka.f_convert_string_vars_to_htmls(globals(),"datatrans",3,"data transformations")
display(HTML("<h2>logic</h2>"))
tka.f_display_html_with_heading(globals(),"lgc",3)
tka.f_display_html_with_heading(globals(),"data_translgc",3)

tka.f_convert_string_vars_to_htmls(globals(),"rht",2,"rhetoric")
display(HTML("<h2>criticisms</h2>"))
tka.f_display_html_with_heading(globals(),"crt",3)

display(HTML("hi"))



```



