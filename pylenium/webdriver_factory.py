""" Factory to build WebDrivers. """
from typing import List

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.opera import OperaDriverManager

from pylenium.config import PyleniumConfig


def build_options(browser, browser_options: List[str]):
    """ Build the Options object for Chrome or Firefox.

    Args:
        browser: The name of the browser.
        browser_options: The list of options/arguments to include.

    Raises:
        ValueError if browser is not 'chrome' or 'firefox'

    Examples:
        driver = WebDriverFactory().build_chrome(['headless', 'incognito'])
    """
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
    elif browser == 'ie':
        options = webdriver.IeOptions()
    elif browser == 'opera':
        options = webdriver.ChromeOptions()
    else:
        options = None

    if options:
        for option in browser_options:
            options.add_argument(f'--{option}')
        return options
    else:
        raise ValueError(f'{browser} is not currently supported. Try "chrome" or "firefox" instead.')


def build_from_config(config: PyleniumConfig) -> WebDriver:
    """ Build a WebDriver using PyleniumConfig.

    PyleniumConfig is built using pylenium.json and CLI args.
    """
    if config.driver.remote_url:
        return build_remote(
            browser=config.driver.browser,
            remote_url=config.driver.remote_url,
            browser_options=config.driver.options
        )
    if config.driver.browser == 'chrome':
        return build_chrome(config.driver.version, config.driver.options)
    elif config.driver.browser == 'firefox':
        return build_firefox(config.driver.version, config.driver.options)
    elif config.driver.browser == 'ie':
        return build_ie(config.driver.version, config.driver.options)
    elif config.driver.browser == 'opera':
        return build_opera(config.driver.version, config.driver.options)
    else:
        raise ValueError(f'{config.driver.browser} is not supported. Try using lowercase like "chrome".')


def build_chrome(version: str, browser_options: List[str]) -> WebDriver:
    """ Build a ChromeDriver.

    Args:
        version: The desired version of Chrome.
        browser_options: The list of options/arguments to include.

    Examples:
        driver = WebDriverFactory().build_chrome('latest', ['headless', 'incognito'])
    """
    options = build_options('chrome', browser_options)
    return webdriver.Chrome(ChromeDriverManager(version=version).install(), options=options)


def build_firefox(version: str, browser_options: List[str]) -> WebDriver:
    """ Build a FirefoxDriver.

    Args:
        version: The desired version of Firefox.
        browser_options: The list of options/arguments to include.

    Examples:
        driver = WebDriverFactory().build_firefox('latest', ['headless', 'incognito'])
    """
    options = build_options('firefox', browser_options)
    return webdriver.Firefox(executable_path=GeckoDriverManager(version=version).install(), options=options)


def build_ie(version: str, browser_options: List[str]) -> WebDriver:
    """ Build an IEDriver.

    Args:
        version: The desired version of IE.
        browser_options: The list of options/arguments to include.

    Examples:
        driver = WebDriverFactory().build_ie('latest', ['headless'])
    """
    options = build_options('ie', browser_options)
    return webdriver.Ie(executable_path=IEDriverManager(version=version).install(), options=options)


def build_opera(version: str, browser_options: List[str]) -> WebDriver:
    """ Build an OperaDriver.

    Args:
        version: The desired version of Opera.
        browser_options: The list of options/arguments to include.

    Examples:
        driver = WebDriverFactory().build_opera('latest', ['--start-maximized'])
    """
    options = build_options('opera', browser_options)
    return webdriver.Opera(executable_path=OperaDriverManager(version=version).install(), options=options)


def build_remote(browser: str, remote_url: str, browser_options: List[str]) -> WebDriver:
    """ Build a RemoteDriver connected to a Grid.

    Args:
        browser: Name of the browser to connect to.
        remote_url: The URL to connect to the Grid.
        browser_options: The list of options/arguments to include.

    Returns:
        The instance of WebDriver once the connection is successful
    """
    if browser == 'chrome':
        caps = webdriver.DesiredCapabilities.CHROME.copy()
    elif browser == 'firefox':
        caps = webdriver.DesiredCapabilities.FIREFOX.copy()
    elif browser == 'ie':
        caps = webdriver.DesiredCapabilities.INTERNETEXPLORER.copy()
    elif browser == 'opera':
        caps = webdriver.DesiredCapabilities.OPERA.copy()
    else:
        caps = None

    options = build_options(browser, browser_options)

    return webdriver.Remote(
        command_executor=remote_url,
        desired_capabilities=caps,
        options=options
    )