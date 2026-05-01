print ("YONGZZ!" )

level = 1
score = 0

print ("start level:" , level)

# level 1
print ("\nlevel 1: Easy add")
answer = int(input("what is 5+3? "))

if answer == 8 :
   print ("CORRECT! ")
   score += 10
   level += 1
else:
    print ("WRONG! ")

print ("score:", score)
print ("level:", level)

# level 2
print ("\nlevel 2: multiplication")
answer = int(input("what is 9*9? "))

if answer == 81 :
   print ("CORRECT! ")
   score += 10
   level += 1
else:
    print ("WRONG! ")

print ("score:", score)
print ("level:", level)

# level 3
print ("\nlevel 3: Brain  test")
answer = int(input("what is 9/9? "))

if answer == 1 :
   print ("CORRECT!! ")
   score += 10
   level += 1
else:
    print ("wrong!! ")

print ("score:", score)
print ("level:", level)

#level 4
print ("\nlevel 4: hard level")
answer = int(input(" 1.what is 100*10 ? "))
answer = int(input(" 2.what is 100/10? "))

if answer == 1000 : 
   answer == 20 
   print ("CORRECT!! ")
   score += 1
   level += 1
else:
    print ("wrong!! ")

print ("score:", score)
print ("level:", level)

#level 5
print ("\nlevel 5: mixed math") 
answer = int(input("what is (35/5)*7 ? "))

if answer == 49 :
   print ("CORRECT!! ")
   score += 10
   level += 1
else:
    print (" wrong!! ") 

print (" score:", score)
print (" level:", level)


