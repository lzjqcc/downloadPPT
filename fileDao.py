import pymysql;

class fileDAO:
    _conn = pymysql.connect("localhost","root","941005",'file')
    _cursor = _conn.cursor()
    sql = "insert into tb_file (group_name,file_name,download_url, type) values (%s,%s,%s,%s)";

    def insertPPTFile(self,group, fileName, downLoadURL):
        self._cursor.execute(self.sql, [group, fileName, downLoadURL, 1]);
        self._conn.commit();

    def insertPPTImageFile(self, group, fileName, downLoadURL):
        self._cursor.execute(self.sql, [group, fileName, downLoadURL, 2]);
        self._conn.commit()

