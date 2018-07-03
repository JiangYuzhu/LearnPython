
#根据利润计算奖金
#奖金根据利润提成。
#1.利润低于或等于10万元时，奖金可提10%；
#2.利润高于10万低于20万时，低于10万部分按10%提成，高于10万部分按7.5%提成；
#3.利润20-40万之间时，高于20万部分按5%提成；
#4.利润40-60万之间时，高于40万部分按3%提成；
#5.利润60-100万之间时，高于60万部分按1.5%提成；
#6.利润高于100万时，高于100万部分按1%提成；
#根据输入的利润值，计算出提成的奖金数额。


profits = [1000000,600000,400000,200000,100000,0] #profits
rate = [0.01,0.015,0.03,0.05,0.075,0.10]
profit = int(input('请输入销售利润：'))
extract = 0  #extract
for idx in range(0,6):
    if profit > profits[idx]:
        extract += (profit-profits[idx]) * rate[idx]
        print("相应利润段提成："+str((profit-profits[idx]) * rate[idx]))
        profit = profits[idx]
print("销售总提成："+str(extract))
