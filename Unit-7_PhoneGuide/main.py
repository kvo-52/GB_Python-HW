from os.path import exists
from creat_file import creating
from write_file import writing_scv, writing_txt
# from User_data import get_info as gi 


path = 'Guide.csv'
valid = exists(path)
if not valid:
    creating()


writing_scv()
writing_txt()