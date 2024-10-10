import pytest
import allure
import requests

@allure.tag("regression", "p0", "smoke")
@allure.label("owner", "Akshay")
@allure.title("Test GET Request - RestFUL BOOKER Project#1")
@allure.description("TC#1 -> Verify that GET Request with ID works")
@pytest.mark.smoke
def test_get_single_request_by_id_positive():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url)
    print(response_data.text,"here1")
    assert response_data.status_code == 200


@allure.title("Test GET Request - RestFUL BOOKER Project#2")
@allure.description("TC#2 -> Verify that GET Request with invalid bookingID")
@pytest.mark.smoke
def test_get_single_request_by_id_negaitve1():
    url = "https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(url)
    print(response_data.text, "here2")
    assert response_data.status_code == 405


@allure.title("Test GET Request - RestFUL BOOKER Project#3")
@allure.description("TC#3 -> Verify that GET Request with invalid bookingID")
@pytest.mark.smoke
def test_get_single_request_by_id_negative2():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    response_data  = requests.get(url)
    print(response_data.text,"here3")
    assert response_data.status_code == 406


@allure.title("Test GET Request - RestFUL BOOKER Project#4")
@allure.description("TC#4 -> Verify that GET Request with invalid bookingID")
@pytest.mark.smoke
def test_get_single_request_by_id_negative3():
    url = "https://restful-booker.herokuapp.com/booking/9876.8976"
    response_data  = requests.get(url)
    print(response_data.text,'here4')
    assert response_data.status_code == 407


@allure.title("Test GET Request - RestFUL BOOKER Project#5")
@allure.description("TC#5 -> Verify that GET Request with invalid bookingID")
@pytest.mark.smoke
def test_get_single_request_by_id_negative4():
    url = "https://restful-booker.herokuapp.com/not_found"
    response_data  = requests.get(url)
    print(response_data.text,'here5')
    assert response_data.status_code == 408

# allure serve allure_result
# pytest -m "smoke" task_8oct.py --alluredir=allure_result -v -s

