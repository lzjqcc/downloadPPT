import random
from datetime import datetime

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
    def insertFileTemplate(self,size,groupId,tagId,fileFormat, fileName):
        selectSql = 'select * from tb_file_template where name = %s';
        self._cursor.execute(selectSql, [fileName]);
        results = self._cursor.fetchall();
        if len(results) > 0:
            return results[0][0];
        sql = "insert into tb_file_template (group_id, tag_id, file_size,file_format, insert_time, update_time, name) value(%s,%s,%s,%s,%s, %s, %s)";
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S");
        self._cursor.execute(sql,[groupId, tagId, size, fileFormat, dt, dt, fileName])
    def insertTag(self, name, groupId):
        selectSql = 'select * from tb_tag where name = %s';
        self._cursor.execute(selectSql, [name]);
        results = self._cursor.fetchall();
        if len(results) > 0:
            return results[0][0];
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S");
        sql = "insert into tb_tag (name, group_id, insert_time, update_time) value (%s, %s, %s, %s)";
        self._cursor.execute(sql,[name, groupId, dt, dt])
        id = self._cursor.lastrowid;
        self._conn.commit();
        return id;
    def insertGroup(self, name):
        selectSql = 'select * from tb_group where name = %s';
        self._cursor.execute(selectSql, [name]);
        results = self._cursor.fetchall();
        if len(results) > 0:
            return results[0][0];
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S");
        sql = "insert into tb_group (name, insert_time, update_time ) value (%s, %s, %s)";
        self._cursor.execute(sql, [name, dt, dt])
        id = self._cursor.lastrowid;
        self._conn.commit();
        return id;
    def updateFileTemplateFileNum(self, fileNum, id):
        sql = "update tb_file_template set file_num = %s where id = %s";
        self._cursor.execute(sql, [fileNum, id])
        self._conn.commit();
    def insertImage(self, fileName, imageUrl):
        sql = "select file_num from tb_file_template where name = %s";
        self._cursor.execute(sql,[fileName]);
        results = self._cursor.fetchall();
        if results is None or len(results) == 0:
            return
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S");
        selectSQL = "select * from tb_image WHERE file_template_num =  %s";
        self._cursor.execute(selectSQL, [results[0][0]])
        images = self._cursor.fetchall();
        if images is None or len(images) ==0:
            insertSql = "insert into tb_image (file_template_num, url,insert_time,update_time) value (%s, %s, %s, %s)";
            print(results[0][0])
            self._cursor.execute(insertSql, [results[0][0], imageUrl, dt, dt]);
            self._conn.commit();


