from datetime import datetime
from operator import itemgetter


class Api_Softtek:
    def orderStat(self, lista):
        res = {}
        data = []
        # creating a new dictionary with the the items from the same order_id together
        for item in lista:
            res.setdefault(item["order_number"], []).append(item)
        # for every order_id is check if the order is pending, shipped or cancelled,
        # in case an item is pending the order is pending, cancelled only if all item are cancelled,
        # shipped if theres no pending and at least one item is shipped
        for x in res:
            aux = "cancelled"
            for y in res[x]:
                if "pending" in y["status"]:
                    data.append({"order_number": x, "status": "pending"})
                    aux = "pending"
                    break
                elif "shipped" in y["status"]:
                    aux = "shipped"
            if aux == "shipped":
                data.append({"order_number": x, "status": "shipped"})
            elif aux == "cancelled":
                data.append({"order_number": x, "status": "cancelled"})
        return data

    def seasons(self, lista):
        seasons = []
        # convert string date to datetime object
        for x in lista:
            x["ORD_DT"] = datetime.strptime(x["ORD_DT"], "%m/%d/%y")
        # check season of the determined date and add it to the new list tha will be returned
        for x in lista:
            date = (x["ORD_DT"].month, x["ORD_DT"].day)
            if (3, 19) <= date < (6, 19):
                seasons.append({"ORD_ID": x["ORD_ID"], "season": "Spring"})
            elif (6, 20) <= date < (9, 21):
                seasons.append({"ORD_ID": x["ORD_ID"], "season": "Summer"})
            elif (9, 22) <= date < (12, 20):
                seasons.append({"ORD_ID": x["ORD_ID"], "season": "Fall"})
            else:
                seasons.append({"ORD_ID": x["ORD_ID"], "season": "Winter"})

        return seasons

    def weather(self, lista):
        weath = []
        aux = True
        # convert string to date and sorting order by date
        for x in lista:
            x["date"] = datetime.strptime(x["date"], "%m/%d/%y")
        data = sorted(lista, key=itemgetter("date"))
        # check if the weather changed, if change from False to true then add to the new list that will be returned
        for x in data:
            if x["was_rainy"] == True and aux == False:
                weath.append(
                    {
                        "date": datetime.strftime(x["date"], "%m/%d/%y"),
                        "was_rainy": True,
                    }
                )
            aux = x["was_rainy"]

        return weath
