#!/usr/bin
#python/163.song utf-8
import re
import urllib.request
import urllib.error
import urllib.parse
import json

def get_all_hotSong():#获取所有歌曲名称与Id
    url = "https://music.163.com/discover/toplist?id=3778678"
    header = {#请求头部
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
    }
    request = urllib.request.Request(url=url,headers=header)
    html = urllib.request.urlopen(request).read().decode('utf-8')#打开url
    html = str(html)
    #测试
    reg1 = r'<ul class="f-hide"><li><a href="/song\?id=\d*?">.*</a></li></ul>' #构造获取歌曲相关标签正则第一次
    result = re.compile(reg1).findall(html)
    result = result[0] #获取tutle的第一个元素
    reg2 = r'<li><a href="/song\?id=\d*?">(.*?)</a></li>'#构造获取歌名的正则
    reg3 = r'<li><a href="/song\?id=(\d*?)">.*?</a></li>' #构造获取歌曲id的正则
    hot_song_name = re.compile(reg2).findall(result) #获取所有歌名
    hot_song_id = re.compile(reg3).findall(result)   #获取所有id
    #print(hot_song_name,hot_song_id)
    return hot_song_name,hot_song_id
#get_all_hotSong()
#获取评论内容
def get_hot_Comments(hot_song_name,hot_song_id):
    url = "https://music.163.com/weapi/v1/resource/comments/R_SO_4_"+hot_song_id+"?csrf_token="
    header = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
    }
    # 请求表单数据
    data = {'params':'MqTyknxcVqtPA4ZpAXyqXiGoa4GzZOfl0rWMwXtlZSl/0v45GO0bh1327ZYlyphjA+xt/oJ8ivTYCzJhXPNxS4pJZok1gwWlk6J4U8UQ3FlQQWOYHvhMDB+VN+S7sWrBDkPqzMj5weOUeMyRviqb14ptuGQ1Gsysl9tH0cI/radbMBtMEopJnq+Dt2whmK+Kh68RCxq7j4zx5SVMZAmCgp1xekx3r8/NkdcnIm+ZEho=','encSecKey':'716d8d0621ed113dcaabbf6b9f211da958441e8d88b1171532dd9ff9e2d3830b4a82cfdb1062c794c9ac610df526a4ef074ccd16a63227ddb2754c5dc6eab7f8af96c2a38540d1839410fee994b3b6a2fe917aced05feb168f4611606e0b759eec8d93ee0ddec3ba8f11fddfa8ed31cb443cda06cddff1411434e101b6a6ea2d'}
    postdata = urllib.parse.urlencode(data).encode('utf-8')#参数编码
    request = urllib.request.Request(url,headers=header,data=postdata)#拼接请求信息
    response = urllib.request.urlopen(request).read().decode('utf-8')#开始请求返回内容
    json_dict = json.loads(response)#获取json
    hot_commit = json_dict['hotComments']#获取属性值
    #print(hot_commit)
    num = 0
    fhandle = open('./song_comments','a',encoding='utf-8')#写入文件
    fhandle.write(hot_song_name+":"+"\n")

    for item in hot_commit:
        num += 1
        fhandle.write(str(num)+'.'+item["content"]+'\n')
    fhandle.write("\n-----------------------------\n\n")
    fhandle.close()
# 获取歌曲名 id信息
hot_song_name,hot_song_id = get_all_hotSong()
num = 0
while num < len(hot_song_name):
    print('正在抓取第%d首歌热评..'%(num+1))
    get_hot_Comments(hot_song_name[num],hot_song_id[num])
    print('第%d首歌曲评论抓取成功!!'%(num+1))
    num += 1









