# TB_Spider
百度贴吧爬虫,爬取百度贴吧的帖子,图片
## 依赖库 Srapy
安装： 
```
pip install scrapy
```
## 使用
添加关键词
修改TBid.txt文件，添加要抓的帖子的id（url中的那段长数字）
## 运行爬虫
../TB_Spider/PicGet/PicGet$ scrapy crawl Doutu
## 查看运行结果
生成的内容在../TB_Spider/PicGet/PicGet/spider_products文件夹下