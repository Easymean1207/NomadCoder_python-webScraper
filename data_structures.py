# list

days_of_week = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

""" list 내에서 특정 문자열이 있는 경우 index, value 출력 """
for index, value in enumerate(days_of_week):
    if "Sun" in value:
        print(f"index:{index}, value:{value}")

# 특정 substring이 몇 개나 있는 지 확인 / count와는 다른 개념
count_days = 0
for day in days_of_week:
    if "day" in day:
        count_days += 1
print(f"{count_days}days in one week!")

# 특정 substring 혹은 character로 끝나는 지 확인
for index, value in enumerate(days_of_week):
    if days_of_week[index].endswith("day"):
        print(f"index:{index}, value:{value}")

""" list reverse """
days_of_week.reverse()
print(days_of_week)

""" list remove """
days_of_week.remove("Monday")
print(days_of_week)

""" list append """
days_of_week.append("월요일 좋아~")
print(days_of_week)

""" list replace """
for index, value in enumerate(days_of_week):
    if "Fri" in value:
        days_of_week[index] = "불타는 금요일!"
print(days_of_week)

""" list 안의 value의 특정 문자를 변경 """
for item in range(len(days_of_week)):
    days_of_week[item] = days_of_week[item].replace(
        days_of_week[item][2], days_of_week[item][2].upper()
    )
print(f"first translate: {days_of_week}")

for item in range(len(days_of_week)):
    days_of_week[item] = days_of_week[item].replace("day", "day".upper())
print(f"second translate: {days_of_week}")


# tuple -> immutable (can't change the value!!!)

days_of_week_tuple = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)

""" reversed()는 객체의 값으로 반환하며 list, tuple, string, dictionary 등에도 활용 가능하다. """
days_of_week_2 = tuple(reversed(days_of_week_tuple))
print(f"origin tuple:{days_of_week_tuple}")
print(f"reversed tuple: {days_of_week_2}")

# dictionary -> key, value pair!!!


def find_key_by_value(dictionary, finding_value):
    for key, value in dictionary.items():
        # value가 list나 tuple과 같이 복합 데이터 유형인 경우
        if isinstance(value, (list, tuple)):
            if finding_value in value:
                return key
        # value가 단일값 유형인 경우
        elif value == finding_value:
            return key
    return None


player = {
    "name": "Elon Musk",
    "age": 50,
    "country": "USA",
    "gender": "M",
    "alive": True,
    "fav_food": ["chicken", "pizza"],
    "family": ("mother", "father", "wife", "children"),
}

""" print value with key (using get()) """
print(f"player name: {player.get('name')}")
print(f"player favorite foods: {player.get('fav_food')}")
print(f"player family: {player.get('family')}")

""" print key with value (using user_define_fucntion) """
print(f"before replace: {find_key_by_value(player, 'chicken')}")
player["fav_food"][0] = "noodle"  # value replace
print(f"after replace: {find_key_by_value(player, 'chicken')}")
print(find_key_by_value(player, 50))
print(find_key_by_value(player, "father"))

""" dictionary add """
player["xp"] = 2000
player["fav_food"].append("burger")
print(player)
