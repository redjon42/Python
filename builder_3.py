
medal_count = {}
country_list = ["US", "UK", "China", "Russia", "Germany"]
medal_list = [70, 38, 45, 30, 17]
test = len(country_list) == len(medal_list)
print(test)
for i in range(len(country_list)):
    medal_count[country_list[i]] = medal_list[i]
medal_count['Brazil'] = '10'

keys = list(medal_count.keys())
print(keys)

