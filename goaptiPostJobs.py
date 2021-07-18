import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import goaptiLogin


def postJobs(browser,title,location,description,url,companyName):
    goaptiLogin.login(browser)
    jobTitle=WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "job_title")))
    jobTitle.clear()
    jobTitle.send_keys(title)
    jobLocation=browser.find_element_by_id("job_location")
    jobLocation.clear()
    jobLocation.send_keys(location)
    jobCategory=browser.find_element_by_class_name("select2-search__field")
    jobCategory.clear()
    jobCategory.send_keys("Freshers Job")
    jobCategory.send_keys(Keys.ENTER)
    jobDescription=browser.find_element_by_id("job_description")
    jobDescription.clear()
    jobDescription.send_keys(description)
    jobURL=browser.find_element_by_id("application")
    jobURL.clear()
    jobURL.send_keys(url)
    jobCompany=browser.find_element_by_id("company_name")
    jobCompany.clear()
    jobCompany.send_keys(companyName)
    browser.find_element_by_name("submit_job").send_keys(Keys.ENTER)
    browser.find_element_by_id("job_preview_submit_button").click()
    browser.close()