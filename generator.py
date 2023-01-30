import random

def generator_student():
    name=['Маша', 'Лиза', 'Сережа', 'Петя', 'Вася', 'Коля', 'Саша', 'Артем', 'Андрей']    
    sename=['Иванов', 'Петров', 'Сидоров', 'Тарасов', 'Кукушкин', 'Пушкин', 'Команин', 'Левашов']
    predmet= ['русский-язык', 'математика', 'английский-язык', 'билогия', 'химия', 'естествознание', 'история', 'ИЗО', 'физра']
    estimation = ['1', '2', '3', '4', '5']
    estimation_student=','.join(random.choice(estimation) for i in range (5))

    for i in range (101):
        key=random.randint(1,11)
        note_key=random.randint(1,101)
        value=''.join(random.choice(name)+" "+random.choice(sename)+" "+random.choice(predmet)+": "+estimation_student+' ' for i in range(1))
        student={key: value} 
        all_student={note_key: {student[key]}} 
        print (all_student)
    
def write_file(data):
    with open('student.csv','a') as file:
        file.writelines(data)    
    
    
write_file(generator_student()) 
print(generator_student())
