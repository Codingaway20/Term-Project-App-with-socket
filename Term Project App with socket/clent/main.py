#!C:\Users\iiha7\anaconda3\python.exe
import time
def printHeader(title):
    print(("Content-type: text/html"))
    print("")
    print("<html><head><title>{}</title>".format(title))
    print("<link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css' integrity='sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z' crossorigin='anonymous>")
    print("<script src='https://code.jquery.com/jquery-3.5.1.slim.min.js' integrity='sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj' crossorigin='anonymous'></script>")
    print("<script src='https://cdn.jsdelivr.net/npm/[email protected]/dist/js/bootstrap.bundle.min.js' integrity='sha384-LtrjvnR4Twt/qOuYxE721u19sVFLVSA4hf/rRt6PrZTmiPltdZcI7q7PXQBYTKyf' crossorigin='anonymous'></script>")
    print("<script src='show.js'>")
    print("</script>")
    print("</head><body>")

def printFooter():
    print("</body></html>")


def generateDate():
    return time.strftime("%X")

def loadTable():
    date=generateDate()
    print("<div class='text-center'>")
    print("<h1 class='text-center'>Welcome to Fire Detection System!</h1>")
    print("<a class='table' href='table.py'>  <input type='submit' value='Start Sensing'/> </a>")
    print("<a class='table1' href='all.py'>  <input type='submit' value='List Previous Sensed Values'/> </a>")

    #print("<button id='showTableButton' class='btn btn-success' onclick='showTable()'>Start Sensing</button>")
    

    
if __name__ == '__main__':
    printHeader("An Automated Sensor-based Fire Detection System")
    loadTable()
    printFooter()