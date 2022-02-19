

class Point:
    def __init__(self, *args) -> None:
        self.args = [*args]

    def __str__(self) -> str:
        return (r'Point: {}'.format(self.args))

    def __repr__(self) -> str:
        return (r'Point: {}'.format(self.args))

    def __len__(self) -> int:
        return len(self.args)