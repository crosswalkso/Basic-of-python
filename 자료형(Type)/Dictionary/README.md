# 딕셔너리

## 구조
```py
dict = {key1:value1,
        key2:value2,
        ...
        } # key는 불변값(immutable)
```

### 딕셔너리 생성
```py
dict = {}
dict["name"] = "Python" # dict = {'name': 'Python'}
dict["address"] = "Busan" # dict = {'name': 'Python', 'address': 'Busan'}
```
### get(key, default_value)
- key를 이용해 값을 불러온다.
- 없는 key면 `None`을 반환
- 없는 key의 경우 반환할 값을 설정해줄 수 있지만 딕셔너리에 key:value 쌍이 추가되지는 않는다.
```py
dict.get("phone_number") # None
dict.get("phone_number", 12345) # 12345
```

## Python Dictionary Methods - 메소드
- 몇몇은 메모리 낭비를 줄이기 위해 객체를 반환하며 객체는 iterate 구문들을 실행할 수 있다.
- 메소드는 데이터(Type)와 결합되며 그렇지 않으면 함수(function)이다.

### keys(), values(), items()

```py
info = {
    "name": "python",
    "address": "Seoul",
    "favorite_color": "orangeblue",
    "favorite_food": "kimchi",
}
print(info.keys())  # dict_keys 객체
print(info.values())  # dict_values 객체
print(info.items())  # dict_items 객체 - key, value 쌍
```
#### items()
- 튜플로 뽑기
```py
for tup in info.items():
    print(tup, tup[0], tup[1])
```
결과
```
('name', 'python') name python
('address', 'Seoul') address Seoul
('favorite_color', 'orangeblue') favorite_color orangeblue
('favorite_food', 'kimchi') favorite_food kimchi
```
- 튜플 언패킹
```py
for i, j in info.items():
    print("key:", i, "| value:", j)
```
결과
```
key: name | value: python
key: address | value: Seoul
key: favorite_color | value: orangeblue
key: favorite_food | value: kimchi
```
### list
list로 만들고 싶다면 list()를 하면 된다.

### key 확인
```
>>> "name" in info
True
``` 
### pop()
- 값을 반환하며 key:value 쌍을 지운다.
```
>>> info
{'name': 'python', 'address': 'Seoul', 'favorite_color': 'orangeblue', 'favorite_food': 'kimchi'}
>>> info.pop('name')
'python'
>>> info
{'address': 'Seoul', 'favorite_color': 'orangeblue', 'favorite_food': 'kimchi'}
```

### clear()
```
>>> info.clear()
>>> info
{}
```

## 응용
### value - 리스트, 딕셔너리
```py
info = {
    "name": "python",
    "address": "Seoul",
    "favorite_color": [
        "orange",
        "blue",
    ],
    "favorite_food": "kimchi",
    "friends": {
        "django": "framework",
        "numpy": "library",
    },
}

info["favorite_color"].append("red") # 'favorite_color': ['orange', 'blue', 'red']
info["friends"].get("numpy") # library
# get 말고도 dict_name[key]로 값을 불러올 수 있다.
```