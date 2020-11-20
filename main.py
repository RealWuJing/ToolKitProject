from toolkit.toolkit_cfg import toolkit_cfg
from mysql.join import join_sql
import threading

if __name__ == '__main__':
    # join_sql()
    join_sql_thread = threading.Thread(target=join_sql)
    join_sql_thread.start()
    # join_sql_thread.join()
    # print('main end')
