#Question 4
import copy


weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

copied_dict = copy.deepcopy(weekly_sales)
print(copied_dict)

copied_dict["Week 2"]["Electronics"] = 18000

print(copied_dict)