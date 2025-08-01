# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent,md
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
# imports
from IPython.display import display, Markdown, HTML, SVG
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO
import notation as ntn
import functions as fnc
import takeaways as tka


# %%
tka.f_css()


# %%
# GRAMMAR STATEMENTS 
grm_3_functions_money = "3 functions of money: store of wealth; medium of exchange;means of evaluation; means of establishing future value"

# %%
# RHETORICAL STATEMENTS 
rht_changes_in_money = "It is generally recognised that changes in the amount of money can have a powerful effect on all the major macroeconomic indicators, such as inflation, unemployment, economic growth, interest rates, exchange rates and the balance of payments. "






display(HTML("<h1>Rough notes on Sloman Economics Banking Money and Interest Rates section</h1>"))
tka.f_convert_string_vars_to_htmls(globals(),"grm",2,"grammar")
tka.f_convert_string_vars_to_htmls(globals(),"rht",2,"rhetoric")
