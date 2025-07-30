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



# %%
wrd_V_vector_space = "We define " + ntn.not_V + " as a <a href='./vector-spaces-clean.html'>vector space</a>."
#----------------------------------------------------------
#----------------------------------------------------------
wrd_eigen_intro = "<h2>Eigenvectors and Eigenvalues</h2>"
wrd_v_TV_parralell = ntn.not_Tv + " & " + ntn.not_v + " are parallel if: " + .ntn.eqn_tv_lamdav
wrd_lamda_eigenvalue = ntn.not_lamda + " is an eigenvalue of " + ntn.not_T

wrd_aka = "<h2>aka</h2>"+"<p>Eigenvalues are also known as proper values or characteristic values.</p>"+"<p>Eigenvectors are also known as proper vectors or characteristic vectors</p>"


# %%
display(HTML('<a href="https://christopherpaine.github.io/Mathematics">link home</a>'))
display(HTML(wrd_V_vector_space))



display(HTML(wrd_eigen_intro))
display(HTML(ntn.not_v_exists_in_v))
display(HTML(wrd_v_TV_parralell))
display(HTML(wrd_lamda_eigenvalue))
display(HTML(wrd_aka))



