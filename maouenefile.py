class ExtractData:
    def __init__(self):
        # list for all the %mor lines to go to
        morphlines = []
        self.morphlines = morphlines

    def getline(self, transcript):
        # for each line in the transcript
        for i in transcript:
            # searching for just %mor and %umor lines
            if i.startswith('*MOT') or i.startswith('*CHI'):
                # setting the line to a variable
                # print(i)
                line = i
                # sending lines to the PrepareData class
                prepareclass = PrepareData()
                # sends each line into the numberlines function of PrepareData
                prepareclass.getalllines(line)
                # sends each line into the makearray function of PrepareData
                prepareclass.makearray(line)

    def getmorphlines(self, transcript):
        for i in transcript:
            if i.startswith('%mor'):

                # im thinking here you might need to use nltk, either to tokenize or seperate the
                # lines based on each word

                # setting the line to a variable
                morphline = i
                # sending lines to ExtractData class (so we can access our init)
                morpharray = ExtractData()
                # add into array for later access
                morpharray.morphlines += morphline

                # currently does not work
                print("This is the array of %mor lines: ", morpharray.morphlines)


class PrepareData:
    def __init__(self):
        # list for all the MOT and CHI lines to go to
        all_lines = []
        self.all_lines = all_lines

    def getalllines(self, line):
        # putting each line into the all_lines array
        self.all_lines += line
        # sending lines to PrepareData class (so we can send it to another function)
        dataclass = PrepareData()
        # send array of all lines to numberlines function
        dataclass.numberlines(self.all_lines)

    # these two functions may be swapped

    # numberlines function still needs some work
    def numberlines(self, lines):
        # number lines of MOT and CHI in file
        line_count = 1
        # accessing each line in the array of all lines with MOT and CHI
        for line in lines:
            # place line_count variable at the front of the line
            # append/save line instead of printing
            print(f"{line_count}: {line}")
            # increment line_count by 1 for next line
            line_count += 1

    # need to make an array of each line and save it for later
    def makearray(self, line):
        # here separate words into an array via whitespace
        pass

class CategorizeLists:
    def __init__(self):
        # our grand noun and verb lists
        grand_nounls = []
        self.grand_nounls = grand_nounls

        grand_verbls = []
        self.grand_verbsls = grand_verbls

        # will add other categories here later


if __name__ == "__main__":
    file = open('./amy.cha copy', 'r')
    lineclass = ExtractData()
    # lineclass.getline(file)
    lineclass.getmorphlines(file)

