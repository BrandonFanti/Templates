from ...logging import logger, color

from . import MambaTrace, MambaFrame


#Adds color!
class ColoredMambaFrame(MambaFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def colorize(self):
        self.factory_colorize()

    @staticmethod
    def factory_colorize(frame:MambaFrame, magic=True):
        attr_to_color_info = [
            'line_prefixed__pre_faulting_lines',
            'line_prefixed__post_faulting_lines',
            'pre_faulting_lines',
            'post_faulting_lines',
        ]
        attr_to_color_fail = [
            'line_prefixed_faulty_line'
        ]
        attr_to_color_magic = ['problem_vars_str']

        def apply_color(attr_list, color):
            for attr in attr_list:
                msg  = getattr(frame, attr)
                nmsg = logger.format_color(msg, color)
                setattr(frame, attr, nmsg)

        def apply_effect(attr_list):
            for attr in attr_list:
                msg  = getattr(frame, attr)
                nmsg = logger.format_effect(msg)
                setattr(frame, attr, nmsg)

        apply_color(['frame_prefix',], 'GREEN')
        apply_color(attr_to_color_info, 'BLUE')
        apply_color(attr_to_color_fail, 'RED')
        apply_color(attr_to_color_magic,'PURPLE')
        if magic: apply_effect(attr_to_color_magic)

        return frame

class ColoredMambaTrace(MambaTrace):

    def __init__(self, *args, magic=True, **kwargs):
        super().__init__(*args, **kwargs)
        self.frame_list =\
            [ColoredMambaFrame.factory_colorize(f, magic=magic) for f in self.frame_list]
        self.multiframe_prefix_str =\
            logger.format_color(self.multiframe_prefix_str, 'blue')
        self.exception =\
            logger.format_color(self.exception, 'red')

if __name__ == '__main__':
    frame = None
    if frame:
        print(self)
        print("Sample:")
        sample = self.frame_list[0].faulty_line
        print(sample,end='')
        print("as")
        print(logger.format_color(sample),end='')
        print("... or")
        magic_sample = logger.format_effect(sample)
        magic_sample = logger.format_color(magic_sample, color='PURPLE')
        print(magic_sample,end='')
        print("Now, Applying color...")
    else:
        print("Sorry! Author broke this sample")