# DDNS

> 虽然使用花生壳好几年了，但花生壳总是时不时抽疯，比如今天将我的域名解析为127.0.0.2
> 想想大抵是因为没有氪金吧，不过在找问题原因时候看见了一条思路，借助DNSPod刷新DNS解析信息。后进一步了解DNSPod已经归属腾讯云了。
> 思路大致如下：
> 1. 获取本地公网IP 暂时借助 `https://api.ipify.org?format=json` .想到自己几年前薅阿里云羊毛，写过相关服务，但是服务器续费太贵，试了下这个可以用但是速度比较慢，暂时先凑合吧。淘宝的API已经不能使用了。
> 2. 将获取到的信息通过DNSPod接口 `https://dnsapi.cn/Record.Ddns`  更新
> 3. 以上步骤开个定时器运行即可。



找了几个可用的获取本地IPV4公网地址的接口

- http://ip.42.pl/raw
- https://ifconfig.me/ip

- http://jsonip.com
- https://api.ipify.org?format=json
