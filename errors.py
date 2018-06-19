class NumberRequiredException:
    __NUMBER_REQUIRED = '[ERROR 00] Number required\n\n'

    def __init__(self):
        print(self.__NUMBER_REQUIRED)
        exit()


class InvalidCodeException:
    __INVALID_CODE = '[ERROR 01] Invalid Code\n\n'

    def __init__(self):
        print(self.__INVALID_CODE)
        exit()