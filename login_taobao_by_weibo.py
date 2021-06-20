from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class taobao_infos:
    def __init__(self):
        url = 'https://login.taobao.com/member/login.jhtml'
        self.url = url
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        options.add_argument(
            'User-Agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"')
        options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})  # 不加载图片,加快访问速度
        options.add_experimental_option('excludeSwitches',
                                        ['enable-automation'])  # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
        self.browser = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
        self.wait = WebDriverWait(self.browser, 5)  # 超时时长为10s

    # 登录淘宝
    def login(self):
        # 打开网页
        self.browser.get(self.url)
        # 等待 密码登录选项 出现
        #(By.CSS_SELECTOR, '.qrcode-login > .login-links > .forget-pwd') 是locator，元组形式，定位元素用的
        #until 意思是直到xx出现就继续运行，until_not相反。
        # 还有 EC.presence_of_all_elements_located等待所有元素加载完毕才通过
        # '.'意思是class，'#'意思是id，如果class名有空格，就需要额外用引号括起来。 >是直接子节点的意思，如果不加>加空格，则是所有子节点里
        # 这些都是在网站上右键检查看到的。
        # '.'后面内容不加引号，class的value中间有空格代表有两个class，所以.X1.X2这么去搜索
        # print(self.browser.find_element_by_css_selector("div[class='login-blocks']").text)
        password_login = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".login-blocks.login-switch-tab > .password-login-tab-item")))
        password_login.click()

        # 等待 微博登录选项 出现
        weibo_login = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.weibo-login')))
        weibo_login.click()

        # 等待 微博账号 出现
        weibo_user = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.inp.username > .W_input')))
        weibo_user.send_keys(weibo_username)

        # 等待 微博密码 出现
        weibo_pwd = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.inp.password > .W_input')))
        weibo_pwd.send_keys(weibo_password)

        # 等待 登录按钮 出现
        submit = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn_tip > a > span')))
        submit.click()

        #其实已经OK了，但是微博开启了登录保护，没办法

        # 直到获取到淘宝会员昵称才能确定是登录成功
        taobao_name = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                      '.site-nav-bd > ul.site-nav-bd-l > li#J_SiteNavLogin > div.site-nav-menu-hd > div.site-nav-user > a.site-nav-login-info-nick ')))
        # 输出淘宝昵称
        print(taobao_name.text)


# 使用教程：
# 1.下载chrome浏览器:https://www.google.com/chrome/
# 2.查看chrome浏览器的版本号，下载对应版本号的chromedriver驱动:http://chromedriver.storage.googleapis.com/index.html
# 3.填写chromedriver的绝对路径
# 4.执行命令pip install selenium
# 5.打开https://account.weibo.com/set/bindsns/bindtaobao并通过微博绑定淘宝账号密码

if __name__ == "__main__":
    chromedriver_path = "/Users/bird/Desktop/chromedriver.exe"  # 改成你的chromedriver的完整路径地址
    weibo_username = "472192957@qq.com"  # 改成你的微博账号
    weibo_password = ""  # 改成你的微博密码

    a = taobao_infos()
    a.login()  # 登录