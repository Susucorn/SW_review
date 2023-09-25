'''
    신라대학교 202395016 컴퓨터공학부 박수연
'''

import matplotlib.pyplot as plt    # as 뒤에 이름은 별명, 내가 쓰고자 할 이름을 간략하게 적음

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [67.0, 87.0, 257.0, 1686.0, 6505, 11865.3, 22103.3]       # 국민소득

plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

plt.title("GDP")

plt.ylabel("dollars")                           # y변의 이름
plt.xlabel("year")                              # x변의 이름
plt.savefig("gdp_per_capita.png", dpi=600)
plt.show