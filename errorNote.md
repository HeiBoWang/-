year = province.css(".sline > div:nth-child(2)::text").extract()[0]
###  .sline clearfix 这样是错误的写法， 空格娶不到。
### extract()[0] 可以将 ['2018年'] 变为 2018年
### nth-child(2) 变量从 1 开始