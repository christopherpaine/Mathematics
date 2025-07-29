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


# %%
not_identity_matrix = r"""\(
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
\)"""



# %%
wrd_identity_matrix = "<p>An identity matrix is a square matrix with ones on the main diagonal and zeros elsewhere, serving as the multiplicative identity in matrix algebra.</p>"       




# %%
display(HTML("<h2>Identity Matrix</h2>"))
display(HTML(wrd_identity_matrix))
display(HTML(not_identity_matrix))
display(HTML("<h2>Inverse Matrix</h2>"))
