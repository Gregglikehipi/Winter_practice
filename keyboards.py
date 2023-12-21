from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from DBHelper import DBHelper


def get_start():
    key = VkKeyboard(one_time=True)
    key.add_button('Каталог 🗂', color=VkKeyboardColor.SECONDARY)
    key.add_button('Корзина 🛒', color=VkKeyboardColor.SECONDARY)
    key.add_line()
    key.add_button('Заказы 📋', color=VkKeyboardColor.SECONDARY)
    key.add_button('Акции 💯', color=VkKeyboardColor.SECONDARY)
    key.add_line()
    key.add_button('Анкета 📝', color=VkKeyboardColor.SECONDARY)
    key.add_button('Помощь 🙏', color=VkKeyboardColor.SECONDARY)
    key.add_line()
    key.add_button('О нас 🏪', color=VkKeyboardColor.SECONDARY)
    return key


def get_start_for_admin():
    key = VkKeyboard(one_time=True)
    key.add_button('Список заказов 📖', color=VkKeyboardColor.SECONDARY)
    key.add_line()
    key.add_button('Изменить статус заказа 🔁', color=VkKeyboardColor.SECONDARY)
    key.add_line()
    key.add_button('Изменить акцию 💯', color=VkKeyboardColor.SECONDARY)
    key.add_line()
    key.add_button('Режим пользователя👥', color=VkKeyboardColor.SECONDARY)
    return key


def get_katalog():
    key = VkKeyboard(one_time=True)
    key.add_button('Корзина 🛒', color=VkKeyboardColor.SECONDARY)
    key.add_line()
    key.add_button('Поиск 🔎', color=VkKeyboardColor.SECONDARY)
    key.add_button('На главную 🏡', color=VkKeyboardColor.SECONDARY)
    return key


def get_anketa():
    key = VkKeyboard(one_time=True)
    key.add_button('Имя 👩👨', color=VkKeyboardColor.SECONDARY)
    key.add_button('Телефон 📞', color=VkKeyboardColor.SECONDARY)
    key.add_line()
    key.add_button('Адрес 🏨', color=VkKeyboardColor.SECONDARY)
    key.add_button('Город 🏤', color=VkKeyboardColor.SECONDARY)
    key.add_line()
    key.add_button('На главную 🏡', color=VkKeyboardColor.SECONDARY)
    return key


def get_back_anketa():
    key = VkKeyboard(one_time=True)
    key.add_button('Назад ⬅', color=VkKeyboardColor.SECONDARY)
    return key


def get_basket():
    key = VkKeyboard(one_time=True)
    key.add_button('На главную 🏡', color=VkKeyboardColor.SECONDARY)
    key.add_button('Оформить заказ 📦', color=VkKeyboardColor.SECONDARY)
    return key


def get_order():
    key = VkKeyboard(one_time=True)
    key.add_button('На главную 🏡', color=VkKeyboardColor.SECONDARY)
    return key


def get_making():
    key = VkKeyboard(one_time=True)
    key.add_button('Самовывоз 🚹', color=VkKeyboardColor.SECONDARY)
    key.add_button('Доставка 🚕', color=VkKeyboardColor.SECONDARY)
    key.add_line()
    key.add_button('На главную 🏡', color=VkKeyboardColor.SECONDARY)
    return key


def get_pay():
    key = VkKeyboard(one_time=True)
    key.add_button('Наличными при получении 💵', color=VkKeyboardColor.SECONDARY)
    key.add_button('Переводом на карту 💳', color=VkKeyboardColor.SECONDARY)
    key.add_line()
    key.add_button('На главную 🏡', color=VkKeyboardColor.SECONDARY)
    return key


def get_chat():
    key = VkKeyboard(one_time=True)
    key.add_button('Оператор 📞', color=VkKeyboardColor.SECONDARY)
    key.add_openlink_button('Чат с менеджером 🗒', link="https://vk.com/sellstolen")
    key.add_line()
    key.add_button('На главную 🏡', color=VkKeyboardColor.SECONDARY)
    return key


def get_product():
    key = VkKeyboard(one_time=True)
    key.add_button('Корзина 🛒', color=VkKeyboardColor.SECONDARY)
    key.add_line()
    key.add_button('На главную 🏡', color=VkKeyboardColor.SECONDARY)
    return key


def get_home():
    key = VkKeyboard(one_time=True)
    key.add_button('На главную 🏡', color=VkKeyboardColor.SECONDARY)
    return key


def get_list():
    product_names = get_name()
    keys = VkKeyboard(one_time=True)

    for i in range(len(product_names)):
        name = product_names[i]
        keys.add_button(name + " ✅", color=VkKeyboardColor.SECONDARY)
        keys.add_line()
    keys.add_button("Поиск 🔎")
    return keys


def get_list_basket(name): # TODO
    product_names = get_name_search(name)
    keys = VkKeyboard(one_time=True)

    for i in range(len(product_names)):
        name = product_names[i]
        newName = name + " 📦"
        keys.add_button(newName, color=VkKeyboardColor.SECONDARY)
        keys.add_line()
    keys.add_button('На главную 🏡')
    return keys

def get_list_search(name):
    product_names = get_name_search(name)
    keys = VkKeyboard(one_time=True)

    for i in range(len(product_names)):
        name = product_names[i]
        newName = name + " ✅"
        keys.add_button(newName, color=VkKeyboardColor.SECONDARY)
        keys.add_line()
    keys.add_button('На главную 🏡')
    return keys


def get_name():
    helper = DBHelper()
    products_ = helper.print_info('product')
    product_names = []
    index = 0
    for prod in products_:
        product_names.append(prod[1])
    return product_names


def get_name_for_search():
    helper = DBHelper()
    products_ = helper.print_info('product')
    product_names = []
    index = 0
    for prod in products_:
        product_names.append(prod[1] + " ✅")
    return product_names


def get_name_search(name):
    helper = DBHelper()
    products_ = helper.print_info('product')
    product_names = []
    index = 0
    for prod in products_:
        if name.lower() in prod[1].lower():
            product_names.append(prod[1])
    return product_names


def get_name_vkid(vkid): # TODO
    helper = DBHelper()
    products_ = helper.print_info('product')
    product_names = []
    index = 0
    for prod in products_:
        if name.lower() in prod[1].lower():
            product_names.append(prod[1])
    return product_names