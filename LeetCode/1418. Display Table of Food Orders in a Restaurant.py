class Solution(object):
    def displayTable(self, orders):
        """
        :type orders: List[List[str]]
        :rtype: List[List[str]]
        """
        dish = set()
        for i in orders:
            dish.add(i[2])
        dish_list = sorted(dish)
        tables_order = {}

        for i in orders:
            if int(i[1]) in tables_order:
                tmp = tables_order[int(i[1])]
                tmp[dish_list.index(i[2])] += 1
                tables_order[int(i[1])] = tmp
            else:
                tmp = [0] * (len(dish_list))
                tmp[dish_list.index(i[2])] += 1
                tables_order[int(i[1])] = tmp

        # print(dish)
        # print(tables_order)
        ans = []
        dish_list.insert(0,"Table")
        ans.append(dish_list)
        tmp = []
        for k in sorted(list(tables_order.keys())):
            tmp.append(str(k))
            for i in tables_order[k]:
                tmp.append(str(i))
            ans.append(list.copy(tmp))
            tmp.clear()
        print(ans)
        return ans



s = Solution()
s.displayTable(orders=[["David", "3", "Ceviche"], ["Corina", "10", "Beef Burrito"], ["David", "3", "Fried Chicken"],
                       ["Carla", "5", "Water"], ["Carla", "5", "Ceviche"], ["Rous", "3", "Ceviche"]])
