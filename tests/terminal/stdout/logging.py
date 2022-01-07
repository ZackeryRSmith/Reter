import sys
import tty
from typing import (
    AnyStr,
    Iterable
)

class OutputRedirect(object):
    def __init__(self):
        # Clean up this code before using
        self.name = sys.__stdout__.name
        self.mode = sys.__stdout__.mode
        self.errors = sys.__stdout__.errors
        self.encoding = sys.__stdout__.encoding
        self.closed = sys.__stdout__.closed
        self.buffer = sys.__stdout__.buffer
        self.line_buffering = sys.__stdout__.line_buffering
        self.newlines = sys.__stdout__.newlines
        self.cached_buffer = ""

    def write(self, s: AnyStr):
        """
        Just standard out but with a capturing system

        :: IMPORTANT
        : Make sure you add "\\n" to the end of your string, if you don't visual bugs will occur. 
        : I am working on fixing this bug, and no it's not "simple" or else it would be fixed already.
        : Feel free to give it a shot, open a pull request.
        
        :: RECOMENDATION
        : Use print(), it passes through this function and adds a newline character for you. If you MUST use stdout.write() make sure you read
        : the `IMPORTANT` section found above!
        
        :param str s: String to write
        """
        self.cached_buffer += s
        sys.__stdout__.write(str(s))
    
    def writelines(self, lines: Iterable[AnyStr]):
        for line in lines:
            self.cached_buffer += line
        sys.__stdout__.writelines(lines)

    def writable(self) -> bool:
        sys.__stdout__.writable()

    def isatty(self) -> bool:
        sys.__stdout__.isatty()

    def fileno(self) -> int:
        sys.__stdout__.fileno()

    def flush(self):
        sys.__stdout__.flush()


def main():
    outputs = OutputRedirect()

    sys.stdout = outputs
    print("this is a test")
    print("this is another test")
    
    print("\n"+outputs.cached_buffer)

if __name__ == "__main__":
    main()
