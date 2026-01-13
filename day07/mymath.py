import math
def tri_area(height:int,base:int)->int:
    '''
    삼각형은 넓이 구하는 함수
    '''
    return 0.5*height*base
def cir_area(radius:int)->int:
    '''
    원의 넓이를 구하는 함수
    '''
    return math.pi * radius ** 2
def cubo_area(height:int,width:int,length:int)->int:
    '''
    직육면체의 겉넓이를 구하는 함수
    '''
    return (width *length + length * height + width * height) * 2

