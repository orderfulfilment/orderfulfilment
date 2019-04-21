import pymysql
con = pymysql.connect(host='192.168.1.10', user='lik', password='lik', db='project', port=3306)
cu = con.cursor()