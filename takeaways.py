from IPython.display import display, Markdown, HTML, SVG
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO
import notation as ntn
import functions as fnc


def f_css():
    HTML("""<style>
         h1, h2 {
             font-weight: 1000 !important;
             color: black;
             }
    
         h1 {
             text-decoration: underline;
             }
         </style>
    """)


