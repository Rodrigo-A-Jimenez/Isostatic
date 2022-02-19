

class Point:
    def __init__(self, *args, typePoint = 'Point', rotate_degrees = 0, ) -> None:
        self.args = [*args]
        self.typePoint = typePoint
        self.rotate_degrees = rotate_degrees #degrees

    def __str__(self) -> str:
        return (r'{}: {}'.format(self.typePoint, self.args))

    def __repr__(self) -> str:
        return (r'{}: {}'.format(self.typePoint, self.args))

    def __len__(self) -> int:
        return len(self.args)

    def components(self):
        pass
