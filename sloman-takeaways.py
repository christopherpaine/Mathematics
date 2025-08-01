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
grm_national_income = "national income is value of nations output per year"
grm_stock_and_flow= "national income is a flow concept.  money supply is a stock concept"
grm_3_functions_money = "3 functions of money: store of wealth; medium of exchange;means of evaluation; means of establishing future value"
grm_financial_intermediaries = "Financial intermediaries The general name for financial institutions (banks, building societies, etc.) which act as a means of channelling funds from depositors to borrowers."
grm_matruity_transformation = "This process whereby financial intermediaries lend for longer periods of time than they borrow is known as maturity transformation ."


# %%
# LOGIC LISTS
lgc_risk_maturity_transformation = [
"maturity transformation creates risk for financial intermediaries", 
"mismatch of assets and liabilities on their balance sheet",
"risk needs managing",

]

# %%
# RHETORICAL STATEMENTS 
rht_changes_in_money = "It is generally recognised that changes in the amount of money can have a powerful effect on all the major macroeconomic indicators, such as inflation, unemployment, economic growth, interest rates, exchange rates and the balance of payments. "






display(HTML("<h1>Rough notes on Sloman Economics Banking Money and Interest Rates section</h1>"))
tka.f_convert_string_vars_to_htmls(globals(),"grm",2,"grammar")
display(HTML("<h2>logic</h2>"))
tka.f_display_html_with_heading(globals(),"lgc",3)
tka.f_convert_string_vars_to_htmls(globals(),"rht",2,"rhetoric")
