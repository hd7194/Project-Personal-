import mysql.connector as M
import time
noc = M.connect(host='localhost',user='root',password='mypassword',database='Project')
cur = noc.cursor()
file = open('C:\\Users\Vaidehi M\PycharmProjects\pythonProject1\wordlist.txt','r')
if file(1) == 'a':
    print(file)
