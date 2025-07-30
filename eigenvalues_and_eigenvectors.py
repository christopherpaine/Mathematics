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
wrd_linear_transformation_intro = "<h2>Linear Transformations</h2>"
wrd_T_linear_transformation = "We define " + ntn.not_transformation + " as a linear transformation that preserves the vector space."
wrd_defn_linear_transformation = "A linear transformation is a function or mapping between two vector spaces that preserves the operations of vector addition and scalar multiplication."
#----------------------------------------------------------
wrd_eigen_intro = "<h2>Eigenvectors and Eigenvalues</h2>"
wrd_v_TV_parralell = ntn.not_Tv + " & " + ntn.not_v + " are parallel if: " + .ntn.eqn_tv_lamdav
wrd_lamda_eigenvalue = ntn.not_lamda + " is an eigenvalue of " + ntn.not_T

wrd_aka = "<h2>aka</h2>"+"<p>Eigenvalues are also known as proper values or characteristic values.</p>"+"<p>Eigenvectors are also known as proper vectors or characteristic vectors</p>"


# %%
display(HTML('<a href="https://christopherpaine.github.io/Mathematics">link home</a>'))
display(HTML(wrd_V_vector_space))
display(HTML(wrd_linear_transformation_intro))


display(HTML(wrd_defn_linear_transformation))
display(HTML(wrd_T_linear_transformation))



display(HTML(wrd_eigen_intro))
display(HTML(ntn.not_v_exists_in_v))
display(HTML(wrd_v_TV_parralell))
display(HTML(wrd_lamda_eigenvalue))
display(HTML(wrd_aka))


## %%
#A linear transformation is not a vector, but rather a function or mapping       
#between two vector spaces that preserves the operations of vector addition and  
#scalar multiplication. In mathematical terms, if ( T: V \rightarrow W ) is a    
#linear transformation between vector spaces ( V ) and ( W ), then for any       
#vectors ( \mathbf{u}, \mathbf{v} \in V ) and any scalar ( c ), the following    
#properties hold:                                                                
#
# 1 ( T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v}) )               
# 2 ( T(c\mathbf{u}) = cT(\mathbf{u}) )                                          
#
#While linear transformations themselves are not vectors, they can be represented
#by matrices when considering finite-dimensional vector spaces.                  
