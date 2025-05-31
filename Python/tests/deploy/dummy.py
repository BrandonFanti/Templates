from mamba_meta.debug.decorators import protector

def promptly_exlode(my_logger):
    my_logger.colorize("Wanna see me explode?", color='red')
    explode = input().upper()

    if explode=='Y':
        raise Exception("SHOT?! IN THE BOMB?!")

@protector
def main(logger=None):
    my_logger = logger.getLogger()
    my_logger.info(f"Hey! I'm new! It's me, {logger.name}, from {__name__}!")
    promptly_exlode()

if __name__ == '__main__':
    main()