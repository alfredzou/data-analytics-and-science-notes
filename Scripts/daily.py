# Schedule this code using https://www.pythonanywhere.com/

from datetime import datetime

with open(datetime.now().strftime("%X-%d-%m-%Y"), "w") as file:
    file.write("We automated this using Python and PythonAnywhere!")
