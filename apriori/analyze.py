from efficient_apriori import apriori
import csv


direct = '张艺谋'
file_name = 'douban.csv'
lists = csv.reader(open(file_name, 'r', encoding='utf-8-sig'))
data = []
for names in lists:
    data.append(names[1:])

#挖掘频繁项集和关联规则
itemsets,rules = apriori(data,min_support=0.1,min_confidence=1)

print(itemsets)
print(rules)
