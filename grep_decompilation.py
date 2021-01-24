
import idaapi


class expression_finder():
    __func_map = {}
    def __init__(self):
        for func in Functions():
            try:
                cfunc = idaapi.decompile(func)
            except:
                pass
            self.__func_map[func]= cfunc


    def find(self, expression):
        for func in self.__func_map:
            if expression in str(self.__func_map[func]):
                print("Function address :" + hex(func) + " contain expression")





ef = expression_finder()
ef.find("strcpy")

