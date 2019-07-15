import urllib3
from selenium import webdriver
from time import sleep;

from selenium.webdriver.support import wait

yppturl = 'http://www.ypppt.com'

# browser = webdriver.Chrome()
# browser.get(yppturl+'/moban');
# sleep(15)
# print(browser.find_element_by_link_text("自我介绍").click());
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Mobile Safari/537.36',
    "HOST":"www.ypppt.com",
    "Upgrade-Insecure-Requests":1,
    "ACCPT":'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',


}


def getRequestContent(url):
    http = urllib3.PoolManager();
    http.headers = headers;
    if url.__contains__(yppturl):
        return http.request('GET', yppturl + url, headers).data.decode("utf-8");
    r = http.request('GET', yppturl+ url, headers);
    print(http.headers)
    return r.data.decode("utf-8");
print(getRequestContent('/moban/jieshao'))



