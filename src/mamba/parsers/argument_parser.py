from argparse import RawTextHelpFormatter, Action, ArgumentParser, BooleanOptionalAction
from os import environ as env

from mamba_meta.logging import logger
import logging

class MambaParser(ArgumentParser):
    defaults={
        "debugging":False
    }

    def __init__(self, *k, **kw):
        super().__init__(
            prog=f"{__class__.__name__}",
            description="Generic template",
            epilog=""" ~ A tool created by Brandon Fanti ~""",
            formatter_class=RawTextHelpFormatter,
        )
        self.logger = logger.getLogger()

    def parse_args(self):
        #initialize defaults
        self._set_defaults()
        self._add_default_arguments()

        self.to_be_overridden = True # Prevent warnings/prompts in initialization.
        self.environ_parse() #environ vars are overridden by cli_parse() as a default
        self.cli_parse() 
        self.to_be_overridden = False
        self.action_defaults = None

    def _set_defaults(self):
        defaults = {**__class__.defaults, **self.defaults}
        for key in defaults.keys():
            self.logger.debug(f"Setting self.{key} = {defaults[key]}")
            setattr(self, key, defaults[key])

    def _warn_overloading_non_default_and_configured(self, new_options, option_source="?"):
        defaults = {**__class__.defaults, **self.defaults}
        to_be_overridden = []
        #Iterate current options and CLI arguments
        for key in new_options.keys():
            if hasattr(self, key) and key != getattr(self, key) and key != __class__.defaults[key]:
                to_be_overridden.append((key, new_options[key]))
                if not self.to_be_overridden:
                    self.logger.warn(
                        f"Overriding non-default, previously configured, configuration option:\n"
                        f" (source: {option_source}) '{key}' (Provided: '{new_options[key]}',  "
                        f"default is {defaults[key]})"
                    )

        if not self.to_be_overridden and to_be_overridden != []:
            self.logger.info("Set --to-override (CLI), or to_override=True (Either .env config file, "
                                  "or environment variable) to dismiss these warnings and prompts... "
                                  "alternatively, remove the duplicate")
            if input('Continue with these options? [y/n]: ').upper()[0] == 'N':
                self.logger.info('Exiting...')
                exit()

        for attr,value in to_be_overridden:
            setattr(self, attr, value)

        if not getattr(self, 'debugging', True):
            self.logger.set_level(20) #default log off
        else: self.logger.set_level(10) #Debug on

    #Env, take 3
    def environ_parse(self):
        defaults = {**__class__.defaults, **self.defaults}
        new_options = {}
        for key in defaults.keys():
            if key in env: 
                new_options[key] = env[key]

        self._warn_overloading_non_default_and_configured(new_options, option_source="environment")

    def cli_parse(self):
        new_options = {}
        args = super().parse_args()
        self.logger.debug(args)
        defaults = {**__class__.defaults, **self.defaults}
        #Iterate options 
        for key in vars(args).keys():
            self.logger.debug(f"cli_parse(): Checking {key}")
            if not hasattr(self, key) and getattr(args, key) != defaults[key]:
                self.logger.debug(f"Changing {key} to  {getattr(args, key)}")
                new_options[key] = getattr(args, key)
            else:
                setattr(self, key, getattr(args, key))
                pass

        self._warn_overloading_non_default_and_configured(new_options, option_source="CLI Flag")

    def _add_default_arguments(self):
        if hasattr(self, 'action_defaults'):
            self.logger.debug("Resetting argparser Action defaults")
        defaults = {**__class__.defaults, **self.defaults}
        actions = []

        actions.append(
            self.add_argument(
                "-v",
                "--debugging",
                dest="debugging", action='store_true', default=defaults['debugging'],
                help="Maximize log verbosity"
            )
        )

        self.action_defaults = actions
