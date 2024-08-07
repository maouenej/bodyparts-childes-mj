class ExtractData:
    def __init__(self):
        # list for all the %mor lines to go to
        morphlines = []
        self.morphlines = morphlines

    def getline(self, transcript):
        # for each line in the transcript
        for i in transcript:
            # searching for MOT and CHI lines
            if i.startswith('*MOT') or i.startswith('*CHI'):
                # sending lines to the PrepareData class
                prepareclass = PrepareData()
                #extract = ExtractData()

                # prints each line
                line = print(i)
                # sends each line into the makelineslist function of PrepareData
                prepareclass.makelineslist(line)



    def numline(self, transcript):
        # make a variable to number each line
        counter = 1
        for i in transcript:
            line = print(f"{counter}: {i}")
            #sending lines to the PrepareData class
            prepareclass = PrepareData()
            # sends each line into the makelineslist function of PrepareData
            prepareclass.makelineslist(line)
            # add one to counter to prepare variable for next line
            counter += 1

                #corespondingclass = CorespondingLines()
                #corespondingclass.FindMMlines(line)

    def getmorphlines(self, transcript):
        counter = 1
        for i in transcript:
            if i.startswith('%mor'):
                # setting the line to a variable
                print(f"{counter}: {i}")
                counter += 1

                # sending lines to ExtractData class (so we can access our init)
                # morpharray = ExtractData()

                # add into array for later access
                # morpharray.morphlines += morphline
                # morarray = morpharray.morphlines

                # currently does not work
                # print("This is the array of %mor lines: ", morarray)


class PrepareData:
    def __init__(self):
        # list for all the MOT and CHI lines to go to
        all_lines = []
        self.all_lines = all_lines

    def makelineslist(self, line):
        # putting each line into the all_lines array
        self.all_lines.append(line)
        # sending lines to PrepareData class (so we can send it to another function)
        dataclass = PrepareData()

        # prints each numbered line
        #array = self.all_lines
        for line in self.all_lines:
            print(line)



    # function to link MOT and corresponding mor lines

    # doesnt work correctly !!!!!!!!!!!!!!!!!!!
    def linkmotmor(self, line):
        # list for corresponding lines
        mmlines = []

        # setting parameter to a variable to use python functions
        i = line
        # if the line is a MOT line

        '''
        I tried adding in the if i is not None because without it or after the 
        i.startswith call, you get a NoneType Attribute error message.
        
        It now prints but prints all lines including CHI, which is what we do NOT want.
        '''
        if i.startswith('*MOT'):
        # find the corresponding mor line
            mmlines.append(i)
        if i.startswith(''):
            mmlines.append(i)
        pass

class CategorizeLists:
    def __init__(self):
        # our grand noun and verb lists
        grand_nounls = []
        self.grand_nounls = grand_nounls

        grand_verbls = []
        self.grand_verbsls = grand_verbls

        # grand list for body parts
        grand_bdparts = []
        self.grand_bdparts = grand_bdparts

        # will add other categories here later
    def findbodypart(self, bd_part, sentence):
        # put body parts file in place of amy.copy
        bodyparts = open('./amy.cha copy', 'r')

        i = bd_part
        for i in bodyparts:
            if i in sentence:
                self.grand_bdparts.append(i)
        pass


    def findnouns(self):
        pass

    def findverbs(self):
        pass


if __name__ == "__main__":
    file = open('./amy.cha copy', 'r')
    lineclass = ExtractData()
    # lineclass.getline(file)
    lineclass.numline(file)
    # lineclass.getmorphlines(file)

