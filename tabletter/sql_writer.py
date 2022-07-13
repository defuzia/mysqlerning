import pymysql
from tabletter.config import host, port, user, password, schema
import pandas as pd

try:
    con = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=schema
    )
    with con:
        cur = con.cursor()

        cur.execute("""SELECT * FROM main_personal;
        """)

        # for i in cur:
        #     result.append(i)
        table = pd.DataFrame(cur)

        con.commit()

except Exception as ex:
    print(ex)
