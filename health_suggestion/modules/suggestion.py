#!/usr/bin/env python
# coding: utf-8

# 熱量運動消耗
import random

def sport_calculate(weight, tdee, meal_calories):
    with open("./data./運動消耗熱量對照表.csv", encoding="utf-8") as f:
        data = [i.split(",") for i in f.readlines()][1:]
        per_meal_tdee = tdee/3 
    if meal_calories > per_meal_tdee:
        calculate = int(round(meal_calories - per_meal_tdee, 0))
        suggest = {}  # a dictionary of random suggest
        for i in range(5):
            sports = random.choice(data)
            u_calculate = float(sports[1])
            sport = sports[0]
            minutes = int(round(calculate / (u_calculate * weight) * 60, 0))
            suggest[sport] = minutes
            if len(suggest) == 2:
                break
        result = ""
        for key, value in suggest.items():
            result += f"做'{key}'活動 {value}分鐘 或是 "
        result = result[:-4]  # delete"或是"
        return f"本餐攝取熱量超過{calculate}大卡，建議您 {result}"


# 蛋白質：●一般成人=體重（kg）×1.1（ｇ）的蛋白質●70歲以上老年人=體重（kg）×1.2（ｇ）的蛋白質●運動健身族＝體重（kg）×1.5~1.7（ｇ）的蛋白質
def protein_suggest(protein, weight, age, purpose):
    # protein_std:不同對象有不同係數
    if purpose != 1:
        protein_std = weight * 1.5 / 3  # 除以3餐
    elif age > 70:
        protein_std = weight * 1.2 / 3
    else:
        protein_std = weight * 1.1 / 3
    # 蛋白質是否攝取不足
    if protein < protein_std:
        protein_lack = int(protein_std - protein)
        egg_num = round(protein_lack / 7, 1)  # 一顆雞蛋7g
        return f"'蛋白質'含量不足{protein_lack}克，約等於{egg_num}顆雞蛋，建議您增加今日的蛋白質攝取量"

    
# 脂肪:一般人每日飲食中脂肪攝取量應該占總熱量的20%到30%
def fat_suggest(fat, sat_fat, trans_fat, per_meal_tdee):
    # Fat_std:20~30%，1g脂肪熱量9大卡
    result = ""
    if fat * 9 < per_meal_tdee * (20 / 100):
        fat_lack = int((per_meal_tdee * 20 / 100 / 9) - fat)  # g
        oil_num = round(fat_lack * 9 / 8.84, 1)
        result = result + f"'脂肪'含量不足{fat_lack}克，約等於{oil_num}毫升橄欖油，建議您增加今日的脂肪攝取量"
    if fat * 9 > per_meal_tdee * (30 / 100):
        fat_over = int((fat * 9 / per_meal_tdee * 100) - 30)  # %
        oil_num = round((fat * 9 - per_meal_tdee * (30 / 100)) / 8.84, 1)
        result = result + f"'脂肪'含量超過{fat_over}%，約等於{oil_num}毫升橄欖油，建議您減少今日的脂肪攝取量"
    # sat_fat:每日飽和脂肪的攝取量應低於總熱量的10%
    if sat_fat * 9 > per_meal_tdee * (10 / 100):
        sat_fat_over = int(round((sat_fat * 9 / per_meal_tdee * 100) - 10, 0))  # %
        result = result + "；" + "\n" + f"'飽和脂肪'含量超過{sat_fat_over}%，建議您減少今日的飽和脂肪攝取量"
    # trans_fat:反式脂肪的攝取量不得超過總熱量的1%
    if trans_fat * 9 > per_meal_tdee * (1 / 100):
        trans_fat_over = round((trans_fat * 9 / per_meal_tdee * 100) - 1, 2)  # %
        result = result + "；" + "\n" + f"'反式脂肪'含量超過{trans_fat_over}%，建議您不要攝取反式脂肪"
    return result


# 碳水化合物:，一至七十歲以上碳水化合物每日建議攝取量為130公克，占總熱量的50~60%
def carbohydrate_suggest(carbohydrate, per_meal_tdee):
    # carbohydrate_std:50~60%，1g碳水化合物熱量4大卡
    carbohydrate_std = 130 / 3
    if carbohydrate < carbohydrate_std:
        carbohydrate_lack = int(round(130 / 3 - carbohydrate, 0))
        rice_num = round(carbohydrate_lack / 60, 1)
        return f"'碳水化合物'含量不足{carbohydrate_lack}克，約等於{rice_num}碗白飯，建議您增加今日的碳水化合物攝取量"
    if carbohydrate * 4 > per_meal_tdee * (60 / 100):
        carbohydrate_over = int((carbohydrate * 4 / per_meal_tdee * 100) - 60)  # %
        rice_num = round((carbohydrate * 4 - per_meal_tdee * (60 / 100)) / 60, 1)
        return f"'碳水化合物'含量超過{carbohydrate_over}%，約等於{rice_num}碗白飯，建議您減少今日的碳水化合物攝取量"
    else:
        return f"'本餐碳水化合物'攝取量符合標準"

# 糖：每日飲食中，添加糖攝取量不宜超過總熱量的10%，最好低於5%
def suger_suggest(suger, per_meal_tdee):
    # suger_std:<10%，1g糖熱量4大卡
    suger_std = per_meal_tdee * 1 / 10
    if suger * 4 > suger_std:
        suger_over = ((suger * 4) - suger_std) / 4
        return f"'糖'含量超過{suger_over}克，建議您多喝水及減少本日攝取的糖含量"


# 鈉：成人每日鈉總攝取量不宜超過2400毫克（即鹽6公克）
def sodium_suggest(sodium):
    # sodium_std:<2400
    sodium_std = 2400 / 3
    if sodium > sodium_std:
        sodium_over = int(round(sodium - sodium_std, 0))
        return f"'鈉'含量超過{sodium_over}毫克，建議您多喝水及減少本日攝取的鈉含量"


# def vegetable_suggest():
    
def nutrition_suggest(test):
    result = "本餐攝取的"
    result += "\n" + protein_suggest(test['protein'], test['weight'], test['age'], test['purpose'])
    result += "；" + "\n" + fat_suggest(test['fat'], test['sat_fat'], test['trans_fat'], test['per_meal_tdee'])
    result += "；" + "\n" + carbohydrate_suggest(test['carbohydrate'], test['per_meal_tdee'])
    result += "；" + "\n" + suger_suggest(test['suger'], test['per_meal_tdee'])
    result += "；" + "\n" + sodium_suggest(test['sodium'])
    return result


# test
if __name__ == "__main__":
    test = {
        "age": 30,
        "weight": 60,
        "purpose": 2,
        "per_meal_tdee": 500,
        "protein": 20,
        "fat": 20,
        "sat_fat": 10,
        "trans_fat": 1,
        "carbohydrate": 80,
        "suger": 30,
        "sodium": 900,
    }

    print(nutrition_suggest(test))
    
    # print(sport_calculate(60, 500, 600))