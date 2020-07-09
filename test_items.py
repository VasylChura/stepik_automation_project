from selenium import webdriver
import  time

def test_is_there_addbusket_button(browser):
    browser.implicitly_wait(5)
    add_button = browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
    time.sleep(10)

    button_text = add_button.text
    #print("---------" + button_text + "----------")
    assert button_text == "Añadir al carrito" or button_text == "Ajouter au panier", "There is no add busket button or wrong language!!!"