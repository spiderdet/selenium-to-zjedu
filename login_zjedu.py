from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class zjedu_info:
    def __init__(self):
        url = 'https://jsfzxx.zjedu.gov.cn/ability/login'
        self.url = url
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        options.add_argument(
            'User-Agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"')
        options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})  # 不加载图片,加快访问速度
        options.add_experimental_option('excludeSwitches',
                                        ['enable-automation'])  # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
        self.browser = webdriver.Chrome(executable_path=chromedriver_path, options=options)
        self.wait = WebDriverWait(self.browser, 5)  # 超时时长为10s

    # 登录
    def login(self):
        # 打开网页
        self.browser.get(self.url)
        # 等待 账号 出现s
        weibo_user = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="text"]')))
        weibo_user.send_keys(username)

        # 等待 密码 出现
        weibo_pwd = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"]')))
        weibo_pwd.send_keys(password)

        # 等待 登录按钮 出现
        submit = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.login-button')))
        submit.click()

        # 直到获取到个人中心才能确定是登录成功
        main_header = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                      'ul.main-header-menu > li:nth-of-type(4)')))
        # 输出个人中心
        print(main_header.text)
        if main_header.text == "个人中心":
            print("Same， 登录成功")
        else:
            print("Different， 登录失败")

        #报名学习 师德教育专题学习，并跳转到新页面
        #文本定位 用 css还不知道怎么弄， 用xpath   可以这样 //*[contains(text(），'后台审核')] 经试验不行！
        # shide = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
        #                                                               'p[title=师德教育专题学习'))) 这个可以
        # shide = self.wait.until(EC.presence_of_element_located((By.XPATH,
        #                                                         "//p[text()='师德教育专题学习']")))  这个可以
        # print(shide.text)
        baoming = self.wait.until(EC.presence_of_element_located((By.XPATH,"//p[text()='师德教育专题学习']/following-sibling::button[1]")))
        print(baoming.text)
        old_window = self.browser.current_window_handle  # 定位当前页面句柄
        baoming.click()

        ## 进入新页面
        # sleep(3)  没有显性等待的方法就只能用sleep的等待方法了
        # all_handles = self.browser.window_handles  # 获取全部页面句柄
        self.wait.until(EC.number_of_windows_to_be(2))
        all_handles = self.browser.window_handles  # 获取全部页面句柄
        print(len(all_handles))
        new_window = [window for window in all_handles if window != old_window][0]
        # 或直接 new_window = all_handles[1]
        self.browser.switch_to.window(new_window)  # 切换到新页面

        ## 点击幼儿园的进入学习
        main_list = self.wait.until(EC.presence_of_element_located((By.XPATH,
                                                                      '//div[@class="main_list"]')))
        print("main_list text:", main_list.text)
        baomingxuexi = self.browser.find_elements_by_link_text("进入学习")
        for i in baomingxuexi:
            print("a.text:",i.text)
            print("a previous text",i.find_element_by_xpath("preceding-sibling::span[1]").text)
        baomingxuexi[1].click()

        ##
        max_position = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".max-position"))).text
        print(max_position)

if __name__ == "__main__":
    chromedriver_path = 'chromedriver.exe'  # 改成你的chromedriver的完整路径地址
    username = "wh115622"  # 改成你的微博账号
    password = "614469wh. "  # 改成你的微博密码

    a = zjedu_info()
    a.login()  # 登录