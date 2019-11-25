import pickle

class FileIO() :
    def __init__(self, filename):
        self.filename = filename

    def append(self, data) :
        with open(self.filename, mode="a",encoding="utf-8") as f :
            f.write(data+"\n")

    def read(self):
        try :
            with open(self.filename, mode="r",encoding="utf-8") as f:
                a = f.read()
                return a

        except FileNotFoundError :
            raise FileNotFoundError
