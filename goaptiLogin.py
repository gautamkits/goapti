import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def login(browser):
    browser.execute_script('''window.open("https://goapti.in/job-submission/","_blank");''')
    jobSubmission=browser.window_handles[1]
    browser.switch_to.window(jobSubmission)
    # browser.get('https://goapti.in/job-submission/')
    browser.maximize_window()
    time.sleep(2)
    signinCheck=browser.find_elements_by_id("pwbox-90743")
    if(len(signinCheck)>0):
        password=WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.ID, "pwbox-90743")))
        password.send_keys("test123")
        password.send_keys(Keys.ENTER)

        signin=WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '//fieldset[@class="fieldset-login_required"]/div/a')))
        signin.click()

        username=WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.ID, 'user_login')))
        pwd=browser.find_element_by_id("user_pass")

        username.clear()
        username.send_keys("dailyquizgoapti@gmail.com")
        pwd.clear()
        pwd.send_keys("dailyquizgoapti@gmail.com")

        browser.find_element_by_id("wp-submit").click()
        browser.maximize_window()




