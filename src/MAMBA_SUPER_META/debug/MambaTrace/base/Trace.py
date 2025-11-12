import sys
# from os.path import isfile, sep as path_sep

from .Frame import MambaFrame

def frame_inspector(**kwargs):
    has_next_frame = lambda tbf: (hasattr(tbf, 'tb_next') and tbf.tb_next!=None)

    e_type, e_instance, exc_info = sys.exc_info()
    current_frame = exc_info
    frames = [MambaFrame(current_frame,**kwargs)]

    while has_next_frame(current_frame):
        current_frame = current_frame.tb_next
        frames.append(MambaFrame(current_frame, **kwargs))

    return frames

class MambaTrace:
    root_exception = None
    exception = ""
    frame_list = []
    multiframe_prefix_str = f"Traceback (most recent call last):\n"
    
    def __init__(self, exc, frame_list=None, colorize_frames=True, skip_frames=0, **kwargs):
        self.root_exception = exc
        self.exception = f"{exc.__class__.__name__}: {exc}"
        if not frame_list:
            self.frame_list = frame_inspector(**kwargs)[skip_frames:]
        else:
            self.frame_list = frame_list[skip_frames:]

    def __str__(self):
        frame_list_str = ''
        for frame in self.frame_list:
            frame_list_str += str(frame)
        return \
            self.multiframe_prefix_str+\
            frame_list_str +'\n'+ str(self.exception)