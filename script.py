import yaml
import os
import argparse
import time
import shutil
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('yaml', type=str, help='yamle-file path')
parser.add_argument(
    '-wd',
    type=str,
    default='./',
    help="path to working_directory (default: './')"
)
parser.add_argument(
    '-f',
    type=bool,
    default=0,
    help="request confirmation?  (default: 0)"
)


args = parser.parse_args()



def err():
    print('error in the yaml file, check the correctness of the rules')
    exit()

def is_older(path, age):
    delta = time.time()-os.path.getmtime(path)
    if age[-1] == 'd':
        delta = delta//60//60//24
    else:
        err()
    return delta > int(age[:-1])


def check_if(ifd, name):
    if 'maj' in ifd:
        if(ifd['maj']=='test' and name.split('.')[2]=='0'): return 0
        if(ifd['maj']=='release' and name.split('.')[2]!='0'): return 0
    if 'age' in ifd:
        if not is_older(args.wd+'/'+name, ifd['age']): 
            return 0
    return 1

def just_do_it(what_to_do, where_do):
    for task in what_to_do:
        if task == 'delrep':
            if what_to_do[task]==1:
                del_object(where_do)
                return 0
        if task == 'delmask':
            path = Path()
            files = list(path.rglob(where_do+'/'+what_to_do[task]))
            for file in files:
                file = str(file)
                del_object(file)
        if task == 'delage':
            del_age(what_to_do[task]['age'], where_do+'/'+what_to_do[task]['path'])

def del_age(age, path):
    ls = os.listdir(path)
    for file in ls:
        if is_older(path+'/'+file, age):
            del_object(path+'/'+file)
    ls = os.listdir(path)
    for file in ls:
        if os.path.isdir(path+'/'+file):
            del_age(age, path+'/'+file)

def del_object(obj):

    if os.path.exists(obj+'/'):
        if args.f==1:
            print('delete a directory? '+obj+' [Y/n]')
            if input()!='n':
                shutil.rmtree(obj)
        else:
            shutil.rmtree(obj)
    elif os.path.exists(obj):
        if args.f==1:
            print('delete a file? '+obj+' [Y/n]')
            if input()!='n':
                os.remove(obj)
        else:
            os.remove(obj)
    else:
        print('file or directory not found')

with open(args.yaml) as fh:
    data = yaml.load(fh, Loader=yaml.FullLoader)


try:
    for rule in data:
        rule = rule['rule']
        ver = os.listdir(args.wd)
        for rep in ver:
            
            if check_if(rule['if'], rep):
                just_do_it(rule['do'], args.wd+'/'+rep)


except:
    err()

# Бонус

import pymysql
try: 
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='my-secret-pw',
                                database='devops',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
except:
    print('mysqly connect error')

try:  
    with connection.cursor() as cursor: 
        sql = "DELETE FROM reps" 
        cursor.execute(sql)
        connection.commit()
        ver = os.listdir(args.wd)
        for rep in ver:
            d = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(os.path.getmtime(args.wd+'/'+rep)))
            s = os.path.getsize(args.wd+'/'+rep)
            sql = "INSERT INTO reps(version, modified, size) VALUES ('"+rep+"','"+d+"','"+str(s)+"')" 
            cursor.execute(sql) 
            connection.commit()
finally:
    # Закрыть соединение (Close connection).      
    connection.close()