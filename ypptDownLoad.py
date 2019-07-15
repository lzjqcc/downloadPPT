# coding=utf-8
import urllib3;
from proxy import Proxy;
from bs4 import BeautifulSoup;
import os;
import threading;
from fileDao import fileDAO;
yppturl = 'http://www.ypppt.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Mobile Safari/537.36',
    "HOST":"www.ypppt.com",
    "Upgrade-Insecure-Requests":1,
    "ACCPT":'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
}
rootPath = "D:\\ppt背景\\";
fileSplit ="\\";

def getRequestContent(url,proxy=False):
    if proxy:
        http = Proxy().getProxyHttp(headers);
    else:
        http = getHttp();
    print(getUrl(url))
    r = http.request('GET', getUrl(url));
    return r.data.decode("utf-8");
def getUrl(url):
    if url.__contains__('http'):
        return url;
    return yppturl + url;

def getRequest(url):
    http = getHttp();
    return http.request("GET", getUrl(url));

def getHttp():
    http = urllib3.PoolManager();
    http.headers = headers;
    return http;

def getPage(url, proxy = False):
    return BeautifulSoup(getRequestContent(url, proxy), 'lxml');
def download(classifyName,classifyHref):
    # if not os.path.exists(rootPath + classifyName):
    #     os.mkdir(rootPath + classifyName);
    downloadAll(classifyHref,classifyHref, classifyName, 0)
def getMaxPageIndex(pageLinkAs):
    pageLinkAsReverse = pageLinkAs[::-1];
    for pageLinkA in pageLinkAsReverse:
        if pageLinkA.string.isdigit():
            return int(pageLinkA.string);


def downloadAll(href,preFixHref, classifyName, currentPage):
    classifyPage = getPage(href);
    pageLinkAs = classifyPage.select('.page-navi')[0].select('a');
    maxPageIndex = getMaxPageIndex(pageLinkAs);
    downloadOnePagePPT(href, classifyName)
    for pageHrefIndex in range(len(pageLinkAs)):
        #当前页的链接
        pageHref = pageLinkAs[pageHrefIndex].attrs['href'];
        #当前页的数字  1,2,3,4,5
        pageIndexString = pageLinkAs[pageHrefIndex].string;
        #判断是否是数字
        if pageIndexString.isdigit():
            pageIndex = int(pageIndexString)
        else:
            continue
        if pageIndex <= currentPage:
            continue

        if pageIndex == maxPageIndex:
            downloadAll(preFixHref + '/' + pageHref, preFixHref, classifyName, pageIndex);
        else:
            downloadOnePagePPT(preFixHref + '/' + pageHref, classifyName);
            print(classifyName + "下载第"+pageIndexString+"页" + preFixHref + '/' + pageHref)

def downloadOnePagePPT(href, classifyName):
    soup = getPage(href);
    posts = soup.select(".posts")[0];
    for a in posts.select("a"):
        if a.string is not None:
            name = a.string;
            if os.path.exists(rootPath + classifyName + fileSplit + name +'.rar'):
                continue
            pptPageHref = a.attrs["href"];
            pptPage = getPage(pptPageHref);
            downButtn = pptPage.select(".down-button")[0];
            downButtnHref = downButtn.attrs["href"];
            downLoadPage = getPage(downButtnHref);
            down = downLoadPage.select(" li a")[0];
            # print(down.attrs['href'])
            # ppt = getRequest(down.attrs['href']);

            print(classifyName + "下载:"+name);
            downHref = down.attrs['href']
            fileDAO().insertPPTFile(group=classifyName,fileName= name, downLoadURL=getUrl(downHref))
            # with open(rootPath + classifyName + fileSplit + name + ".rar", "wb") as f:
            #     f.write(ppt.data)
            # f.close()
            # break;
mobanPage = getPage('/jieri/');
menu = mobanPage.select('.menu ul')[0];
for a in menu.select('a'):
    if a.string != '动态模版':
        classifyName = a.string;
        classifyHref = a.attrs['href'];
        #threading.Thread(target=download, args=(classifyName, classifyHref)).start()
        download(classifyName, classifyHref)




