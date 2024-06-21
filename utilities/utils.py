import softest
import logging
import inspect


class Utils(softest.TestCase):
    def assert_list_item_text(self, lists, value):
        for stop in lists:
            print("The text is:" + stop.text)
            self.soft_assert(self.assertEqual,stop.text, value)
            if stop.text == value:
                print("test pass")
            else:
                print("test failed")
        self.assert_all()

    def custom_logger(loglevel = logging.DEBUG):
        # Set class/method name from where its called
        logger_name = inspect.stack()[1][3]
        # Create logger
        # __name__ is added in get logger
        logger = logging.getLogger(logger_name)
        # Level setting
        logger.setLevel(loglevel)
        # Create console handler or file and set the log level
        # Case of file handler and provide the name of file
        fh = logging.FileHandler("automation.log")
        # Create formatter - how you want your logs to be formatted
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s ")
        # add formatter to console or file handler to indicate which format need to be display
        fh.setFormatter(formatter)
        # file case
        logger.addHandler(fh)
        return logger
