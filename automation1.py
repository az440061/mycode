from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

# import xlsxwriter
from csv import writer
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://recro-team.freshteam.com/")
action = ActionChains(driver)
# workbook = xlsxwriter.Workbook('JavaRemote.xlsx'

def Freshteam():
    driver.maximize_window()

    driver.implicitly_wait(20)
    print("debugging #1 entering username and password")
    driver.find_element(By.ID, 'username').send_keys("ismail@recro.io")
    driver.find_element(By.ID, "password").send_keys("Initial@123")
    driver.find_element(By.CLASS_NAME, "css-o1ejds").click()
    driver.implicitly_wait(20)
    driver.find_element(By.ID, "ember216").click()
    driver.implicitly_wait(15)
    myDivs = driver.find_elements(By.CLASS_NAME, "col-inside")
    print("Find my anchor", len(myDivs))
    # print("what is in titles", myDivs.find_element(By.LINK_TEXT, '/hire/jobs/4000013308/applicants'))
    pushNewpage = False
    for myitem in myDivs:
        myancor = myitem.find_element(By.TAG_NAME, 'a')
        if "/hire/jobs/4000013308/applicants" in myancor.get_attribute("href"):
            print("Bingo click this now")
            myancor.click()
            pushNewpage = True
            break

    candidateParsing()


def candidateParsing():

    tdlist = driver.find_elements(By.XPATH, "s//tr[@class='candidate-list-item   ']/td[@class='onhover-active']")
    for mylist in tdlist:
        action.move_to_element(mylist).perform()
        popoverDiv = mylist.find_element(By.XPATH , "//tr[@class='candidate-list-item   ']/td[@class='onhover-active']")
        if len(onhover) < 1:
            continue
        onhover = popoverDiv[0]

        name = onhover.find_element(By.CLASS_NAME , "semi bold ellipsis")
        print("name" , name.text)

        email = onhover.find_element(By.XPATH, "//div[@class='popover-content contact-popover']/div[class='btn-full-width ellipsis'][1]")
        print("email",email.text)

        if check_exists_by_xpath("//div[@class='popover-content contact-popover']/div[class='btn-full-width ellipsis'][2]"):
            mobile = onhover.find_element(By.XPATH , "//div[@class='popover-content contact-popover']/div[class='btn-full-width ellipsis'][2]")
            print("mobile" , mobile.text)

            #
            # candidateList = [name.text,email.text,mobile.text]
            #
            # with open('candidate list.csv' , 'a')


def check_exists_by_xpath(xpath):
    try:
        driver.find_element(By.XPATH)

    except NoSuchElementException:
        return False
    return True






Freshteam()