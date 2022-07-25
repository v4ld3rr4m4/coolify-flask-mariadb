from  flask import Flask
import mysql.connector as mariadb

app=Flask(__name__)



@app.get("/")
def index():
    return "XOpa MUndo"

@app.get("/coolify/create")
def coolify():
    conn = mariadb.connect(
                            host="cl605frrq1606698c3ldkk9bph8t",
                            port="9000", 
                            user="cl605frro00dp0old1kw84kld", 
                            password="TGHDGsn4wKdsuNRfEFSfmytd", 
                            database="cl605frrp00dr0old36z131ie"
                          )
    cursor = conn.cursor()
    cursor.execute("create table xopa_mundo(id int)")
    cursor.execute("insert into xopa_mundo(id) values(300)")
    cursor.execute("insert into xopa_mundo(id) values(300)")
    cursor.execute("select id from xopa_mundo")
    arr1 = []
    for idx in cursor:
        arr1.append(idx)
    conn.close()
    return str(arr1)



if __name__ == "__main__":
    app.run(debug=True)
