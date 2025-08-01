from IPython.display import display, Markdown, HTML, SVG
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO
import notation as ntn
import markdown as mdn




def f_md_to_html(mdfile):
    # Read the markdown file
    with open(mdfile, 'r') as file:
        markdown_text = file.read()
    # Convert markdown to HTML
    html = mdn.markdown(markdown_text)
    return html



# HTML functions ################################################################################## #

def f_truncate_df(df, head=5, tail=5):
    n = df.shape[0]
    
    # Handle rows
    if n > head + tail:
        top_rows = df.iloc[:head, :]
        bottom_rows = df.iloc[-tail:, :]
        middle_row = pd.DataFrame(
            [['...'] * df.shape[1]], 
            index=['...'], 
            columns=df.columns
        )
        df = pd.concat([top_rows, middle_row, bottom_rows])

    # Handle columns
    n_cols = df.shape[1]
    if n_cols > head + tail:
        left_cols = df.iloc[:, :head]
        right_cols = df.iloc[:, -tail:]
        middle_col = pd.DataFrame(
            [['...']] * df.shape[0], 
            index=df.index, 
            columns=['...']
        )
        df = pd.concat([left_cols, middle_col, right_cols], axis=1)

    return df

def f_create_flex_columns(html1, html2, padding=0, flex1=1, flex2=1):
    """
    Create a two-column HTML layout with specified content, padding, and flex values.

    Args:
    html1 (str): HTML content for the first column.
    html2 (str): HTML content for the second column.
    padding (int, optional): Padding for each column. Default is 0.
    flex1 (int, optional): Flex value for the first column. Default is 1.
    flex2 (int, optional): Flex value for the second column. Default is 1.

    Returns:
    str: A string representing the HTML layout with two columns.
    """
    return f'''
    <div style="display: flex;">
        <div style="flex: {flex1}; padding: {padding};">
            {html1}
        </div>
        <div style="flex: {flex2}; padding: {padding};">
            {html2}
        </div>
    </div>
    '''


def f_create_styled_div(content, text_color='black', background_color='white', padding=0,border='1px solid #999'):
    """
    Create a styled HTML div element with specified content, text color, background color, and padding.

    Args:
    content (str): The HTML content to be placed inside the div.
    text_color (str, optional): The color of the text inside the div. Default is 'black'.
    background_color (str, optional): The background color of the div. Default is 'white'.
    padding (int, optional): Padding for the div. Default is 0.

    Returns:
    str: A string representing the HTML div element with inline CSS.
    """
    style = f"flex: 1; padding: {padding}px; background-color: {background_color}; border: {border};"
    return f'<div style="{style} color: {text_color};">{content}</div>'


def f_list_to_html_bullets(lst):
    """
    Converts a list of items into an HTML unordered list with bullet points.

    Args:
        lst (list): A list of items to be converted into HTML bullet points.

    Returns:
        str: A string representing the HTML unordered list with the items as bullet points.
    """
    html_list = "<ul>\n"
    for item in lst:
        html_list += f"  <li>{item}</li>\n"
    html_list += "</ul>"
    return html_list


def f_wrap_in_span(text, color):
    """
    Wraps the given text in an HTML <span> tag with the specified text color.

    Args:
    text (str): The text to be wrapped in a span.
    color (str): The color to be applied to the text.

    Returns:
    str: The HTML string with the text wrapped in a <span> tag with the specified color.
    """
    return f'<span style="color: {color};">{text}</span>'





def list_variables(caller_globals):                                            
     return [var for var in caller_globals if not var.startswith("__") and not callable(caller_globals[var])]                                                 


def combine_strings(string_list):
    return '<br>'.join(string_list)





def combine_strings_with_heading(string_list, header_level):
    if header_level < 2:
        header_level = 2
    header_tag = f"h{header_level}"
    string_list[0] = f"<{header_tag}>{string_list[0]}</{header_tag}>"
    return string_list[0] + string_list[1]+''.join(f'<br>{s}' for s in string_list[2:])


