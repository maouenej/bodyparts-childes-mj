class ExtractData:
    def getline(self, transcript):
        # for each line in the transcript
        for i in transcript:
            # searching for just %mor and %umor lines
            if i.startswith('*MOT') or i.startswith('*CHI') or i.startswith('%mor'):
                # setting result to a variable
                # print(i)
                line = i
                # sending variable to next function
                prepareclass = PrepareData()
                prepareclass.numberlines(line)


class PrepareData:
    # these two functions may be swapped
    def numberlines(self, all_lines):
        # number lines of MOT and CHI in file
        pass

    def makearray(self, line):
        # here separate words into an array via whitespace
        pass

class CategorizeLists:
    def __init__(self):
        # our grand noun and verb lists
        grand_nounls = []
        grand_verbls = []

        # will add other categories here later


if __name__ == "__main__":
    file = open('./amy.cha copy', 'r')
    lineclass = ExtractData()
    lineclass.getline(file)

