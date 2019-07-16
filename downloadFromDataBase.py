from proxy import Proxy;
from fileDao import fileDAO;
import urllib3;
import os;
class FromTB:
    _rootPath = "D:\\ppt\\"
    _fileSperator = "\\"
    _map = {1:'PPT文件',2:"PPT背景",3:"PPT素材",4:"字体",5:"PPT图表"}
    def downloadFromTb_file(self):
        results = fileDAO().selectAllFile();
        for result in results:
            groupName = result[1]
            fileName = result[2]
            type = result[3]
            downloadUrl = result[4]
            if downloadUrl.__contains__(".rar"):
                dirPath = self._rootPath + self._map[int(type)] + self._fileSperator + groupName
                if not os.path.exists(dirPath):
                    os.makedirs(dirPath)
                print(downloadUrl)
                temp = urllib3.PoolManager().request("GET", downloadUrl)
                print("下载:" + groupName + ":" + fileName);
                with open(dirPath + self._fileSperator + fileName + ".rar", "wb") as f:
                    f.write(temp.data)
                f.close()
FromTB().downloadFromTb_file();