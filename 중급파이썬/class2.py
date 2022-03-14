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
    
    def __repr__(self):
        return '객체: {}  {}'.format(self._company, self._detail) 
    
    def detail_info(self):
        print('Current ID: {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._detail.get('price')))
    
car1 = Car('hyundai', {'color':'white', 'horsepower':400,'price':7500})
car2 = Car('auid', {'color':'black', 'horsepower':600,'price':6000})
car3 = Car('bmw', {'color':'silver', 'horsepower':500,'price':9000})


print(id(car1))
print(id(car2))
print(id(car3))

print(dir(car1))

car1.detail_info()

print(id(car1.__class__))
print(id(car2.__class__))