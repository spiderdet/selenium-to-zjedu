from selenium import webdriver
from time import sleep

def test_default_download():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'D:\\chengxu2\\selenium tests\\data\\'}
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
    driver.get('http://sahitest.com/demo/saveAs.htm')
    two_buttons = driver.find_elements_by_xpath('//a[text()="testsaveas.pdf"]')
    two_buttons[0].click() # http://sahitest.com/demo/testsaveas.pdf    有头模式下：新标签页打开的无法下载
    two_buttons[1].click() # http://sahitest.com/demo/php/download.php  有头模式下：额外弹窗的就可以下载，并且相同文件名不会覆盖而是加(1)来区分
    # 无头模式下，都可下载！
    sleep(3)
    driver.quit()


if __name__ == "__main__":
    test_default_download()