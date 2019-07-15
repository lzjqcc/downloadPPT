# coding=utf-8
import urllib3;
from bs4 import BeautifulSoup;


def getRequestContent(url):
    http = urllib3.PoolManager();
    if url.__contains__('http://www.1ppt.com/'):
        return http.request('GET', url).data.decode("utf-8");
    r = http.request('GET', "http://www.1ppt.com/" + url);
    return r.data;


def getRequest(url):
    http = urllib3.PoolManager();
    return http.request("GET", url);


def getPage(url):
    return BeautifulSoup(getRequestContent(url), 'lxml');


soup = getPage('/moban/jianjie/');
posts = soup.select(".tplist")[0];

for a in posts.select("h2 a"):
    if a.string is not None:
        name = a.string;
        pptPageHref = a.attrs["href"];
        pptPage = getPage(pptPageHref);
        downLoad = pptPage.select(".downurllist")[0].select("a")[0].attrs['href'];
        ppt = getRequest(downLoad);
        with open("/home/li/download/"+name+".zip", "wb") as f:
            f.write(ppt.data)
        f.close()