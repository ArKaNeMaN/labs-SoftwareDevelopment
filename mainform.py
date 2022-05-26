from datetime import datetime
from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext
import file_read_utils


def _format_date(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%d-%m-%Y %H:%M:%S')


class MainForm(object):
    _window = Tk()
    _text_field = ''
    _filename = StringVar()

    def __init__(self):
        self._window.title('Получение данных из файла')
        self._window.geometry('500x400')
        self._setup_widgets()
        self._window.mainloop()

    def _setup_widgets(self):
        self._filename.set('*Файл не выбран*')

        Button(self._window, text='Выбрать файл', command=self._select_file).grid(column=0, row=0, columnspan=1)
        Label(self._window, textvariable=self._filename).grid(column=1, row=0, columnspan=4)

        Button(self._window, text='Прочитать матрицу', command=self._read_matrix).grid(column=0, row=1, columnspan=1)
        Button(self._window, text='Прочитать CSV', command=self._read_csv).grid(column=1, row=1, columnspan=1)

        self._text_field = scrolledtext.ScrolledText(
            self._window,
            height=19,
            width=60,
            bg="white",
            fg='black',
            wrap=WORD,
        )
        self._text_field.grid(column=0, row=4, columnspan=5)


    def _select_file(self):
        filetypes = (
            ('Text files', '*.txt'),
            ('CSV files', '*.csv'),
            ('All files', '*.*')
        )

        filename = filedialog.askopenfilename(
            title='Открыть файл',
            initialdir='./',
            filetypes=filetypes
        )

        if filename == '':
            return

        self._filename.set(filename)

    def _print_to_field(self, string):
        self._text_field.delete(0.0, 99999999.0)
        self._text_field.insert(0.0, string)

    def _read_matrix(self):
        filename = self._filename.get()
        if filename[0] == '*':
            self._print_to_field('Файл не выбран!')
            return

        self._print_to_field(file_read_utils.read_matrix(filename))

    def _read_csv(self):
        filename = self._filename.get()
        if filename[0] == '*':
            self._print_to_field('Файл не выбран!')
            return

        self._print_to_field(file_read_utils.read_csv(filename, 0))


if __name__ == '__main__':
    form = MainForm()
