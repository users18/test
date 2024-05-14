fi = open("xueyajilu.txt",'r')
jl = [[],[],[],[],[]]   #存储数据
zyc = []   #左臂压差
yyc = []   #右臂压差
xl  = []   #心率
for item in fi:
    lls=item.replace('\n','').strip().split(',')
    for i in range(1,5):
        jl[i].append(eval(lls[i] ))
    zyc.append(eval(lls[1])-eval(lls[2]  ))  #左臂压差
    yyc.append(eval(lls[3])-eval(lls[4]))  #右臂压差
    xl.append(eval(lls[5]))                #心率
fi.close()
cnt = len(xl)
res = []
res.append(list(("高压最大值",max(jl[1]),max(jl[3]))))
res.append(list(("低压最大值",max(jl[2]),max(jl[4]))))
res.append(list(("压差平均值",sum(zyc)/cnt,sum(yyc)/cnt)))
res.append(list(("高压平均值",sum(jl[1])/cnt,sum(jl[3])/cnt)))
res.append(list(("低压平均值",sum(jl[2])/cnt,sum(jl[4])/cnt)))
res.append(list(("心率平均值",sum(xl)/cnt ,0)))
zbg = 0
ybg = 0
print('{:<10}{:<10}{:<10}'.format("对比项", "左臂", "右臂"))
for r in range(len(res)-1):
    print('{:<10}{:<10}{:<10}'.format(res[r][0],res[r][1],res[r][2]))
    if res[r][1]>res[r][2]:
        zbg += 1
    else:
       ybg += 1
if zbg > ybg:
    print('结论：左臂血压偏高',end ='')
elif zbg == ybg:
    print('结论：左臂血压与右臂血压相当',end ='')
else:
    print('结论：右臂血压偏高',end ='')
print(', 心率平均值为{}'.format(res[5][1]))
