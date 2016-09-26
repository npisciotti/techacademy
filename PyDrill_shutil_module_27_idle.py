import shutil, os
shutil.move('C:/Users/Administrator/Desktop/a/1.txt','C:/Users/Administrator/Desktop/b')
shutil.move('C:/Users/Administrator/Desktop/a/2.txt','C:/Users/Administrator/Desktop/b')
shutil.move('C:/Users/Administrator/Desktop/a/3.txt','C:/Users/Administrator/Desktop/b')
shutil.move('C:/Users/Administrator/Desktop/a/4.txt','C:/Users/Administrator/Desktop/b')

for filename in os.listdir('C:/Users/Administrator/Desktop/b'):
    print filename

