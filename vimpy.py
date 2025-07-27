# vimpy.py
# simulates a simple Vim-like text editor in Python

class Vimpy:

    _currentfile = None

    def __new__(cls): # Singleton pattern
        if not hasattr(cls, '_instance'):
            cls._instance = super(Vimpy, cls).__new__(cls)
        return cls._instance
    
    def parse_input(self, input_str):
        if Vimpy._currentfile is None:
            tokens = input_str.strip().split()
            if len(tokens) < 2:
                pass
            if tokens[0].lower() == 'pyvim':
                Vimpy._currentfile = open(tokens[1], 'a+', encoding='utf-8')
            else:
                print("Invalid command. Use 'pyvim <filename>' to open a file.")
        else:
            match input_str.strip().split()[0].lower():
                case '%exit':
                    Vimpy._currentfile.close()
                    Vimpy._currentfile = None
                case '%show':
                    Vimpy._currentfile.seek(0)
                    print(20 * '=' + Vimpy._currentfile.name + 20 * '=')
                    print(Vimpy._currentfile.read())
                case '%add':
                    Vimpy._currentfile.write(' '.join(input_str.lstrip().split()[1:]) + '\n')

    def __init__(self):
        try:
            while True:
                self.parse_input(input('>>'))
        except KeyboardInterrupt:
            Vimpy._currentfile.close()
            Vimpy._currentfile = None

if __name__ == "__main__":
    v = Vimpy()

