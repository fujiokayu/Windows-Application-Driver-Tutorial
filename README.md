# Simple tutorial of Appium on Windows

## Prerequisites

1. Download WinAppDriver from [here](https://github.com/Microsoft/WinAppDriver/releases)
1. pip install [robotframework-appiumlibrary](https://github.com/serhatbolsu/robotframework-appiumlibrary)
1. Run WinAppDriver.exe by administrator mode.  
As follows:
```
"C:\Program Files (x86)\Windows Application Driver\WinAppDriver.exe"
```
You can specify IP and port address by option.
## Implement test case

This is a Alarms & Clock App Sample
1. Import webdriver
```python
from appium import webdriver
```
2. Launch the Alarms & Clock app.  
UWP App can specify by Application ID.  
Classic App need full path.
```python
desired_caps = {}
desired_caps["app"] = "Microsoft.WindowsAlarms_8wekyb3d8bbwe!App"
alarm_clock_session = webdriver.Remote(
    command_executor='http://127.0.0.1:4723',
    desired_capabilities= desired_caps)
```
3. Control the app by Using alarm_clock_session as follows:
```python
alarm_clock_session.find_element_by_accessibility_id("AddAlarmButton").click();
alarm_clock_session.find_element_by_accessibility_id("AlarmNameTextBox").clear();
```
4. Take screenshots as evidence of the test.
```python
screenshot = alarm_clock_session.get_screenshot_as_png()
with open(r"C:\MyTestFolder\add_alarm.png", "wb") as fout:
    fout.write(screenshot)
```
5. Close your app
```python
alarm_clock_session.quit()
```
* * *

This tutorial is provited AS IS and with all faults without warranty or conditions of any kind.
