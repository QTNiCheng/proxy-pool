redis_host = '127.0.0.1' #redis连接地址
redis_port = 6379 #端口
flask_host = '0.0.0.0'
flask_port = 5010
db = 0 #数据库
name = 'proxy' #数据库表名
check_redis = True #是否检查redis中的代理，开启后会先剔除redis中不可用的代理，然后在爬取代理.
updata_proxy = False #是否更新redis库中的代理