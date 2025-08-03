# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
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
import sys
import os



# %%
sys.path.append(os.path.abspath("/home/chris-jakoolit/Mathematics/_templates"))
from common_imports import *





# %%
tka.f_css()






# %%
display(HTML(fnc.f_md_to_html("./_md/the_suppy_of_money.md")))
