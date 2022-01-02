import numpy as np
from lexer import ds
def exe_select(columns_name,datasource,join,whereCond,group_Col,having,order,limit):
    
    print("import pandas as pd")
    print("import time")


    # starting time
    print("start = time.time()")


    datasource = datasource[0]["name"]
    col_list = []
    for x in columns_name:
        col_list.append(x["name"])        
        columns_name = col_list


    print( f'df = pd.read_csv("{datasource}.csv")')
    #print(columns_name)  




    ## ---------------  Handle  SELECT  ------------------------ 
    if(whereCond==[] and columns_name != []  and join ==[]  and  group_Col == [] and having==[]  and order==[]  and limit==[] ): 
        if(columns_name[0] != "*"):
            print(f"print(df[{columns_name}])")
        else:
            print("print(df)")



    # handle where 
    if(columns_name != []  and join ==[]  and whereCond != [] and group_Col == [] and having==[] and order==[] and limit==[] ): 
        #print (whereCond)
        print(f"df = df.loc[df['{whereCond[0]['name']}'] {whereCond[0]['compare']}'{whereCond[0]['value']}', {columns_name}]")
        print("print(df)")

    # handle GROUPBY Without Where 
    if(columns_name != []  and join ==[]  and whereCond == [] and group_Col != [] and having==[] and order==[] and limit==[] ):  
        print(f"df.loc[:, {columns_name} ].groupby({group_Col}).sum()")



    # handle GROUPBY with Where 
    if(columns_name != []  and join ==[]  and whereCond != [] and group_Col != [] and having==[] and order==[] and limit==[] ): 
        print(f"df.loc[df['{whereCond[0]['name']}'] {whereCond[0]['compare']}'{whereCond[0]['value']}', {columns_name} ].groupby({group_Col}).sum()")

    # handle order by with Where 
    #df[{columns_name}]
    if(columns_name != []  and join ==[]  and whereCond == [] and group_Col == [] and having==[] and order!=[] and limit==[] ):
        order_Col= (order[0]['name'])
        if (order[0]['type'] =='ASC'):
            print(f"df[{columns_name}].sort_values(by=['{order_Col}'], ascending=True).drop_duplicates()")
        elif (order[0]['type'] =='DESC'):
            print(f"df[{columns_name}].sort_values(by=['{order_Col}'], ascending=False).drop_duplicates()")

    print("end = time.time()")
    print("print(f'Runtime of the query is {end - start}')")

def exe_update(columns_name,datasource,whereCond):
    datasource = datasource[0]["name"]
    print("import time")
    print("import numpy as np")
    print("import pandas as pd")
    # starting time
    print("start = time.time()")
    print( f'df = pd.read_csv("{datasource}.csv")')
    if(columns_name != [] and whereCond != [] ):
   
        col = columns_name[0]["name"]
        new_val = columns_name[0]["value"]

        print(f"df['{col}'] = np.where(df['{whereCond[0]['name']}'] {whereCond[0]['compare']} '{whereCond[0]['value']}', '{new_val}', df['{col}'])")

    print("end = time.time()")
    print("print(f'Runtime of the query is {end - start}')")

def exe_delete(datasource,whereCond):
    print("import time")
    print("import pandas as pd")
    # starting time
    print("start = time.time()")
    datasource = datasource[0]["name"]
    print( f'df = pd.read_csv("{datasource}.csv")')
    print(f"df = df.drop(np.where(df['{whereCond[0]['name']}'] {whereCond[0]['compare']} '{whereCond[0]['value']}')[0])")
    print("end = time.time()")
    print("print(f'Runtime of the query is {end - start}')")

def exe_insert(columns_name,datasource,new_col):
    print("import time")
    print("import pandas as pd")
    # starting time
    print("start = time.time()")
    # print (columns_name)
    # print (datasource)
    #print (new_col)

    cols_list = []
    for x in columns_name:
        cols_list.append(x["name"])        
    
    #print(cols_list)


    new_cols = []
    for x in new_col:
        for y in x:
            new_cols.append(y)       
    
    datasource = datasource[0]["name"]
    #print(new_cols) 
    print(f"data = pd.DataFrame([{new_cols}])")
    print(f"data.to_csv('{datasource}.csv', mode='a',index=False,header=False)")
    
    # print(f"data = pd.DataFrame(list(zip({new_cols})), columns=[{cols_list}])")
    # print(f"data.to_csv({datasource}, mode='a')")
    print("end = time.time()")
    print("print(f'Runtime of the query is {end - start}')")


###################33   sqlite #################3
def exe_sqlite(query,ds):
    #obj = cls_DS_Sqlite()
    #datasource = datasource[0]["name"]
    print("import time")
    print("import pandas as pd")
    print('import sqlite3')
    # starting time
    print("start = time.time()")
    print (f"conn = sqlite3.connect('{ds}')")
    # conn = obj.open_DS(datasource)
    print (f"df = pd.read_sql_query('{query}', conn)")
    print("print(df)")

    print("conn.close()")
    print("end = time.time()")
    print("print(f'Runtime of the query is {end - start}')")
    # print(data)
    # obj.close_DS()
