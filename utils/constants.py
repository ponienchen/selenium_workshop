class WebDriverClientConstant:

    ENABLE_LOGS = True
    LOGS_FOLDER = '../logs'
    CHROME_DRIVER_LOG = f'{LOGS_FOLDER}/chromedriver_log.txt'
    SUPPORTED_BROWSERS = ['chrome']
    TIME_OUT = 5  # in seconds
    SERVICE_ARGS = {
        'chrome': [
            '--verbose',
            f'--log-path={CHROME_DRIVER_LOG}'
        ]
    }
