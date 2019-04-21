import pymysql
class conn:
    def __init__(self):
        pass


    def nonreturn(self,a):

        print(a)
        self.con = pymysql.connect(host='localhost', user='root', password='', db='project', port=3306)
        self.cu = self.con.cursor()
        self.cu.execute(a)
        self.con.commit()
        return self.cu.lastrowid

    def mid(self,a):
        self.con = pymysql.connect(host='localhost',  user='root', password='', db='project', port=3306)
        self.cu = self.con.cursor()
        self.cu.execute(a)
        f=self.cu.fetchone()
        print(f)
        if f[0] is None:
            id=1
        else:
            id=f[0]+1
        return id
    def selectall(self,a):
        self.con = pymysql.connect(host='localhost',  user='root', password='', db='project', port=3306)
        # self.con = pymysql.connect(host='localhost', user='root', password='', db='project1', port=3306)
        self.cu = self.con.cursor()
        self.cu.execute(a)
        self.res=self.cu.fetchall()
        return (self.res)
    def selectalljson(self,a):
        self.con = pymysql.connect(host='localhost', user='root', password='', db='project', port=3306)
        # self.con = pymysql.connect(host='localhost', user='root', password='', db='project1', port=3306)
        self.cu = self.con.cursor()
        self.cu.execute(a)
        self.res=self.cu.fetchall()
        return (self.res,self.cu)
    def selectone(self, a):
        self.con = pymysql.connect(host='localhost', user='root', password='', db='project', port=3306)
        # self.con = pymysql.connect(host='localhost', user='root', password='', db='project1', port=3306)
        self.cu = self.con.cursor()
        self.cu.execute(a)
        self.res = self.cu.fetchone()
        return (self.res)

    def jsonselect(self,a):
        self.con = pymysql.connect(host='localhost', user='root', password='', db='project', port=3306)
        # self.con = pymysql.connect(host='localhost', user='root', password='', db='project1', port=3306)
        self.cu = self.con.cursor()
        self.cu.execute(a)
        json_data=[]

        res= self.cu.fetchall()
        if res is not None:
            row_headers = [x[0] for x in self.cu.description]

            for result in res:
                json_data.append(dict(zip(row_headers, result)))

            print(json_data)
        return json_data

