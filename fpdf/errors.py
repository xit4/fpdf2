# -*- coding: latin-1 -*-

"""FPDF Error classes"""

# this module is unwriteable without tests

def fpdf_error(message):
    raise RuntimeError('FPDF error: ' + message)

def argument_representation(inputs):
  return ', '.join(list(map(lambda x: repr(x), inputs)))

class FPDFException(Exception):
    pass

class FPDFPageFormatException(FPDFException):
    """Error is thrown when a bad page format is given"""
    def __init__(self, argument, unknown=False, one=False):
        super(FPDFPageFormatException, self).__init__()

        if unknown and one:
            raise TypeError('FPDF Page Format Exception cannot be both for '
                            'unknown type and for wrong number of arguments')

        self.argument = argument
        self.unknown = unknown
        self.one = one

    def _f(self, message):
        return 'FPDFPageFormatException: ' + message

    def format_unknown(self, argument):
        return self._f("Unknown page format: " + argument)

    def format_one(self, a):
        return self._f('Only one argument given: %s. Need (height,width)' % a)

    def __repr__(self):
        inputs = [self.argument, self.unknown, self.one]
        arguments = argument_representation(inputs)
        return ''.join(['FPDFPageFormatException(', arguments, ')'])

    def __str__(self):
        if self.unknown:
            return self.format_unknown(self.argument)
        elif self.one:
            return self.format_one(self.argument)
        else:
            return self._f(self.argument)

class FPDFUndefinedFontException(FPDFException):
    """Error is thrown when set_font called on font which is not added"""
    def __init__(self, family, style):
        super(FPDFUndefinedFontException, self).__init__()
        self.family = family
        self.style = style

    def __repr__(self):
        arguments = argument_representation([self.family, self.style])
        return 'FPDFUndefinedFontException({})'.format(arguments)

    def __str__(self):
        style = ' ' + self.style if self.style and len(self.style) else ''
        return 'Undefined font: {}{}'.format(self.family, style)
    