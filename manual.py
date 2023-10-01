import os
import excel as r
def check(d):
 s = []  # initialized as an empty list to store the base filenames without extensions
 h="" # initialized as an empty string to temporarily store each character of the filename until a dot ('.') is encountered.
 i=0   
 listing = os.listdir(d+"/") # retrieves a list of filenames in the specified directory.
 for file in listing:
   f = str(file)
   print(file)
   for k in f:
    if k == '.':
        break
    h = h + k
   print(h)
   for k in f:
    if k == ".":
       i = 1
    valid_characters = "jpg"
    if i >= 1 and k in valid_characters:
        i += 1
    if i==4:
      s.append(h)
      h=""
      i=0 
 
    
 print(s)
 r.names(s,d)
#check("classa")      