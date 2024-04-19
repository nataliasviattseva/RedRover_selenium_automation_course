# AUTH
USERNAME_FIELD = '//input[@data-test="username"]'
PASSWORD_FIELD = '//input[@data-test="password"]'
LOGIN_BUTTON = '//input[@data-test="login-button"]'
LOGIN_ERROR_MESSAGE = '//*[@id="login_button_container"]/div/form/div[3]/h3'
LOGIN_ERROR_MESSAGE_TEXT = 'Epic sadface: Username and password do not match any user in this service'

# CART PAGE
BACKPACK_ADD_BUTTON = 'add-to-cart-sauce-labs-backpack'
CART_BUTTON = 'shopping_cart_link'
BACKPACK_ITEM = '//*[@id="item_4_title_link"]/div'
BACKPACK_DELETE_BUTTON = 'remove-sauce-labs-backpack'
ADD_TO_CART = 'add-to-cart'
REMOVE_BUTTON = 'remove'
CART_LOGO = '//*[@data-test="shopping-cart-link"]'
CART_LOGO_BADGE = '//*[@data-test="shopping-cart-badge"]'

# FILTERS
FILTER_ELEMENT = 'product_sort_container'
FILTER_VALUES = ('Name (A to Z)', 'Name (Z to A)', 'Price (low to high)', 'Price (high to low)')
FIRST_ELEMENT = '(//*[@data-test="inventory-item-name"])[1]'
ITEM_TEXTS = ('Sauce Labs Backpack',
             'Test.allTheThings() T-Shirt (Red)',
             'Sauce Labs Onesie',
             'Sauce Labs Fleece Jacket')

# INVENTORY ITEM
BACKPACK_IMAGE = 'item_4_img_link'
BACKPACK_TITLE = 'item_4_title_link'
BACKPACK_ITEM_TEXT = '//*[@id="inventory_item_container"]/div/div/div[2]/div[1]'
INVENTORY_ITEM_FRAME = 'inventory_item_container'

# BURGER MENU
BURGER_MENU = 'react-burger-menu-btn'
BURGER_MENU_ITEMS = ('inventory_sidebar_link',
                     'about_sidebar_link',
                     'logout_sidebar_link',
                     'reset_sidebar_link')

