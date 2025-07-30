# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent,md
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
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

# %%









# %%
display(HTML("<h1>Interest Rates</h1>"))
display(HTML("<h2>Zero Coupon Bond</h2>"))
display(HTML(ntn.not_zero_coupon_bond_price))
display(HTML(ntn.eqn_zero_coupon_price_spot_rate))
display(HTML("<h2>Spot Rate</h2>"))
display(HTML(ntn.not_spot_rate))
display(HTML(ntn.eqn_spot_rate_zero_coupon_price))
display(HTML(ntn.eqn_spt_rate_forward_rate))
display(HTML("<h2>forward rate</h2>"))
display(HTML(ntn.not_forward_rate + " is the forward rate at time t for delivery between T and S"))







