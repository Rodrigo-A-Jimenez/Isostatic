

class Point:
    def __init__(self, *args) -> None:
        self.args = args

    def __str__(self) -> str:
        return ("Point: "+ str(self.args))