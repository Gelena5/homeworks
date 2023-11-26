name = [input("name: ")]
x = 0

while True:
   name.append(input("Enter names: "))
   if "stop" in name:
       name.remove("stop")
       break
   
   x += 1
if x == 1:
   print(name[0], "liked your post.")
if x == 2:
   print(name[0], name[1], "liked your post.")
if x == 3:
   print(name[0], name[1], name[2], "liked your post.")
if x >= 4:
   print(name[0],"and",x-1, "liked your post.")