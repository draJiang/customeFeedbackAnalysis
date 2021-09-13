def cixing(addr, column):
    '''
    词性分析，返回分词及对应的词性数据
    addr：数据源表格地址
    column：数据在表格中的第几列
    '''
    # 打开表格
    wb = load_workbook(addr)  # 数据源
    ws = wb.worksheets[0]
    wbcixing = openpyxl.Workbook() # 新建表格，存储词性数据
    wscixing = wbcixing.worksheets[0]

    dataTemp = []

    for index in range(ws.max_row):

        index += 1
        if(index == 1):
            continue
        else:
            # for j in range(ws.cell(row = index, column = column+1).value):
            v = ws.cell(row=index, column=column).value

            if(v == None):
                continue
            # 过滤
            if(len(keyWord) == 0):
                dataTemp.append(v)
            else:
                for item in keyWord:
                    if(item in v):
                        dataTemp.append(v)

    for index in range(len(dataTemp)):
        print(index/len(dataTemp))
        try:
            s = SnowNLP(dataTemp[index])  # 创建分词对象
            # print(dataTemp[index])
            print(s.words)
            print(s.tags)

            for token_tag in s.tags:
                token_tagTemp = []
                print(token_tag)
                token_tagTemp.append(token_tag[0])
                token_tagTemp.append(token_tag[1])

                wscixing.append(token_tagTemp)

            
        except:
            continue

    wbcixing.save('/Users/cc/Documents/inbox/'+str(int(time.time()))+'.xlsx')


# keyWord = ['电脑', 'PC', 'pc']
keyWord = []

# 有效词性 a n v
cixing('/Users/cc/Documents/用户反馈/用户反馈2021-08-14-2021-09-12.xlsx', 15)
