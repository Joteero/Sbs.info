## sbs / settings.py

### signature first commit

# тут будут храниться все ссылки и логины для тестов
new_url = "https://task_nimda.ctst.sberins.ru/"
release_url = "https://release_url.sberins.ru/"
stage_url = "https://sber-stage.sbps.ru/"
test_url = "https://sber-test.sbps.ru/"
psi_url = "http://test.sberins.ru/"
if_url = "https://te_sberins.ru/"
email = "arjadiy.parovozov@31rins.ru"
password = "228322"
email_admin = "miss_kate@s3bs.com"
password_admin = "baltika_9"
email_2 = "vladimir.butin@sb3rins.ru"
password_2 = "baltika_0!"

# StaticMethod
def wait_for_ajax(type, _locator, timeout=5):
    """
    Message = "Element %s was not visible in %s second(s)." % (_locator, str(timeout))
    driver = SeleniumWebDriver()
    wait = WebDriverWait(driver, timeout)
    wait.until(EC.element_to_be_clickable(_type, _locator))
    # and driver.execute_script("return $.active") == 0, message=message
```