class Light:

    on: bool
    
    def __init__(self):
        self.on = False
    
    def __repr__(self) -> str:
        if self.on:
            return "light is on."
        else:
            return "light is off."

    def _bool__(self) -> bool:
        return self.on
    
    def switch(self) -> None:
        self.on = not self.on


if __name__ == "__main__":
    a: Light = Light()
    a.switch()
    if bool(a):
        print(a)
