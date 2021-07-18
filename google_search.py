import time,goaptiPostJobs,goaptiLogin
jobLinks =[
'https://www.google.com/search?q=fresher+jobs&rlz=1C1GCEA_enIN885IN885&oq=fre&aqs=chrome.0.69i59j69i57j0i271l3j69i60l2.1297j0j7&sourceid=chrome&ie=UTF-8&safe=active&ibp=htl;jobs&sa=X&ved=2ahUKEwjVrc-oldXxAhXPyjgGHQAhB50QutcGKAB6BAgGEAQ#htivrt=jobs&fpstate=tldetail&htichips=date_posted:today,gcat_category.id:GC08&htischips=date_posted;today,gcat_category.id;GC08:ComputerIT&htidocid=CiBhcWy7a8nmiuTfAAAAAA%3D%3D',
'https://www.google.com/search?q=fresher+jobs+pune&rlz=1C1GCEA_enIN885IN885&oq=fre&aqs=chrome.0.69i59j69i57j0i271l3j69i60l2.1297j0j7&sourceid=chrome&ie=UTF-8&safe=active&ibp=htl;jobs&sa=X&ved=2ahUKEwjVrc-oldXxAhXPyjgGHQAhB50QutcGKAB6BAgGEAQ#fpstate=tldetail&htivrt=jobs&htichips=date_posted:today,gcat_category.id:GC08&htischips=date_posted;today,gcat_category.id;GC08:ComputerIT&htidocid=SvLonvl-z73POKf0AAAAAA%3D%3D',
'https://www.google.com/search?q=fresher+jobs+mumbai&rlz=1C1GCEA_enIN885IN885&oq=fre&aqs=chrome.0.69i59j69i57j0i271l3j69i60l2.1297j0j7&sourceid=chrome&ie=UTF-8&safe=active&ibp=htl;jobs&sa=X&ved=2ahUKEwjVrc-oldXxAhXPyjgGHQAhB50QutcGKAB6BAgGEAQ#fpstate=tldetail&htivrt=jobs&htilrad=50.0&htichips=gcat_category.id:GC08,date_posted:today&htischips=gcat_category.id;GC08:ComputerIT,date_posted;today&htidocid=D5DT5YjsTuM9cpFNAAAAAA%3D%3D',
'https://www.google.com/search?q=fresher+jobs+in+hyderabad&rlz=1C1GCEA_enIN885IN885&oq=fre&aqs=chrome.0.69i59j69i57j0i271l3j69i60l2.1297j0j7&sourceid=chrome&ie=UTF-8&safe=active&ibp=htl;jobs&sa=X&ved=2ahUKEwjVrc-oldXxAhXPyjgGHQAhB50QutcGKAB6BAgGEAQ#fpstate=tldetail&htivrt=jobs&htichips=date_posted:today,gcat_category.id:GC08&htischips=date_posted;today,gcat_category.id;GC08:ComputerIT&htilrad=50.0&htidocid=zWo9PVwNCpgPz0WDAAAAAA%3D%3D',
'https://www.google.com/search?q=freshers+jobs+delhi&sxsrf=ALeKk01DKeS1xcO4sY7AinwUHzaIxMysAg:1625896470728&ei=FjbpYJjwK_rXz7sP57OYiA0&oq=freshers+jobs+delhi&gs_lcp=Cgdnd3Mtd2l6EAMyAggAMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeOgcIABBHELADOggIABCxAxCDAToFCAAQyQM6BAgAEEM6CQgAEMkDEBYQHkoECEEYAFC4CFjzFGCHGGgAcAN4AIAB5wKIAfEOkgEFMi01LjKYAQCgAQGqAQdnd3Mtd2l6yAEIwAEB&sclient=gws-wiz&uact=5&safe=active&ibp=htl;jobs&sa=X&ved=2ahUKEwjszPqu6NfxAhUA6nMBHSBGC28QudcGKAJ6BAgGECg#fpstate=tldetail&htivrt=jobs&htilrad=50.0&htichips=gcat_category.id:GC08,date_posted:today&htischips=gcat_category.id;GC08:ComputerIT,date_posted;today&htidocid=DjUCOh6y3RyVO-2_AAAAAA%3D%3D'
]
def scroll(driver,googleWindow,count):
    jobList = driver.find_elements_by_xpath('//div[@id="VoQFxe"]/div')
    if(len(jobList)>count):
        jobs = driver.find_elements_by_xpath('//div[@id="VoQFxe"]/div[' + str(count + 1) + ']/div/ul/li')
        for j in jobs:
            j.click()
            basePath = '//div[@id="tl_ditc"]/div/div/'
            title = driver.find_element_by_xpath(basePath + 'div[@class="sVx81"]/div[@class="OghIW"]/div/h2').text
            companyName = driver.find_element_by_xpath(
                basePath + 'div[@class="sVx81"]/div[@class="OghIW"]/div[@class="iGy6ud"]/div[@class="tJ9zfc"]/div[1]').text
            location = driver.find_element_by_xpath(
                basePath + 'div[@class="sVx81"]/div[@class="OghIW"]/div[@class="iGy6ud"]/div[@class="tJ9zfc"]/div[2]').text
            urls = driver.find_elements_by_partial_link_text("Apply on")
            url = urls[0].get_attribute('href')
            # url = driver.find_element_by_xpath('//div[@class="B8oxKe"]/span[@class="DaDV9e"]/a').get_attribute('href')
            time.sleep(1)

            jobTime=driver.find_element_by_xpath(basePath + 'div[4]/span[1]/span[2]').text

            description = ""
            red = driver.find_elements_by_xpath(basePath + 'div[5]/div/span[@class="HBvzbc"]/span')
            if (len(red) > 0):
                driver.find_element_by_xpath(basePath + 'div[5]/div/div').click()
                description += driver.find_element_by_xpath(basePath + 'div[5]').text
            else:
                description += driver.find_element_by_xpath(basePath + 'div[5]/span').text

            if((int(jobTime.split(" ")[0])<=5) or (int(jobTime.split(" ")[0])>24) ):
                goaptiPostJobs.postJobs(driver, title, location, description, url, companyName)
                print(title)
                print(location)
                print(companyName)
                print(url)
                print(jobTime)


            time.sleep(5)
            driver.switch_to.window(googleWindow)
            time.sleep(2)
        scroll(driver,googleWindow,count+1)
    else:
        return
def search(driver):
    for element in jobLinks:
        driver.get(element)
        driver.maximize_window()
        googleWindow = driver.window_handles[0]
        time.sleep(1)
        scroll(driver,googleWindow,0)
    scroll(driver, googleWindow, count + 1)




