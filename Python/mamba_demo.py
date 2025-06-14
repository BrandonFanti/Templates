from mamba_meta.debug.decorators import Protector

def promptly_explode(my_logger):
    my_logger.colorize("Wanna see me explode?", color='red')
    explode = input().upper()
    if explode=='Y':
        raise Exception(f"SHOT?! IN THE BOMB?! '{explode}'")

@Protector
def main(logger=None):
    my_logger = logger.getLogger()
    my_logger.info(f"Hey! I'm new! It's me, `{my_logger.name}()`, you know, from {__name__}!")
    promptly_explode(my_logger)

if __name__ == '__main__': main()