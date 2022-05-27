import os

for root, dirs, files in os.walk("./"):
    for file_name in files:
        res = []
        if file_name.endswith(".txt"):
            with open(file_name, "r") as f:
                lines = f.readlines()
                for line in lines:
                    words = line.split(" ")
                    words[0] = "0"
                    line = " ".join(words)
                    res.append(line)
            with open(file_name, "w") as f:
                for line in res:
                    f.write(line)                    
