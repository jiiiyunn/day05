import matplotlib.pyplot as plt #plt로 부르겠다는거

data = [('A', 10),('B', 20),('C', 30)]
color = ['#FFF000', 'blue', 'g']
xticks = ['AC','BC','CC']

plt.rc('font', family='Malgun Gothic')
plt.title("한글Grape Test")
plt.bar([k for k, v in data], [v for k, v in data], label =[k for k, v in data], color = color)
plt.xlabel("company")
plt.ylabel("count")
plt.ylim(0, 50)
plt.legend()#범례
#plt.xticks(xticks)
plt.show()
plt.close()

