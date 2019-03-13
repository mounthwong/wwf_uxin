#coding=utf-8
#author='Shichao-Dong'

import time
from appium import webdriver
from selenium.common.exceptions import WebDriverException
import readConfig
import GetDevices
from StartAppiumServer import Sp
from logs import log

log = log()
conf = readConfig.Readconfig()
cmd = GetDevices.devices()


deviceName = cmd.get_deviceName()
platformVersion = cmd.get_platformVersion().encode('ascii')
platformName = conf.getConfigValue('platformName')
appPackage = conf.getConfigValue('appPackage').encode('ascii')
appActivity = conf.getConfigValue('appActivity').encode('ascii')

s = Sp(deviceName)
appium_port = s.main()


def mydriver():
    desired_caps = {
                'platformName':platformName,'deviceName':deviceName, 'platformVersion':platformVersion,
                'appPackage':appPackage,'appActivity':appActivity,
                'unicodeKeyboard':True,'resetKeyboard':True,'noReset':True,
                'newCommandTimeout':180
                }
    caps = {}
    caps["platformName"] = "Android"
    caps["platformVersion"] = "8.0.0"
    caps["deviceName"] = "f8a47de7"
    caps["appPackage"] = "com.meijiale.macyandlarry"
    caps["appActivity"] = ".activity.LauncherActivity"
    caps["app"] = "E:\\APK\\_uxin\\debug\\uxin_trunk-_uxin-debug.apk"
    try:
        driver = webdriver.Remote('http://localhost:4723/wd/hub',caps)
        time.sleep(4)
        log.info('获取driver成功')
        return driver
    except WebDriverException:
        print 'No driver'


if __name__ == "__main__":

    mydriver()