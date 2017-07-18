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
    
    def parse_command_line_arguments(self):

        # Start by creating an argument parser to help with user input.
        parser = argparse.ArgumentParser(description="boostsrl-mini: a barebones version of BoostSRL implemented in Python3."\
                                         " Written by: Kaushik Roy and Alexander L. Hayes",
                                         epilog="Copyright 2017 Free Software Foundation, Inc."\
                                         " License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>."\
                                         " This is free software: you are free to change and redistribute it."\
                                         " There is NO WARRANTY, to the extent permitted by law.")
        # Add the arguments.
        learninginference = parser.add_mutually_exclusive_group()

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
        
        if not ((args.infer) or (args.learn)):
            raise ExceptionCase('Must either learn or infer.')

        print('value of args.learn is: ' + str(args.learn))
        print('value of args.infer is: ' + str(args.infer))

        tests = UnitTests()
        tests.test_file_exists('background.txt')
        
        '''
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
        '''

class UnitTests:

    def __init__(self):
        pass

    def test_file_exists(self, file_to_test):
        if setup.verbose:
            print('Checking for ' + file_to_test)
        if not os.path.isfile(file_to_test):
            raise ExceptionCase('Error [2]: Could not find file: "' + file_to_test + '"')
        
    def test_directory_exists(self, dir_to_test):
        pass

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
    args = setup.parse_command_line_arguments()
