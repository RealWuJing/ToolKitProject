import os
import time

from toolkit.toolkit_cfg import toolkit_cfg

# sql语句拼接
def join_sql():
    mysql_dir = toolkit_cfg()['mysql_dir']
    pre_listdir = set(os.listdir(mysql_dir))
    while 1:
        time.sleep(2)
        now_listdir = set(os.listdir(mysql_dir))
        dif_listdir = now_listdir - pre_listdir
        pre_listdir = now_listdir
        for mysql_sql in dif_listdir:
            mysql_sql_path = os.path.join(mysql_dir, mysql_sql)
            # print(mysql_sql_path)
            with open(mysql_sql_path, 'a+', encoding='utf8') as f:
                f.seek(0, 0)
                mysql = f.read()
                mysql = ' '.join([i.strip().split('\n')[0] for i in mysql.strip().split('\n')])
                print(mysql)
                f.writelines(f'\n\n{mysql}\n')

def join_sql2():
    mysql_dir = toolkit_cfg()['mysql_dir']
    now_listdir = set(os.listdir(mysql_dir))
    for mysql_sql in now_listdir:
        mysql_sql_path = os.path.join(mysql_dir, mysql_sql)
        # print(mysql_sql_path)
        with open(mysql_sql_path, 'a+', encoding='utf8') as f:
            f.seek(0, 0)
            mysql = f.read()
            mysql = ' '.join([i.strip().split('\n')[0] for i in mysql.strip().split('\n')])
            print(mysql)
            f.writelines(f'\n\n{mysql}\n')







