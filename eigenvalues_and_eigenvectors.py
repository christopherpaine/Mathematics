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


# %%
not_V = r"\(V\)"
not_T = r"\(T\)"
not_transformation = r"\(T: V \rightarrow V\)"
not_v_exists_in_v = r"\(\mathbf{v} \in V\)"
not_Tv = r"\(T\mathbf{v}\)"
not_v = r"\(\mathbf{v}\)"
not_lamda = r"\(\lambda\)"


eqn_tv_lamdav = r"\(T\mathbf{v}=\lambda \mathbf{v}\)"

# %%
wrd_vector_spaces_intro = "<h2>Vector Spaces</h2>"
wrd_V_vector_space = not_V + " is a vector space."
wrd_linear_transformation_intro = "<h2>Linear Transformations</h2>"
wrd_T_linear_transformation = " is a linear transformation"
wrd_defn_linear_transformation = "A linear transformation is not a vector, but rather a function or mapping between two vector spaces that preserves the operations of vector addition and scalar multiplication."
wrd_v_TV_parralell = not_Tv + " & " + not_v + " are parallel if: " + eqn_tv_lamdav
wrd_lamda_eigenvalue = not_lamda + " is an eigenvalue of " + not_T


# %%
display(HTML(wrd_vector_spaces_intro))
display(HTML(wrd_V_vector_space))

display(HTML(wrd_linear_transformation_intro))


display(HTML(not_transformation + wrd_T_linear_transformation))
display(HTML(wrd_defn_linear_transformation))
display(HTML(not_v_exists_in_v))
display(HTML(wrd_v_TV_parralell))
display(HTML(wrd_lamda_eigenvalue))


# %%
A linear transformation is not a vector, but rather a function or mapping       
between two vector spaces that preserves the operations of vector addition and  
scalar multiplication. In mathematical terms, if ( T: V \rightarrow W ) is a    
linear transformation between vector spaces ( V ) and ( W ), then for any       
vectors ( \mathbf{u}, \mathbf{v} \in V ) and any scalar ( c ), the following    
properties hold:                                                                

 1 ( T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v}) )               
 2 ( T(c\mathbf{u}) = cT(\mathbf{u}) )                                          

While linear transformations themselves are not vectors, they can be represented
by matrices when considering finite-dimensional vector spaces.                  
