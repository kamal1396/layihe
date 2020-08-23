# # Yeni tələbə əlavə edilməsi
# Tələbə koduna görə tələbə məlumatlarının silinməsi
# Tələbə koduna görə tələbə məlumatlarının dəyişdirilməsi
# Tələbə adına görə tələbə məlumatlarının göstərilməsi
# Bütün tələbə məlumatlarının göstərilməsi

students=[]
count__students=0
max_students=10
while count__students<max_students:
    userid=input("Tələbə kodu:")
    while True:
        if len(userid)==3 and userid.isdigit():
            break
        else:
            userid=input("Tələbə kodu: ")
    name=input("adınız:")
    surname=input("soyadınız: ")
    while True:
      mail=input("mailiniz: ")
      if('@' in mail):
        break
      else:
        print('maililiniz: ')
    phone=input('nömrəniz: ')
    while True:
      if len(phone)==9 and phone.isdigit():
          phone='+994'+phone
          break
    else:
      print('nömrəniz: ')
    count__students+=1
    students+=[userid,name,surname,mail,phone]
    
    
    userid_remove=input("Silmək istədiyin tələbə kodunu daxil et")
    print(students)
    for i in range(len(students)):
        userid__del = students[1][0]
        if userid__del == userid_remove:
            students.pop(i)
            print(students)
            


                            
                            
            
