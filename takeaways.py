from IPython.display import display, Markdown, HTML, SVG
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO
import notation as ntn
import functions as fnc


def f_css():
    display(HTML("""<style>
         h1, h2 {
             font-weight: 1000 !important;
             color: black;
             }
    
         h1 {
             text-decoration: underline; !important;
             }
         </style>
    """))

def f_display_html_with_heading(glob,prefix, heading_level):
    lst = [s for s in fnc.list_variables(glob) if s.startswith(prefix)]
    for html in lst:
        display(HTML(fnc.combine_strings_with_heading(eval(html,glob), heading_level)))

def f_convert_string_vars_to_htmls(glob,prefix, heading_level, content):
    display(HTML(f"<h{heading_level}>{content}</h{heading_level}>"))
    filtered_list = [s for s in fnc.list_variables(glob) if s.startswith(prefix)]
    for html in filtered_list:
        display(HTML(eval(html,glob)))


