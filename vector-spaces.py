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
not_V = r"\(V\)"
not_T = r"\(T\)"
not_transformation = r"\(T: V \rightarrow V\)"
not_v_exists_in_v = r"\(\mathbf{v} \in V\)"
not_Tv = r"\(T\mathbf{v}\)"
not_v = r"\(\mathbf{v}\)"
not_lamda = r"\(\lambda\)"


eqn_tv_lamdav = r"\(T\mathbf{v}=\lambda \mathbf{v}\)"
eqn_associativity_of_additions = r"\((\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})\)"




# %%
wrd_vector_spaces_intro = "<h2>Vector Spaces</h2>"\
        + "<p>A vector space is is a set of vectors with two operations:</p>"\
        + "\
        <ul>\
            <li>addition</li>\
            <li>scalar multiplication</li>\
        </ul>\
        "\
        + "These operations satisfy the following axioms:" + """

<table border="1">
  <tr>
    <th style="width: 30%;>Name of Vector Space Axiom</th>
    <th style="width: 50%;">Explanation</th>
    <th>Mathematical Notation</th>
  </tr>
  <tr>
    <td>Closure under Addition</td>
    <td style="width: 50%;">The sum of any two vectors is also a vector in the same space.</td>
    <td>\(\mathbf{u} + \mathbf{v} \in V\)</td>
  </tr>
  <tr>
    <td>Associativity of Addition</td>
    <td style="width: 50%;">The way in which vectors are grouped in addition does not change the result.</td>
    <td>\((\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})\)</td>
  </tr>
  <tr>
    <td>Identity Element of Addition</td>
    <td style="width: 50%;">There exists a zero vector such that adding it to any vector does not change the vector.</td>
    <td>\(\mathbf{v} + \mathbf{0} = \mathbf{v}\)</td>
  </tr>
  <tr>
    <td>Inverse Elements of Addition</td>
    <td style="width: 50%;">For every vector, there exists an inverse vector such that their sum is the zero vector.</td>
    <td>\(\mathbf{v} + (-\mathbf{v}) = \mathbf{0}\)</td>
  </tr>
  <tr>
    <td>Closure under Scalar Multiplication</td>
    <td style="width: 50%;">The product of a scalar and a vector is also a vector in the same space.</td>
    <td>\(a\mathbf{v} \in V\)</td>
  </tr>
  <tr>
    <td>Distributive Property of Scalar Multiplication with respect to Vector Addition</td>
    <td style="width: 50%;">Scalar multiplication distributes over vector addition.</td>
    <td>\(a(\mathbf{u} + \mathbf{v}) = a\mathbf{u} + a\mathbf{v}\)</td>
  </tr>
  <tr>
    <td>Distributive Property of Scalar Multiplication with respect to Field Addition</td>
    <td style="width: 50%;">Scalar addition distributes over scalar multiplication.</td>
    <td>\((a + b)\mathbf{v} = a\mathbf{v} + b\mathbf{v}\)</td>
  </tr>
  <tr>
    <td>Associativity of Scalar Multiplication</td>
    <td style="width: 50%;">The way in which scalars are grouped in multiplication does not change the result.</td>
    <td>\(a(b\mathbf{v}) = (ab)\mathbf{v}\)</td>
  </tr>
  <tr>
    <td>Identity Element of Scalar Multiplication</td>
    <td style="width: 50%;">Multiplying a vector by one does not change the vector.</td>
    <td>\(1\mathbf{v} = \mathbf{v}\)</td>
  </tr>
</table>
"""



# %%
wrd_V_vector_space = "We define " + not_V + " as a vector space."
#----------------------------------------------------------

# %%
display(HTML('<a href="https://christopherpaine.github.io/Mathematics">link home</a>'))
display(HTML(wrd_vector_spaces_intro))





