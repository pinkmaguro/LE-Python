"""
인터넷에서 가져온 숫자 정보를 가지고 있는 스트링으로부터 Decimal 클래스를
생성하고 싶다.
어떻게 스트링을 클리닝할까?
"""

from decimal import Decimal

def clean_decimal(text):
    if text is None: return text
    try:
        return Decimal(text.replace('$','').replace(',', ''))
    except InvalidOperation:
        return text

"""
위의 예에서는 replace 메쏘드를 두 번 호출했다. 
의미가 희석된다.
"""