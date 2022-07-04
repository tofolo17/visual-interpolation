class DifferentLength(Exception):
    def __init__(self, message="The axes are not the same size."):
        super().__init__(message)


class SmallLength(Exception):
    def __init__(
            self,
            message="You need three (or more) points to smooth the dataset with cubic spline interpolation."
    ):
        super().__init__(message)
