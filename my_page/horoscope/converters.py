from datetime import datetime


class DateConverter:
    regex = "^(([1-9]|1[012])[-]([1-9]|[12][0-9]|3[01])[-](19|20)\d\d)|((1[012]|0[1-9])(3[01]|2\d|1\d|0[1-9])(19|20)\d\d)|((1[012]|0[1-9])[-](3[01]|2\d|1\d|0[1-9])[-/.](19|20)\d\d)$"

    def to_python(self, value):
        return datetime.strptime(value, '%d-%m-%Y')

    def to_url(self, value):
        return value.strftime('%d-%m-%Y')


class SplitConverter:
    regex = '(\w+,)+\w+'

    def to_python(self, value):
        return value.split(',')

    def to_url(self, value):
        return ','.join(value)

class UpperConvertor:
    regex = '[^/]+'

    def to_python(self, value):
        return value.upper()

    def to_url(self, value):
        return value.lower()