class Sizes:
    size: int
    euro_size: str
    height: int
    chest_girth: int
    waist_circumference: int
    hip_girth: int

    def __init__(
            self,
            size,
            euro_size,
            height,
            chest_girth,
            waist_circumference,
            hip_girth):
        self.size = size
        self.euro_size = euro_size
        self.height = height
        self.chest_girth = chest_girth
        self.waist_circumference = waist_circumference
        self.hip_girth = hip_girth

    def get_formatted_data(self):
        return f'{self.euro_size} {self.size}-{self.hip_girth}-{self.height}'

    def __eq__(self, other):
        return str(self.size) == str(other)


SIZES = [
    Sizes(size=42, euro_size='XS', height=164, chest_girth=84, waist_circumference=64, hip_girth=90),
    Sizes(size=44, euro_size='S', height=164, chest_girth=88, waist_circumference=68, hip_girth=94),
    Sizes(size=46, euro_size='M', height=170, chest_girth=92, waist_circumference=72, hip_girth=98),
    Sizes(size=48, euro_size='M', height=170, chest_girth=96, waist_circumference=76, hip_girth=102),
    Sizes(size=50, euro_size='L', height=176, chest_girth=100, waist_circumference=80, hip_girth=106),
    Sizes(size=52, euro_size='XL', height=176, chest_girth=104, waist_circumference=84, hip_girth=110),
    Sizes(size=54, euro_size='XL', height=176, chest_girth=108, waist_circumference=88, hip_girth=114),
]

SIZES_DICT = {
    str(size.size): size for size in SIZES
}

SIZES_CHOICES = (
    [size.size, f'{size.euro_size} {size.euro_size}-{size.hip_girth}-{size.height}'] for size in SIZES
)
