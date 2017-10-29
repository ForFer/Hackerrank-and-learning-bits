import sys 

name = sys.argv[1] + '.py'

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
