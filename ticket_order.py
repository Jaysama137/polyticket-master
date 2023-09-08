# 以下代码部分引用了Andrewmore在Gitee上的 AutoTicketForPoly的代码
# 原始代码链接: https://gitee.com/andrewmore/auto-ticket-for-poly
# 作者: Andrewmore

from os import name
import select
from xml.sax.xmlreader import Locator
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

#测试使用chrome版本：116.0.5845.180

#抢票目标页
target_url="https://whqtdjy.polyt.cn/#/detail?productId=5896100"

class Concert(object):
    def __init__(self):
        self.status = 0
        self.login_method = 0
        self.date = 1  #选择哪一天，按数字排列，比如2021-01-01，2021-01-02，2021-01-03可选，想选01-01填1，想选01-02填2
        self.price= 2  #买哪一档票，从贵到便宜，1，2，3
        self.total_wait_time = 5   #WebDriverWait总等待时间
        self.refresh_wait_time = 0.1 #WebDriverWait刷新动作的时间
        self.name = "张三"
        self.phonenum = "11451411451"
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")  #控制当前chrome页面
        chrome_driver = "D:/auto-ticket-for-poly-master/chromedriver.exe" # 指定自己的chromedriver路径
        self.driver = webdriver.Chrome(chrome_driver, options=chrome_options)
        print("初始化成功，载入页面中")
    
    def isClassPresent(self, item, name, ret=False):
        try:
            result = item.find_element_by_class_name(name)
            if ret:
                return result
            else:
                return True
        except:
            return False


    def prepare(self):
        self.driver.get(target_url)
        self.driver.refresh()
        start = False
        locator = (By.XPATH, "//*[@id=\"app\"]/div/section/div[2]/div/div/div[2]/div/div[1]/div[2]/div[2]/div/div[1]/div[2]")
        while not start:
            try:
                WebDriverWait(self.driver, 100,0.1).until(EC.text_to_be_present_in_element(locator,'售票中'))
                print("获取页面成功")
                break
            except Exception as e:
                print("未开始")

    def choose_ticket(self):
        choiceTime_xpath = "//*[@id=\"app\"]/div/section/div[2]/div/div/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div[2]" #售票时间
        choicePrice_xpath = "//*[@id=\"app\"]/div/section/div[2]/div/div/div[2]/div/div[1]/div[2]/div[2]/div/div[3]/div[2]" #售票价位
        checkbut_xpath  = "//*[@id=\"app\"]/div/section/div[2]/div/div/div[2]/div/div[1]/div[2]/div[2]/div/div[4]/div[2]/button"#选座购买按钮

        while self.driver.current_url.find('selectSeat') == -1:           #如果跳转到了订单结算界面就算这步成功了，否则继续执行此步
            #选择日期
            print("="*30)
            print("###开始进行日期选择###") 

            #选择时间
            choiceTime = WebDriverWait(self.driver, self.total_wait_time, self.refresh_wait_time).until(
                    EC.presence_of_element_located((By.XPATH, choiceTime_xpath)))
            choiceTime_list = choiceTime.find_elements_by_tag_name('span')  

            if self.date>len(choiceTime_list):
                actualDate = choiceTime_list[0]
                print("想选的日期不存在，自动选择" + actualDate)
                choiceTime_list[0].click()
            else:
                choiceTime_list[self.date-1].click()
            print("日期选择中")


            """
            #选择价位
            print("="*30)
            print("###开始进行价位选择###")
            
            choicePrice = WebDriverWait(self.driver, self.total_wait_time, self.refresh_wait_time).until(
                    EC.presence_of_element_located((By.XPATH, choicePrice_xpath)))
            choicePrice_list = choicePrice.find_elements_by_tag_name('span')  

            if self.price>len(choicePrice_list):
                actualPrice = choicePrice_list[0]
                print("想选的价位不存在，自动选择" + actualPrice)
                choicePrice_list[0].click()
            else:
                choicePrice_list[self.date-1].click()
            
            print("价位选择中")
            """

            #按下选座购票按钮
            checkbut = self.driver.find_element_by_xpath(checkbut_xpath)
            checkbut.click()

            time.sleep(self.refresh_wait_time)

        print("###日期价位选择成功###")

    def seatSelectbyhand(self):
        print("="*30)
        print("###开始进行座位选择###")
        fullscreenbut_xpath = "//*[@id=\"seatContent\"]/div/div[1]/div[2]/div/div[2]"
        confirmbut_xpath = "//*[@id=\"seatContent\"]/div/div[3]/div/div[3]/div[1]/div/div/section/div[2]/button"

        fullscreenbut = WebDriverWait(self.driver, self.total_wait_time, self.refresh_wait_time).until(
                EC.presence_of_element_located((By.XPATH, fullscreenbut_xpath)))
        fullscreenbut.click()

        print("正在等待手动选择")

        while self.driver.current_url.find('orderDetail') == -1:
            print("正在等待跳转支付页面")
            

            #等待出现结账按钮
            try:
                # 等待结账按钮出现并且可以点击
                element = WebDriverWait(self.driver, self.total_wait_time, self.refresh_wait_time).until(
                    EC.element_to_be_clickable((By.XPATH, confirmbut_xpath))
                )
                
                element.click()
                
                print("###手动座位选择成功###")

                time.sleep(self.refresh_wait_time)
                
            except Exception as e:
                print("手动座位选择失败:", str(e))

            
        print("###座位选择成功###")
            
    def checkout(self):
        print("="*30)
        print("###开始填写支付信息###")

        name_input_xpath = "//*[@id=\"pane-self\"]/div/div[2]/form/div[1]/div/div/input"
        phontnum_input_xpath = "//*[@id=\"pane-self\"]/div/div[2]/form/div[2]/div/div/input"
        payway_xpath = "//*[@id=\"app\"]/div/section/div[2]/div/div/div/div[3]/div[2]/div[1]" #第一项，微信支付
        agreement_xpath = "//*[@id=\"app\"]/div/section/div[2]/div/div/div/div[5]/div[2]/div[1]/div/label/span[1]/span"
        checkoutbut_xpath = "//*[@id=\"app\"]/div/section/div[2]/div/div/div/div[5]/div[2]/div[2]/button"

        name_input = WebDriverWait(self.driver, self.total_wait_time, self.refresh_wait_time).until(
                    EC.presence_of_element_located((By.XPATH, name_input_xpath)))
        name_input.clear()
        name_input.send_keys(self.name)
        print("###姓名填写成功###")

        phontnum_input = self.driver.find_element_by_xpath(phontnum_input_xpath)
        phontnum_input.clear()
        phontnum_input.send_keys(self.phonenum)
        print("###手机号填写成功###")

        payway = self.driver.find_element_by_xpath(payway_xpath)
        payway.click()
        print("###支付方式选择成功###")

        agreement = self.driver.find_element_by_xpath(agreement_xpath)
        agreement.click()
        print("###同意协议成功###")

        checkoutbut = self.driver.find_element_by_xpath(checkoutbut_xpath)
        checkoutbut.click()
        print("###订单提交成功###")


if __name__ == '__main__':
    try:
        con = Concert()             #具体如果填写请查看类中的初始化函数
        con.prepare()
        con.choose_ticket()
        con.seatSelectbyhand()
        con.checkout()

    except Exception as e:
        print(e)
        con.finish()




