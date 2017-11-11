import sys 
import os.path

name = sys.argv[1] + '.py'

if not os.path.isfile(name):

    with open(name, 'a') as f:
        s = ("\"\"\"\n"  
             "Author: Fernando Collado\n"
             "Github: ForFer\n"
             "Hackerrank: F0rz4\n"
             "\"\"\"\n"
             "\n"
             "\"\"\"\n"
             "\n"
             "\"\"\""
             )
        f.write(s)

    print("All ok\n")

else:
    print("file with that name already exists, try another")
