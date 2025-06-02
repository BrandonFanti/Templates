from mamba_meta.debug.decorators import Protector

class MyModule:
    __version__ = "0.0.1"
    __author__ = "Your Name"

    def __init__(self):
        pass

    def __repr__(self):
        d = {}
        for key,value in self.__dict__.items():
            if not key.startswith("_"): # Exclude private attributes
                d[key] = value
        if d.keys():
            return f"{__class__.__name__}({d})"
        else:
            return f"{__class__.__name__}()"


    def get_version_info() -> str:
        return (
            f"This is {__class__.__name__} class!\n"
            f"From the package: {__package__}\n"
            f"Authored by: {__class__.__author__}\n"
            f"Version: {__class__.__version__}\n"
        )

    @Protector
    def main():
        print(__class__.get_version_info())
        print(f"You can initialize it like this: ")
        print(repr(__class__()))
