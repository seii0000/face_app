import os

def clean(d):
 i=0   
 listing = os.listdir(d+"/")
 for file in listing:
  #print(file)
  for k in file:
   if k==".":
         i=1
   if i>=1 and k=="n"or k=="d":  
    i=i+1
   if i>=1 and k=="p" or k=="a":  
    i=i+1
   if i>=1 and k=="y"or k=="t":  
    i=i+1
  if i==4:
   base_path = "D:\\Face-recognition-based-attendence-system-master\\Face-recognition-based-attendence-system-master\\"

   # Tạo đường dẫn hoàn chỉnh
   full_path = os.path.join(base_path, d, file)

   # Xóa tệp
   os.remove(full_path)
   i=0

    