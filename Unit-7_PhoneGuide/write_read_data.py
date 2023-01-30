def write_file(data):
    with open('guide.csv','a', encoding = 'utf-8') as file:
        file.writelines(data)
          
def read_file():
    with open('guide.csv','r') as file:
        return file.readlines()