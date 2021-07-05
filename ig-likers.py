# https://stackoverflow.com/questions/54870270/getting-list-of-likers-for-an-instagram-post-python-selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
driver = webdriver.Chrome()

def login():

    driver.get('https://www.instagram.com/accounts/login')

    # login https://gist.github.com/tacomonster/555bceef3d14673810f625edd000c112
    time.sleep(2)
    usr = input("Enter Instagram username: ")
    pwd = input("Enter Instagram password: ")
    user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
    user_name_elem.clear()

    
    user_name_elem.send_keys(usr)
    passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
    passworword_elem.clear()

    
    passworword_elem.send_keys(pwd)
    passworword_elem.send_keys(Keys.RETURN)

    # TODO invalid log in warning 
    time.sleep(5)

    not_now = driver.find_element_by_xpath("//button[@class='sqdOP yWX7d    y3zKF     ']")
    if not_now:
        not_now.click()

    time.sleep(5)
    no_notifs = driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']")
    if no_notifs:
        no_notifs.click()

# POST LIKERS!!!!!!

def get_likers(link_pic):

    time.sleep(2)
    driver.get(link_pic)
    time.sleep(2)

    liked_by = driver.find_element_by_xpath("//a[@href='/p/CO3PxMVLxQM/liked_by/']")
    likes = driver.find_element_by_xpath("//a[@href='/p/CO3PxMVLxQM/liked_by/']/span")
    likes_num = int(likes.text) + 1 # number of likes the post has
    liked_by.click()

    time.sleep(5)

    # Scroll https://stackoverflow.com/questions/53681446/scroll-down-followers-following-list-in-the-instagram-box
    elems_in_view = driver.find_elements_by_xpath("//a[@class='FPmhX notranslate MBL3Z']")

    users = []

    xxx = driver.find_elements_by_xpath("//div[@class='                     Igw0E     IwRSH      eGOV_        vwCYk                                                                            i0EQd                                   ']")
    xxx[0].click()
    actionChain = webdriver.ActionChains(driver)

    count = 0; # max number of likes the post has

    while count < 50:
        elems_in_view = driver.find_elements_by_xpath("//a[@class='FPmhX notranslate MBL3Z']")
        for elem in elems_in_view:
            title = elem.get_attribute('title')
            if title not in users:
                users.append(title)
                count += 1
        # keeps dialog box engaged
        xxx[0].click()
        actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
        print(count)
        time.sleep(2)
    users.sort()
    return users

def get_following():
    driver.get('https://www.instagram.com/juhye.m')
    following = driver.find_element_by_xpath("//a[@href='/juhye.m/following/']")
    following.click()
    # following_num = driver.find_element_by_xpath("//span[@class='g47SY lOXF2'][3]")
    # print(following_num)
    # following_num2= following_num[2].text
    # print(following_num2)
    time.sleep(2)
    dialog = driver.find_elements_by_xpath("//div[@class='isgrP']")
    # print(dialog)
    dialog[0].click()
    actionChain = webdriver.ActionChains(driver)
    count = 0
    users = []
    while count < 30:
        elems_in_view = driver.find_elements_by_xpath("//a[@class='FPmhX notranslate  _0imsa ']")
        for elem in elems_in_view:
            title = elem.get_attribute('title')
            if title not in users:
                users.append(title)
                count += 1
        # keeps dialog box engaged
        dialog[0].click()
        actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
        print(count)
        time.sleep(2)
    users.sort()
    return users


def write_to_csv(lst, filename):
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        for item in lst:
            writer.writerow([item])  # brackets one string per row, no character delimiter



if __name__ == "__main__":
    # https://www.pythontutorial.net/python-basics/python-write-csv-file/
    # users = get_likers('https://www.instagram.com/p/CO3PxMVLxQM/')
    # print(users)

    login()
    write_to_csv(get_following(), 'following.csv')


    # wait 1 minute
    time.sleep(60)
    driver.quit()