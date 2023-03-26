#!C:\Users\iiha7\anaconda3\python.exe

import pandas as pd
import webbrowser

if __name__ =="__main__":
    # Load the data from the text file into a Pandas DataFrame
    # Load the data from the text file into a Pandas DataFrame
    df = pd.read_csv('data.txt', delimiter=' ')

    # Convert the DataFrame to an HTML table with cells for each value in <tr> <td> <td> format
    html_table = df.to_html(index=False, render_links=False, classes='table table-striped', escape=False)
    # Add Bootstrap CSS and JS to the HTML table
    html_table = """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    """ + html_table

    # Save the HTML table to a file
    with open("table.html", "w") as f:
        f.write(html_table)

    # Open the table.html file in the default web browser
    webbrowser.open("table.html")
