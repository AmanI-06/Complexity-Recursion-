import os  
def disk(path):
    t=os.path.getsize(path)
    if os.path.isdir(path):
        
        for i in os.listdir(path):
            c=os.path.join(path,'FLAT textbook.pdf') 
            t+=disk(c)  
    return t
a=disk("C:/Users/lenovo/Downloads/Engineering books")
print(a)
print(os.listdir("C:/Users/lenovo/Downloads/Engineering books"))
print(os.path.isdir("C:/Users/lenovo/Downloads/Engineering books"))
for i in os.listdir("C:/Users/lenovo/Downloads/Engineering books"):
    print(os.path.getsize("C:/Users/lenovo/Downloads/Engineering books/"+ i))