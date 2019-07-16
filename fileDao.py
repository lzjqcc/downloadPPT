import pymysql;


class fileDAO:
    _conn = pymysql.connect("localhost", "root", "941005", 'file')
    _cursor = _conn.cursor()
    _insertSQL = "insert into tb_file (group_name,file_name,download_url, type) values (%s,%s,%s,%s)";
    _selectSQL = 'select * from tb_file;'
    def insertPPTFile(self, group, fileName, downLoadURL):
        self._cursor.execute(self._insertSQL, [group, fileName, downLoadURL, 1]);
        self._conn.commit();

    ## 背景图
    def insertPPTImageFile(self, group, fileName, downLoadURL):
        self._cursor.execute(self._insertSQL, [group, fileName, downLoadURL, 2]);
        self._conn.commit()

    ## PPT素材
    def insertPPTSUCaiFile(self, group, fileName, downLoadURL):
        self._cursor.execute(self._insertSQL, [group, fileName, downLoadURL, 3]);
        self._conn.commit()

    ## 字体
    def insertPPTFontFile(self, group, fileName, downLoadURL):
        self._cursor.execute(self._insertSQL, [group, fileName, downLoadURL, 4]);
        self._conn.commit()
        ## 字体
    ## 图表
    def insertPPTTableFile(self, group, fileName, downLoadURL):
        self._cursor.execute(self._insertSQL, [group, fileName, downLoadURL, 5]);
        self._conn.commit()
    def selectAllFile(self):
        self._cursor.execute(self._selectSQL)
        return self._cursor.fetchall();

