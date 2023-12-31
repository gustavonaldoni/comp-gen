class LaTeX:
    def __init__(self) -> None:
        self.document = ""

        self._document_class = "article"
        self._title = "Default LaTeX Title"
        self._author = "Default LaTeX Author"
        self._date = r"\today"

    def change_document_class(self, new_document_class: str):
        self._document_class = new_document_class

    def change_title(self, new_title: str):
        self._title = new_title

    def change_author(self, new_author: str):
        self._author = new_author

    def document_class(self):
        self.document += f"\\documentclass{{{self._document_class}}}\n"

    def title(self):
        self.document += f"\\title{{{self._title}}}\n"

    def author(self):
        self.document += f"\\author{{{self._author}}}\n"

    def date(self):
        self.document += f"\\date{{{self._date}}}\n"

    def input(self, arquivo: str):
        self.document += f"\\input{{{arquivo}}}\n"

    def make_title(self):
        self.document += f"\\maketitle\n"

    def new_page(self):
        self.document += f"\\newpage\n"

    def table_of_contents(self):
        self.document += f"\\tableofcontents\n"

    def section(self, section_title: str):
        self.document += f"\\section{{{section_title}}}\n"

    def enumerate(self, items: list):
        command = f"\\begin{{enumerate}}\n"

        for item in items:
            command += f"\\item {item}\n"

        command += f"\\end{{enumerate}}\n"

        self.document += command

    def itemize(self, items: list):
        command = f"\\begin{{itemize}}\n"

        for item in items:
            command += f"\\item {item}\n"

        command += f"\\end{{itemize}}\n"

        self.document += command

    def begin_document(self):
        self.document += f"\\begin{{document}}\n"

    def end_document(self):
        self.document += f"\\end{{document}}\n"
        
    def begin_multicols(self, number_of_columns):
        self.document += f"\\begin{{multicols}}{{{number_of_columns}}}\n"

    def end_multicols(self):
        self.document += f"\\end{{multicols}}\n"

    def save_to_file(self, file_path: str):
        with open(file_path, 'wb') as file:
            file.write(self.document.encode('utf-8'))
