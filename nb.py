#
# Will open defined text file, append a new line with date and input strng
# Args: (text)
#
import os
from datetime import datetime
import sys

FILE_LOCATION = r"C:\to do"
FILE_NAME = "todo.txt"

def appendText(text):
    path = os.path.join(FILE_LOCATION, FILE_NAME)
    now = datetime.now()
    date_string = now.strftime("%d/%m/%Y %H:%M")
    try:
        with open(path, "a") as f:
            f.write("\n" + date_string + " | " + str(text))
            print(date_string + " | " + str(text))
    except OSError:
        print("Problem writing to file! Please try again")
    except:
        print("error")


if str(' '.join(sys.argv[1:])) != "":
    appendText(str(' '.join(sys.argv[1:])))
else:
    print("Please write text!")
