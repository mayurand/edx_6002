'''
Created on Feb 8, 2017

@author: Mayur Andulkar

driver.py takes the input game state for nxn game puzzle.

The input is given as:

python driver.py bfs 3,1,2,0,4,5,6,7,8

    where bfs/dfs/ast/ida are the search algorithms to be used 
    and
    3,1,2,0,4,5,6,7,8 is the state of the game with 0 as null or blank tile 
'''
#===============================================================================
# 
# def runGames(args):
#     
# 
# if __name__ == '__main__':
#     """
#     The main function called when pacman.py is run
#     from the command line:
# 
#     > python pacman.py
# 
#     See the usage string for more details.
# 
#     > python pacman.py --help
#     """
#     args = readCommand( sys.argv[1:] ) # Get game components based on input
#     runGames( **args )
# 
#     # import cProfile
#     # cProfile.run("runGames( **args )")
#     pass
#===============================================================================