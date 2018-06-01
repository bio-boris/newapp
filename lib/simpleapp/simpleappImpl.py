# -*- coding: utf-8 -*-
#BEGIN_HEADER
from DataFileUtil.DataFileUtilClient import DataFileUtil
import os
#END_HEADER


class simpleapp:
    '''
    Module Name:
    simpleapp

    Module Description:
    A KBase module: simpleapp
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = ""

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.dfu = DataFileUtil(self.callback_url)
        #END_CONSTRUCTOR
        pass


    def simple_add(self, ctx, params):
        """
        :param params: instance of type "SimpleParams" (Insert your typespec
           information here.) -> structure: parameter "base_number" of Long,
           parameter "workspace_name" of String
        :returns: instance of type "SimpleResults" -> structure: parameter
           "new_number" of Long
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN simple_add
        input_number = int(params['base_number'])
        input_number += 100
        output =  {'new_number':input_number}
        path= self.dfu.download_web_file(
            {'file_url': "http://kbase.us/wp-content/uploads/2016/09/Kbase_Logo_newWeb.png",
             'download_type': 'Direct Download'}).get(
            'copy_file_path')
        #END simple_add

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method simple_add return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
