#oop 객체지향 -> 코드의 재사용, 중복 방지, 유지보수, 대형프로젝트
# 규모 큰 프로젝트 -> 함수 중심  -> 데이터 방대 -> 복잡
#                    클래스 중심 -> 데이터 중심 -> 객체로 관리



class Car():
    def __init__(self, company, detail):
        self._company = company
        self._detail = detail
        print('생성 완료')
    
    def __str__(self):
        return '객체: {}  {}'.format(self._company, self._detail) 
car1 = Car('hyundai', {'color':'white', 'horsepower':400,'price':7500})
car2 = Car('auid', {'color':'black', 'horsepower':600,'price':6000})


list = []
list.append(car1)
list.append(car2)

print(list)