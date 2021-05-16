import mysql.connector as connector


#CRUD OPERATIONS
''' 
CREATE (INSERT)
READ (SELECT)
UPDATE
DELETE
'''


class Dbhelper:
    def __init__(self):
        self.con=connector.connect(host='localhost',port='3306',user='root',password='database@7.',database='pythontest')
        #whenever the program executed created IF NOT EXISTS. So if the table exists it will show the db table.
        query='CREATE TABLE if not exists user(userId int primary key,userName varchar(20),phone varchar(12))'
        #creating cursor. This will execute queries.
        cur=self.con.cursor()
        cur.execute(query)
        print('Table Created')
    
    #insert
    def insert_user(self,userid,username,phone):
        query="INSERT INTO user VALUES({},'{}','{}')".format(userid,username,phone)
        cur = self.con.cursor()
        cur.execute(query)
        #Commit means changing in database physically or really.
        #if we dont use commit() then it will only show output in cmd but the real db did not get changed. Thats why we have to use commit
        self.con.commit()
        print('User Saved To Database')

    #Fetch ALL
    def fetch_all(self):
        query='SELECT * FROM user'
        cur=self.con.cursor()
        cur.execute(query)
        for row in  cur:  
            print('User Id:',row[0])
            print('User Name:',row[1])
            print('Phone:',row[2])
            print()
            print()
    
    #Fetch One
    def fetch_one(self,id):
        query='SELECT * FROM user WHERE userId={}'.format(id)
        cur=self.con.cursor()
        cur.execute(query)
        for row in  cur:  
            print('User Id:',row[0])
            print('User Name:',row[1])
            print('Phone:',row[2])
    
    #Delete User
    def delete_user(self,id):
        query='DELETE FROM user WHERE userID={}'.format(id)
        cur=self.con.cursor()
        cur.execute(query)
        #Commit means it will delete the record in database physically or really.
        self.con.commit()
        print('User Record Deleted.')
    
    #Update
    def update_user(self,userid,newname,newphone):
        query="UPDATE user set userName='{}',phone='{}' WHERE userId={}".format(newname,newphone,userid)
        cur=self.con.cursor()
        cur.execute(query)
        #Commit means it will Update the record in database physically or really.
        self.con.commit()
        print('User Record Updated.')