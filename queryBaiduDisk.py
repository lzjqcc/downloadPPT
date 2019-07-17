# coding=utf-8
import urllib3
import json;
import fileDao;
from urllib import parse
heads = {"Cookie":"PANWEB=1; BDCLND=YsBhsJn1aiARLQqnT3Mbu00pz4aMCebJ; BAIDUID=6C2C6E84AE208A098669142C55110FE3:FG=1; PSTM=1562734288; BIDUPSID=D5CE4C85C9376754A80DE1583763F187; SCRC=7690a83d031a138094ccdbaec8f56f67; BDUSS=mZtLWxQWjdGQ1NDU0ZSLUtjMU9YZFBBUExNMHZsRlBLeksxMndCR0VyM0NoVk5kSVFBQUFBJCQAAAAAAAAAAAEAAAAFLcZUvOGz1mluZ7XEzs~FowAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAML4K13C-Ctdd; STOKEN=133a89b47f247e373c8b3b597a5fc0b61534b4f451161acd6f895b67a43aaccc; MCITY=-179%3A; BDSFRCVID=N8IOJeC62lYW2GjwaOxXhwWy42KK_s7TH6aohRRScs71DTmahG_bEG0PDf8g0KubMX87ogKKKgOTHICF_2uxOjjg8UtVJeC6EG0P3J; H_BDCLCKID_SF=tJPqoCtKtCvHfP8k-tcH244Hqxby26n0QgJeaJ5n0-nnhp-Cqjob-jkFjUoK5fowbK08_fj-3C5pHULRy6CBe5O0jN-8qbO0MITQsJ5K54oqqPbmbtbsq4C85aRzex39WDTm_Dop2UoTSI56-j7N3-kW3puJJfnK2ann-pPKKlIKsDKlL6jB5U4j2xvub5OD3mkjbpnGfn02OPKzbhJE5-4syPRiKMRnWg5mKfA-b4ncjRcTehoM3xI8LNj405OTt2LEoD-KtCt-hDvp5n-_-tu_2xnXetJyaR3z0T6bWJ5TEPnjDU8-qjLW-H7OXxIOMncW-JkXJfjKsD5H-pD5y6TLjNufJTKDfR32WnTJ25rHDbTw5tI_-P4DegcGexRZ5mAqot3ptC8-DP3pehOPMb-i2HOK2xb-WJ7naIQqaKOMjtJj5MtWQPDJWGQ45fb43bRTapCy5KJvfJoKyjKVhP-UyPRMWh37Wm7lMKoaMp78jR093JO4y4Ldj4oxJp8eWJLH_I-XJIPbhKv65nt_5bLf5q3j-I62aKDsob32BhcqEIL4hhrRDx-q5ULOJPv3bav8_IocWM75MUbSj4QoMhDw0Ubet5oRQIjKBp37Kq5nhMJeb67JDMP0-4cvqTby523iab3vQpnzEpQ3DRoWXPIqbN7P-p5Z5mAqKl0MLIOkbC_mj5uMe5bQepJf-K6JbC3tQPJ2HJOoDDv8eMrcy4LdjG5QXl-H3KQf3l7yynnbSPImDxRvBnJW3-Aq54R3LHrg3-85tlbxDJjdQpnDQfbQ0-OhqP-jW5Ta2xPyJb7JOpvobUnxyMFdQRPH-Rv92DQMVU52QqcqEIQHQT3mDUTh-p52f60ftb-j3D; yjs_js_security_passport=9a7ea6d27d8bdc32c5ef5a6a4e5dea4e2c276b60_1563269005_js; H_PS_PSSID=1435_21121_18560_29522_29521_28518_29099_28835_29221; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=5; Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1562304690,1563162759,1563243947,1563345712; Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0=1563345712; PANPSC=16919121463836587262%3A0GmL5sexpYYmQeVWJHBUWjuv496EomYGiBmDr6LzmqGD1CMt3eRYe0aVilywkOnh4BuiUpmcP%2FXDR3cUdO7zPJpXVAfLeXHbigL09BK%2BQ4cjX5u0f7ESQi78Y3XhlnteGjf9pP26iQcBdMBFCejn%2BGPLhvADPmNCIermaD9w8EN3j5cyRAFOLeKEQjOY60ydAQwoaZBLaos%3D; cflag=13%3A3"}
http = urllib3.PoolManager();
http.headers = heads;
def request(pptDir):

    url = "https://pan.baidu.com/api/list?order=time&desc=1&showempty=0&web=1&page=1&num=1000&dir=" + parse.quote(pptDir) +"&t=0.36260855475680676&channel=chunlei&web=1&app_id=250528&bdstoken=a9e0d8c7211a24c44848d8f6a3deb084&logid=MTU2MzM0NjA1NDMxNjAuNjY1MTQzMzMwNTIyMjA4Mw==&clienttype=0&startLogTime=1563346054316"
    return http.request("GET", url)
def getPPTLists(pptDir):

    jsonObject = json.loads(request(pptDir= pptDir).data.decode('unicode_escape'));
    return jsonObject["list"]
def getName(name):
    str(name).encode()

groupLists = getPPTLists('/PPT');
for group in groupLists:
    groupPath = group["path"];
    groupName = group['server_filename'];
    groupId = fileDao.fileDAO().insertGroup(groupName)
    tagLists = getPPTLists(groupPath);
    for tag in tagLists:
        tagPath = tag['path'];
        tagName = tag['server_filename'];
        tagId = fileDao.fileDAO().insertTag(tagName, groupId);
        pptList = getPPTLists(tagPath);
        for ppt in pptList:
            fileInfos = str(ppt['server_filename']).split('.');
            if len(fileInfos) == 2:
                fileName = fileInfos[0];
                fileFormat = fileInfos[1];
            else:
                fileName = fileInfos[0]
            fileDao.fileDAO().insertFileTemplate(ppt['size'], groupId, tagId, fileFormat, fileName);


