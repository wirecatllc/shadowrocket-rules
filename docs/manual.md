# Manual

## Types

- General
- Rule
- Hosts
- URL
- URL Rewrite
- Script
- MITM
- Proxy Group

每一个选项开始部分由`[${name}]` 组成

## Details

### General

#### Example

```
[General]
# 本地配置文件名字
include = someconf.conf
# 旁路系统
bypass-system = true
skip-proxy = 192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12, localhost, *.local, captive.apple.com
tun-excluded-routes = 10.0.0.0/8, 100.64.0.0/10, 127.0.0.0/8, 169.254.0.0/16, 172.16.0.0/12, 192.0.0.0/24, 192.0.2.0/24, 192.88.99.0/24, 192.168.0.0/16, 198.51.100.0/24, 203.0.113.0/24, 224.0.0.0/4, 255.255.255.255/32, 239.255.255.250/32
dns-server = system
ipv6 = true
prefer-ipv6 = false
always-reject-url-rewrite = false
# 如果回复结果是内网IP，则强制使用代理
private-ip-answer = true
# 劫持APP硬编码路由
hijack-dns = 8.8.8.8
# UI中未出现的值
dns-direct-fallback-proxy = true
dns-fallback-system = false
dns-direct-system = false
icmp-auto-reply = true
```

### Rule

#### Example

```
[Rule]
DOMAIN-SUFFIX,baidu.com,DIRECT
DOMAIN-SUFFIX,baidubcr.com,DIRECT
DOMAIN-SUFFIX,bdstatic.com,DIRECT
DOMAIN-SUFFIX,yunjiasu-cdn.net,DIRECT
RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Advertising/Advertising.list,REJECT
DOMAIN-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/
GEOIP,CN,DIRECT
FINAL,PROXY
```

#### 支持类型

- DOMAIN-SUFFIX
- DOMAIN-KEYWORD
- DOMAIN
- USER-AGENT
- URL-REGEX
- IP-CIDR
    - 支持 no-resolve
- RULE-SET
- DOMAIN-SET
- SCRIPT
- DST-PORT
- GEOIP
- FINAL
    - 应该是娄底，未匹配到的规则到这里，所以应该只能有一个

#### 支持策略

- PROXY
- DIRECT
- REJECT
    - 404，没有内容
- REJECT-DICT
    - 200，内容为空的JSON对象
- REJECT-ARRAY
    - 200，内容为空的JSON数组
- REJECT-200
    - 200，没有内容
- REJECT-IMG
    - 200， 像素为1的GIF
- REJECT-TINYGIF
    - 200， 像素为1的GIF
- REJECT-DROP
    - 丢弃IP包
- 或者是本地组/服务器名字

### Hosts

#### Example

```
[Host]
localhost = 127.0.0.1
*testflight.apple.com = server:8.8.4.4
```

#### 支持规则

- 直接对应：直接返回IP
- server: 使用对应的DNS解析

### URL Rewrite

似乎需要MITM

#### Example

```
[URL Rewrite]
^https?://(www.)?g.cn https://www.google.com 302
^https?://(www.)?google.cn https://www.google.com 302
^https?:\/\/api\.abema\.io\/v\d\/ip\/check - reject
(^https?:\/\/app\.biliintl\.com\/intl\/.+)(&s_locale=zh-Hans_[A-Z]{2})(.+) $1&s_locale=en-US_US$3 302
(^https?:\/\/app\.biliintl\.com\/intl\/.+)(&sim_code=\d+)(.+) $1$3 302
```

#### 支持规则

除了Rule支持的所有规则外，还可以

- HEADER
- 302
- 307
- Proxy Group
    - 见下文

### Script

https://manual.nssurge.com/scripting/common.html  

说实话，这些规则和Surge的都很像的样子，看UI和这个基本上都对的上

### MITM

#### Example

```
[MITM]
enable = true
ca-passphrase = 24961EL2
ca-p12 = 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
hostname = www.google.cn,api.abema.io,app.biliintl.com
```

### Proxy Group

#### Example

```
[Proxy Group]
vgroup = load-balance,{0个或多个策略},url=http://example.com,interval=600,timeout=5,select=0,policy-regex-filter={some regex}
```

#### 类别

- select
- url-test
- fallback
- load-balance
- random

#### 策略

所有RULE支持的，可以有多个

#### 其他参数

- regex
    - 可选，和策略不能同时存在
- Interval 间隔
    - 多久只有需要重新发起测试
- timeout 超时
    - 如果超时前未完成
- tolerance 
    - url test专属，如果差距大于这个毫秒数才进行替换