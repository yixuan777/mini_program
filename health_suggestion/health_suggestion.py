from modules import suggestion as sug

# Personal information(name,gender、age、height、weight、activity_level、purpose)
name = input("What's your name?")
gender = int(input("What's your gender?: (1) male (2) female"))
age = int(input("What's your age?:"))
height = int(input("What's your height?(cm):"))
weight = int(input("What's your weight?(kg):"))
activity_level = int(input("What's your activity_level?: (1) 靜態 (2) 較低 (3) 正常 (4) 較高 (5) 激烈"))
purpose = int(input("What's your purpose?: (1) 維持現狀 (2) 健身 (3) 減重"))           

# Calculate BMR & TDEE
def calculate_tdee(gender,age,height,weight,activity_level):
    # BMR
    if gender == 1:
        bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
    elif gender == 2:
        bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
    # TDEE
    if activity_level == 1:
        tdee = round(1.2 * bmr,0)
    elif activity_level == 2:
        tdee = round(1.375 * bmr,0)
    elif activity_level == 3:
        tdee = round(1.55 * bmr,0)
    elif activity_level == 4:
        tdee = round(1.72 * bmr,0)
    else:
        tdee = round(1.9 * bmr,0)
    return tdee

tdee = calculate_tdee(gender,age,height,weight,activity_level)

print(f'{name}，你的總基礎代謝率/(大卡/): {tdee}')


data_dic = {
        "age": age,
        "weight": weight,
        "purpose": 2,
        "per_meal_tdee": tdee/3,
        "protein": 20,
        "fat": 20,
        "sat_fat": 10,
        "trans_fat": 1,
        "carbohydrate": 80,
        "suger": 30,
        "sodium": 900,
}
suggestion = sug.nutrition_suggest(data_dic)
print(suggestion)

# 處理Data:食品營養成分資料庫
# 爬蟲：麥當勞、肯德基、摩斯

# 數據視覺化 

# Data：各類運動消耗表
