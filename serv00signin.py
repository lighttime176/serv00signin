from DrissionPage import Chromium, ChromiumOptions
import logging,os,time
def logging_init():
  # 创建一个logger对象
  logger = logging.getLogger('my_logger')
  logger.setLevel(logging.INFO)  # 设置日志级别为INFO

  # 创建一个控制台处理器，输出到控制台
  console_handler = logging.StreamHandler()
  console_handler.setLevel(logging.INFO)  # 设置控制台日志级别为INFO

  # 创建一个文件处理器，输出到文件
  file_handler = logging.FileHandler('test.log')
  file_handler.setLevel(logging.INFO)  # 设置文件日志级别为INFO

  # 创建一个日志格式化器
  formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
  console_handler.setFormatter(formatter)  # 给控制台处理器设置格式
  file_handler.setFormatter(formatter)  # 给文件处理器设置格式

  # 将控制台和文件处理器添加到logger
  logger.addHandler(console_handler)
  logger.addHandler(file_handler)
  return logger
logger = logging_init()
token = os.environ.get("ydyp")
elements = token.split(',')
for i in range(0, len(elements), 2):
    username = elements[i]
    password = elements[i+1]
    
    co = ChromiumOptions()
    co.incognito()
    # 用该配置创建页面对象
    browser = Chromium(addr_or_opts=co)
    tab = browser.latest_tab
    
    logger.info('打开url')
    tab.get('https://panel14.serv00.com/login/')
    ele = tab.ele('css=#id_username')
    ele.input(username)
    ele = tab.ele('css=#id_password')
    ele.input(password)
    ele = tab.ele('css=#submit')
    ele.click()
    ele = tab.ele('css=#dashboard > div.row.content-row > div:nth-child(1) > div > table > tbody > tr.noborder > td:nth-child(2)')
    logger.info(ele.text)
    time.sleep(10)

    browser.quit()
  



    







