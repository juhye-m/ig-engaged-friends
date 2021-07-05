# https://stackoverflow.com/questions/54870270/getting-list-of-likers-for-an-instagram-post-python-selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()

driver.get('https://www.instagram.com/accounts/login')

# login https://gist.github.com/tacomonster/555bceef3d14673810f625edd000c112
time.sleep(2)
user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
user_name_elem.clear()
user_name_elem.send_keys('****')
passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
passworword_elem.clear()
passworword_elem.send_keys('****')
passworword_elem.send_keys(Keys.RETURN)
time.sleep(5)



not_now = driver.find_element_by_xpath("//button[@class='sqdOP yWX7d    y3zKF     ']")
if not_now:
    not_now.click()

time.sleep(5)
no_notifs = driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']")
if no_notifs:
    no_notifs.click()

time.sleep(2)
driver.get('https://www.instagram.com/p/CO3PxMVLxQM/')
time.sleep(2)

liked_by = driver.find_element_by_xpath("//a[@href='/p/CO3PxMVLxQM/liked_by/']")
likes = driver.find_element_by_xpath("//a[@href='/p/CO3PxMVLxQM/liked_by/']/span")
likes_num = int(likes.text) # number of likes the post has
liked_by.click()

time.sleep(5)

elems = []
# Scroll https://stackoverflow.com/questions/53681446/scroll-down-followers-following-list-in-the-instagram-box
elems_in_view = driver.find_elements_by_xpath("//a[@class='FPmhX notranslate MBL3Z']")
# https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector
# driver.execute_script('''
#     var fDialog = document.querySelector('div[role="dialog"] class='pbNvD  fPMEg     '');
#     fDialog.scrollTop = fDialog.scrollHeight
# ''')

# for i in range(1,7):
#     elems_in_view = driver.find_elements_by_xpath("//a[@class='FPmhX notranslate MBL3Z']")
#     driver.execute_script('''
#         var fDialog = document.querySelector('div[role="dialog"]');
#         fDialog.scrollTop = fDialog.scrollHeight
#     ''')
#     elems_in_view = driver.find_elements_by_xpath("//a[@class='FPmhX notranslate MBL3Z']")
#     elems.extend(elems_in_view)

dialog = driver.find_elements_by_xpath("//div[@class='pbNvD  fPMEg     ']")

# for i in range(1,7):
#     elems_in_view = driver.find_elements_by_xpath("//a[@class='FPmhX notranslate MBL3Z']")
    
#     driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", dialog)
#     elems.extend(elems_in_view)

users = []

xxx = driver.find_elements_by_xpath("//div[@class='                     Igw0E     IwRSH      eGOV_        vwCYk                                                                            i0EQd                                   ']")
xxx[0].click()
# dialog = driver.find_elements_by_xpath("//div[@class='_1XyCr ']")
actionChain = webdriver.ActionChains(driver)

count = 0; # max number of likes the post has

while count < likes_num:
    elems_in_view = driver.find_elements_by_xpath("//a[@class='FPmhX notranslate MBL3Z']")
    # elems.extend(elems_in_view)
    # [users.append(elem.get_attribute('title')) for elem in elems_in_view if elem.get_attribute('title') not in users]
    for elem in elems_in_view:
        title = elem.get_attribute('title')
        if title not in users:
            users.append(title)
            count += 1
    # driver.execute_script(
    #     'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', 
    #   dialog)
    xxx[0].click()
    actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
    print(count)
    time.sleep(2)


# print("hey")

# for elem in elems:
#     # print("yo")
#     users.append(elem.get_attribute('title'))
for user in users:
    print(user)

print(users)

# wait 1 minute
time.sleep(60)
driver.quit()