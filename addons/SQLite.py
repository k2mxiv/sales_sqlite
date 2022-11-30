### <요구사항-2> 반영 ###
import sqlite3
import os
from pathlib import Path

#-------------mySQL 연결 끝
#-------------함수 시작
def servConnect(sel, sql) : ### <요구사항-3> 반영 ###
    path = Path(os.path.dirname(os.path.realpath(__file__))).parent
    conn = sqlite3.connect(f"{path}/sales_db.sqlite3")
    corr = conn.cursor()
    corr.execute(sql)
    if sel == 'alone' :
        None
    elif sel == 'commit' :
        conn.commit()
    elif sel == 'fetch' :
        rerult = corr.fetchall()
        corr.close()
        conn.close()
        return rerult
    corr.close()
    conn.close()
    
