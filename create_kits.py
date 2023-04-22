import configuration
import requests
import data
import tests_kits




def get_order(order_number):
    return request.put(configuration.URL_SERVICE + configuration.ORDER_BY_NUMBER + order_number)

def post_create_order(body):
    return request.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                        json=body,  # тут тело
                        headers=data.headers)  # а здесь заголовки)



# Функция для позитивной проверки
def positive_assert():
    
    order_number = post_create_order(data.user_body).json()
    assert get_order(order_number).status_code == 200
    
