import urllib3;


class Proxy:


    ips = [
        '159.192.253.61:8080',
        '110.36.239.237:8080',
        '188.131.131.2:808',
        '93.188.208.145:34280',
        '222.94.151.208:61234',
        '210.16.102.216:8080',
        '124.41.211.231:41900',
        '177.73.45.193:3128',
        '42.115.53.99:80',
        '103.85.63.70:53281',
        '35.221.6.72:3128',
        '210.56.238.246:8080',
        '31.133.57.134:41258',
        '36.91.32.27:8080',
        '199.68.177.124:80',
        '186.96.113.109:8080',
        '119.82.253.155:31793',
        '122.116.1.83:58086',
        '103.86.43.27:8080',
        '14.207.32.127:8080',
        '27.50.18.81:3128',
        '182.253.115.90:8080',
        '190.184.144.50:36909',
        '134.19.218.94:3129',
        '51.235.219.235:8080',
        '157.119.118.81:40951',
        '124.30.160.11:80',
        '93.99.104.104:8080',
        '154.197.128.226:3128',
        '212.175.98.171:8080']

    def getProxyIP(self):
        for ip in self.ips:
            proxy = urllib3.ProxyManager("http://" + ip)
            urllib3.disable_warnings();
            try:
                response = proxy.request("GET", "https://www.baidu.com");
                if response.status == 200:
                    return ip;
            except Exception as e:
                print('请求错误，重新获取ip' + e)
        return None;


    def getProxyHttp(self, heads = None):
        ip = self.getProxyIP();
        if ip is None:
            proxy = urllib3.PoolManager;
        else:
            proxy = urllib3.ProxyManager("http://" + ip)
        proxy.headers = heads;
        return proxy;