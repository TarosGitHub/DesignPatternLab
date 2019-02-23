import threading

class Singleton:
    """Singletonパターン
    """
    __instance = None
    __lock = threading.Lock()

    def __new__(cls):
        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = super().__new__(cls)

        return cls.__instance
