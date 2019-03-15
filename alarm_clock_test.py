from appium import webdriver

# Launch the Alarms & Clock app
desired_caps = {}
desired_caps["app"] = "Microsoft.WindowsAlarms_8wekyb3d8bbwe!App"
alarm_clock_session = webdriver.Remote(
    command_executor='http://127.0.0.1:4723',
    desired_capabilities= desired_caps)

# Use the session to control the app
alarm_clock_session.find_element_by_accessibility_id("AddAlarmButton").click();
alarm_clock_session.find_element_by_accessibility_id("AlarmNameTextBox").clear();
alarm_clock_session.find_element_by_accessibility_id("AlarmNameTextBox").send_keys("Alarm & Clock Test");

# Take and save screenshot
screenshot = alarm_clock_session.get_screenshot_as_png()
with open(r".\add_alarm.png", "wb") as fout:
    fout.write(screenshot)

alarm_clock_session.find_element_by_accessibility_id("CancelButton").click();

# Quit app
alarm_clock_session.quit()
