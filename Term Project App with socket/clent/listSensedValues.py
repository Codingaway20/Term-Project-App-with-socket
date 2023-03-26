#!C:\Users\iiha7\anaconda3\python.exe
import pandas as pd
import webbrowser

if __name__ =="__main__":
    # Load the data from the text file into a Pandas DataFrame
    df = pd.read_csv('data.txt')

    # Convert the DataFrame to an HTML table
    html_table = df.to_html(index=False, justify='left', classes='table table-striped')

    # Save the HTML table to a file
    with open("table.html", "w") as f:
        f.write(html_table)

    # Create a CSS file that defines the styles for the table
    with open("table.css", "w") as f:
        f.write("table { border-collapse: collapse; width: 100%; }")
        f.write("th, td { border: 1px solid black; padding: 8px; text-align: left; }")
        f.write("th { background-color: #f2f2f2; }")

    # Create an HTML file that links to the CSS file and displays the table
    with open("index.html", "w") as f:
        f.write("<html><head>")
        f.write("<link rel='stylesheet' type='text/css' href='table.css'>")
        f.write("</head><body>")
        f.write("<h1>Table</h1>")
        f.write("<iframe src='table.html' width='1000' height='500'></iframe>")
        f.write("</body></html>")

    # Open the index.html file in the default web browser
    webbrowser.open("index.html")