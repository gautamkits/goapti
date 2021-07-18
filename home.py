from selenium import webdriver
import google_search,goaptiLogin,goaptiPostJobs

try:
    browser = webdriver.Chrome('C:\\Users\\GASHARMA\\PycharmProjects\\pythonProject\\JobAutomation\\DriverFolder\\chromedriver.exe')
    google_search.search(browser)

except Exception as e:
    print(e)
    browser.quit()

else:
    browser.quit()




