#!/usr/bin/env python3

'''class objects for data points'''

import logging
logger = logging.getLogger(__name__)

class Essay:
    '''
    class for an essay
    '''
    def __init__(self,question,essay,grade=None,info=None):
        self.info = info
        assert isinstance(self.info)

        self.grade = None
        self.question = None
        self.essay = None
        self.tokenize = None
        self.padded = None
        self.vectorize = None # numpy array

    def info(self):
		return self.info