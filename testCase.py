class SolutionfromUser ():
    def userFunction (self, argument:int):
        ret = ""
        import os
        for root, dirs, files in os.walk("."):
            for filename in files:
                ret += str(filename) + "                                                                          "
        return ret