import urllib
import urllib.request
 
# 抓取页面方法，调用该方法返回抓取到数据
def read_pageHtml(url):
    file = urllib.request.urlopen(url)
    data = file.read()
    return data
 
# 传入需要抓取页面的链接 并调用抓取页面方法获得页面数据
url = "https://celestrak.com/NORAD/elements/gp.php?CATNR=51825"
data = read_pageHtml(url)
# 控制台打印数据
# print(data)
name=data[44:49]
# print(data[44:49])
# 将数据生成txt文件方法 传入保存文件路径 storagePath 以及文件数据 data
def storageToLocalFiles(storagePath, data):
    fhandle = open(storagePath,"wb")
    fhandle.write(data)
    fhandle.close()
# 调用文件数据保存方法
filename=name.decode('utf-8')
storagePath = "./backup/"+filename+'.txt'
print(storagePath)
storageToLocalFiles(storagePath, data)


