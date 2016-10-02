import shutil, os, stat, time, datetime
from datetime import timedelta
import glob

today = datetime.datetime.today()
last24Hours = str(today - timedelta(hours=24))

path = ('C:/Users/Administrator/Desktop/a')

for file in glob.glob(os.path.join(path, '*.txt')):
    epochDate =  os.path.getmtime(file)
    modifiedDate = datetime.datetime.fromtimestamp(int(epochDate)).strftime('%Y-%m-%d %H:%M:%S')
    if modifiedDate > last24Hours:
        shutil.move(file,'C:/Users/Administrator/Desktop/b')


