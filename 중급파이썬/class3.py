class Car():
    '''
    주제 : Class / Static / Instanch Method
    '''
    
    #클래스변수 ( 모든 인스턴스가 공유 )
    price_per_raise = 1.0
    
    def __init__(self, company, detail):
        self._company = company
        self._detail = detail
        print('생성 완료')
    
    def __str__(self):
        return '객체: {}  {}'.format(self._company, self._detail) 
    
    def __repr__(self):
        return '객체: {}  {}'.format(self._company, self._detail) 
    
    # 인스턴스 메소드 (self 함유)
    # Self: 객체의 고유한 속성 값 사용 (내꺼 !)
    def detail_info(self):
        print('Current ID: {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._detail.get('price')))
    
    
car1 = Car('hyundai', {'color':'white', 'horsepower':400,'price':7500})
car2 = Car('auid', {'color':'black', 'horsepower':600,'price':6000})