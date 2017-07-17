'''
boostsrl-mini: a barebones version of BoostSRL implemented in Python2.7 and Python3
'''

import argparse
import os

# Define a short class for raising exceptions to help with debugging.

class ExceptionCase(Exception):
    def handle(self):
        print(self.message)

# Setup: parse the commandline input, perform checks, and import/parse the specified files.

class Setup:
    
    def __init__(self):
        
        self.learn = False                # -l, --learn
        self.infer = False                # -i, --infer
        self.verbose = False              # -v, --verbose
        self.trainpath = 'train/'         # -train [PATH]
        self.testpath = 'test/'           # -test [PATH]
        self.modelspath = 'train/models/' # -models [PATH]
        self.aucjarpath = '.'             # -aucJarPath [PATH]
        self.trees = 10                   # -trees [NUMBER]
        self.database = None              # -database server
        
        # Start by creating an argument parser to help with user input.
        parser = argparse.ArgumentParser(description="boostsrl-mini: a barebones version of BoostSRL implemented in Python3."\
                                         " Written by: Alexander L. Hayes and Kaushik Roy",
                                         epilog="Copyright 2017 Free Software Foundation, Inc."\
                                         " License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>."\
                                         " This is free software: you are free to change and redistribute it."\
                                         " There is NO WARRANTY, to the extent permitted by law.")
        # Add the arguments.
        learninginference = parser.add_mutually_exclusive_group()
        #parser.add_argument("diagram_file")
        learninginference.add_argument("-l", "--learn",
                                       help="Learn a model for training data.",
                                       action="store_true")
        learninginference.add_argument("-i", "--infer",
                                       help="Perform inference for test data.",
                                       action="store_true")
        parser.add_argument("-v", "--verbose",
                            help="Increase verbosity to help with debugging.", 
                            action="store_true")
        parser.add_argument("-trees",
                            type=int,
                            help="[Default: 10]. Choose the number of trees to use during learning or inference. If 10 trees are learned during training, any number of trees from 1 to 10 can be specified during inference.")
        parser.add_argument("-train",
                            type=str,
                            help="[Default: train/]. Specify the path to the training data. Naming convention will be: train_pos.txt, train_neg.txt, train_facts.txt")
        
        # Get the args.
        args = parser.parse_args()
        print(args)
        exit()

        # Make sure the diagram_file is valid.
        if not os.path.isfile(args.diagram_file):
            raise ExceptionCase('Error [1]: Could not find file: "' + args.diagram_file + '"')

        # Import the file:
        '''Reads the contents of 'file_to_read', raises an exception if it cannot be read.'''
        try:
            diagram = open(args.diagram_file).read()
        except:
            raise ExceptionCase('Error [1]: Could not read the file: "' + args.diagram_file + '"')

        if (len(diagram.splitlines()) == 6):
            self.diagram_file = diagram
        else:
            raise ExceptionCase('Error [1]: File opened successfully, but has the wrong number of lines.')
            
        # Since the files exist, we can go ahead and set the rest of the parameters, starting with verbose
        self.verbose = args.verbose
        
        if (args.number != None):
            if (args.number >= 0):
                self.Nfeatures = args.number
            else:
                raise(ExceptionCase('Error [1]: Cannot have negative features.'))

        # Check the rest of the parameters, update if necessary.
        if not (args.walk or args.nowalk or args.exhaustive or args.random or args.shortest or args.randomwalk):
            # If this occurs, no flags were specified, so keep defaults (default: self.walk=True).
            print('[Default] "Walk Mode": Walk graph from target to features.')
            pass
        else:
            self.nowalk = args.nowalk
            self.walk = args.walk
            self.shortest = args.shortest
            self.exhaustive = args.exhaustive
            self.random = args.random
            self.randomwalk = args.randomwalk

        if self.verbose:
            print('Imported Diagram File:\n')
            print(diagram)

class UnitTests:

    def __init__(self):
        pass

    def test_file_exists(self, file_to_test):
        if not os.path.isfile(file_to_test):
            raise ExceptionCase('Error [2]: Could not find file: "' + args.diagram_file + '"')

    def run_unit_tests(self):
        pass

class CmdInteraction:
    
    def __init__(self):
        pass
        
    def targetFeatureSelector(self):
        pass

class FileWriter:
    
    def __init__(self):
        pass

    def write_modes_to_file(self):
        pass

if __name__ == '__main__':

    '''Parse the commandline input, import the file. Contents are stored in setup.diagram_file.'''
    setup = Setup()
