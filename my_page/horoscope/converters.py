from datetime import datetime


class DateConverter:
    regex = "^(([1-9]|1[012])[-]([1-9]|[12][0-9]|3[01])[-](19|20)\d\d)|((1[012]|0[1-9])(3[01]|2\d|1\d|0[1-9])(19|20)\d\d)|((1[012]|0[1-9])[-](3[01]|2\d|1\d|0[1-9])[-/.](19|20)\d\d)$"

    def to_python(self, value):
        return datetime.strptime(value, '%m-%d-%Y').strftime('%m-%d-%Y')

    def to_url(self, value):
        return value.strftime('%m-%d-%Y')