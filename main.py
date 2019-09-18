import sys, logging, json

#check to make sure we are running the right version of Python
version = (3,7)
assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0],version[1])

#turn on logging, in case we have to leave ourselves debugging messages
logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)


def render():
    """In front of a red barn with a white door"""
    return True
def checkinput():
    """Request information from player"""
    user_input=input("what would you like to do?")  

def main():
    game = {}
    with open('zork.json') as json_file:

        game = json.load(json_file)
def update (world, current, selection):
    game[current]["exits"]
    for e in game[room][current]["exits"]:
  if e["verb"]== selection:
    current= e["target"]
    # Your game goes here!
                    "v": "Q",
                    "map": "QUIT"
                },
                 "v": "WALK"
                 "map":"QUIT"
                 }
                 {
                  "v": "GO INSIDE BARN",
                  "map": "QUIT"
                 },
                 {
                  "v": "LOOK AT ANIMALS"
                  "map": "SOUTH"
                 },
                 {
                  "v": "FEED HORSES",
                  "map": "SOUTH"
                 }
                 {
                  "v": "Found Saddle"
                  "map": "SOUTH"
                 }
                 {
                  "v": "PUT SADDLE ON HORSE"
                  "map": "PUT SADDLE DOWN"
                 }
                 {
                  "v": "GO RIDING
                  "MAP": "STOP HORSE"
                 },
                 {
                   "v":"RATTLESNAKE IN PATH"
                   "map":" RUN FROM RATTLESNAKE"
                 },

                 {
                  "v": "Q"
                  "map": "QUIT"
                 },
                 {
                  "v": "STOP HORSE"
                  "map": "STEP OFF HORSE"
                 },
                 {
                  "v": "BUILD FIRE"
                  "map": "STOP FIRE"
                 },
                 {
                 "v": "BUILD TENT"
                 "map": "DROP TENT"
                 },
                 {
                 "v": "LOOK AROUND"
                 "map": "STOP"
                 },
                 {
                  "v": "GATHER PLANTS"
                  "map":"PICK UP MAP"
                 },
                 {
                  "v": "EAT FOOD"
                 "map": "STOP EATING"
                 },


                 
                




















    current = 'WHOUS'


quit=False
while not quit:
    #render the world
    render(game["rooms"],current)
    #check for player input

#if we are running this from the command line, run main
if __name__ == '__main__':
	main()
