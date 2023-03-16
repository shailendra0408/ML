# ! Dynamic Query


def dynamicQuery(tableName, start, endLimit, colList, valList, oprList, matchList):
    qsList = []
    for i in range(0, len(colList)):
        if i == len(colList)-1:
            vals = valList[i] if type(
                valList[i]) != str else "'" + str(valList[i]) + "'"
            qsList.append(colList[i] + " " + oprList[i] + " " + f"{vals}")
        else:
            vals = valList[i] if type(
                valList[i]) != str else "'" + str(valList[i]) + "'"
            qsList.append(colList[i] + " " + oprList[i] +
                          " " + vals + " " + matchList[i] + " ")

    sql = "SELECT " + ", ".join(colList) + " FROM " + tableName + \
        " WHERE " + "".join(qsList) + " limit "+start+","+endLimit
    print("Query ------------------------ \n", sql)
    return sql

# ! Response


def tb_query():
    q2 = dynamicQuery(tableName="location_testdb", start="0", endLimit="20", colList=['crop', 'speaker'],
                       valList=['bajra', 0], oprList=["=", "="], matchList=["and"])

    #q1 = "SELECT crop, speaker FROM location_testdb WHERE crop = 'bajra' and speaker = 0 limit 0,20"

    #q2 = ()
    print (q2)
    
    #(len(dbs), dbs)


if __name__ == '__main__':
    tb_query()
