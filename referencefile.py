# this is where we are going to store functions and different
# ways of analyzing the lines together and separately

# stuff we are not currently using but may come back to later

'''
This function separates each %mor line into each character
Each %mor line becomes an array
'''
class RefClass:
    def getmorphlines(self, transcript):
        morphlines = []
        for i in transcript:
            if i.startswith('%mor'):

                # im thinking here you might need to use nltk, either to tokenize or seperate the
                # lines based on each word

                # setting the line to a variable
                morphline = i
                # sending lines to ExtractData class (so we can access our init)
                #morpharray = ExtractData()
                # add into array for later access
                morphlines += morphline

                # currently does not work
                print(morphlines)
    '''     
    def numlinetrash(self, transcript):
        # make a variable to number each line
        counter = 1
        # for each line in the transcript
        for i in transcript:
            # searching for MOT and CHI lines
            if i.startswith('*MOT') or i.startswith('*CHI'):
                #sending lines to the PrepareData class
                prepareclass = PrepareData()

                # prints each line with the leading number
                line = print(f"{counter}: {i}")
                # sends each line into the makelineslist function of PrepareData
                prepareclass.makelineslist(line)
                # add one to counter to prepare variable for next line
                counter += 1

                corespondingclass = CorespondingLines()
                corespondingclass.FindMMlines(line)
    '''

if __name__ == "__main__":
    file = open('./amy.cha copy', 'r')
    lineclass = RefClass()
    lineclass.getmorphlines(file)
