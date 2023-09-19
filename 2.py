
def subsets(numbers):
    if numbers == []:
        return [[]]

    i = subsets(numbers[1:])
    return i + [[numbers[0]] + j for j in i]


def all_itemsets(unique_items, n):
	sets = subsets(unique_items) 
	return [eachSubset for eachSubset in sets if len(eachSubset)==n]

print(all_itemsets(["ham", "cheese", "bread"], 2))

