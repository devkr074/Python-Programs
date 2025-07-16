# Writing File in Python

print(f"\nAppend Content\n")
f=open("file.txt","a")
f.write("This is a new line added to the file.\n")
f=open("file.txt","r")
print(f.read())
print(f"\nOverwrite Content\n")
f=open("file.txt","w")
f.write("This line overwrites the previous content.\n")
f=open("file.txt","r")
print(f.read())
f.close()