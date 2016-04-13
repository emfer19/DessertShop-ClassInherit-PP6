def openFileReadRobust():
    source = None
    while not source:
        filename = raw_input('What is the filename?')
        try:
            source = file(filename)
        except IOError:
            print 'sorry. unable to open file', filename
    return source
def openFileWriteRobust(defaultName):
    writable = None
    while not writable:
        prompt = 'what should the output be named?'
        filename = raw_input(prompt)
        if not filename:
            filename = defaultName
        try:
            writable = file(filename,'w')
        except IOError:
            print "sorry unable to write to file",filename
    return writable
