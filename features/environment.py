from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from app.application import Application
from support.logger import logger


# def browser_init(context):
def browser_init(context, scenario_name): # (BrowserStack)
    """
    :param context: Behave context
    """
    ### CHROME ###
    # context.driver = webdriver.Chrome()
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    ### FIREFOX ###
    # context.driver = webdriver.Firefox()

    ### HEADLESS MODE ###
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # context.driver = webdriver.Chrome(options=options)

    ### MOBILE WEB TESTING ###
    # # Define mobile emulation
    # mobile_emulation = { "deviceName": "iPhone 12 Pro" }
    #
    # # Chrome options
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("mobileEmulation", mobile_emulation)
    # options.add_argument("--window-size=375,812")  # Optional: Force mobile viewport
    #
    # # Path to ChromeDriver (adjust if needed)
    # driver_path = ChromeDriverManager().install()
    #
    # # Launch browser with mobile emulation
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service, options=options)

    ### MOBILE WEB TESTING - (BrowserStack) ###
    bs_user = 'samirznifeche_bqDQn5'
    bs_key = 'xtapWDEscyrGz8LiCNfy'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
        "deviceName" : "Samsung Galaxy S21 Ultra",
        "osVersion" : "11.0",
        "browserName" : "chrome",
        "deviceOrientation" : "portrait",
        'sessionName': scenario_name,
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user =''
    # bs_key = ''
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     "os" : "OS X",
    #     "osVersion" : "Sequoia",
    #     'browserName': 'Chrome',
    #     'browserVersion': 'latest',
    #     'sessionName': scenario_name,
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    # context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 15)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    logger.info(f'\nStarted scenario: {scenario.name}')
    # browser_init(context)
    browser_init(context, scenario.name) # (BrowserStack)


def before_step(context, step):
    print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        logger.info(f'Step failed: {step}')


def after_scenario(context, feature):
    context.driver.quit()