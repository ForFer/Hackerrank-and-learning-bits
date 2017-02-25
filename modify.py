import os
import sys

def modify(sub):
    print(sub)
    print(os.listdir(sub))
    try:
        for filename in os.listdir(sub):
            if filename.endswith(".py") and not filename is not "modify.py": 
                with open(filename,'r') as f:
                    data = f.readlines()
                if 'Author'.lower() in data[1].lower():
                    if 'Hackerrank'.lower() not in data[3].lower():
                        print("file %s is being modified" % f)
                        s = "Hackerrank: F0rz4\n"
                        data.insert(3,s)
            
                    with open(filename, 'w') as f:
                        f.writelines(data)
            else:
                continue
    except:
        print("sub %s passed" % sub)
        pass


walk_dir = sys.argv[1]
#print(walk_dir)
#print(*os.walk(walk_dir))

for root, subFolder, files in os.walk(walk_dir):
    for sub in subFolder:
        modify(sub)
