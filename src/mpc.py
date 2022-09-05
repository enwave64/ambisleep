from subprocess import Popen, PIPE

def stop_player():
    Popen(["mpc", "stop"])

def start_player(tracknumber):
    print('playing track ', tracknumber)
    Popen(["mpc", "play", tracknumber])

def mpc_setup():
    Popen(["mpc", "repeat", "on"]) #loop playlist
    Popen(["mpc", "single", "on"]) #play single track

#returns a list of tracknames
def construct_playlist():
    cmd = ['mpc', 'playlist']
    #grab the terminal output of this command
    output = Popen(cmd, stdout=PIPE).communicate()[0]
    #get a list of the lines
    tokens = output.decode().split('\n')
    tokens.remove('')

    #for each playlist line, get rid of the rest of the path and the '.mp3'
    for index, token in enumerate(tokens):
        tmp = token.split('/')
        token = tmp[len(tmp) - 1]
        tmp = token.split('.')
        tokens[index] = tmp[0].lower().replace(" ", "")

    return tokens