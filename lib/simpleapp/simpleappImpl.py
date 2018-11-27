# -*- coding: utf-8 -*-
#BEGIN_HEADER
from DataFileUtil.DataFileUtilClient import DataFileUtil
from sleep_job.sleep_jobClient import sleep_job
from .simpleappClient import simpleapp as simpleapp_client

import os
from pathos.multiprocessing import ProcessingPool as Pool

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
    GIT_URL = "https://github.com/bio-boris/newapp.git"
    GIT_COMMIT_HASH = "d6da47ed34ad191a51ec43ea4696ed713be241da"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.dfu = DataFileUtil(self.callback_url)
        self.sj = sleep_job(self.callback_url)
        self.sac = simpleapp_client(self.callback_url)

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
        output = {'new_number': input_number}
        path = self.dfu.download_web_file(
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

    def simple_add_multiprocessing(self, ctx, params):
        """
        :param params: instance of type "SimpleParams" (Insert your typespec
           information here.) -> structure: parameter "base_number" of Long,
           parameter "workspace_name" of String
        :returns: instance of type "SimpleResults" -> structure: parameter
           "new_number" of Long
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN simple_add_multiprocessing

        import random
        random_nums = random.sample(range(1, 1001), 1000)

        cpus = 4
        p = Pool(ncpus=5)
        f = self.sac.simple_add
        params = []

        for number in random_nums:
            params_dict = {'base_number': str(number)}
            params.append(params_dict)

        print(p.map(f, params))

        output = {'new_number': 0}


        #END simple_add_multiprocessing

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method simple_add_multiprocessing return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]

    def simple_add_with_sleep(self, ctx, params):
        """
        :param params: instance of type "SimpleParams" (Insert your typespec
           information here.) -> structure: parameter "base_number" of Long,
           parameter "workspace_name" of String
        :returns: instance of type "SimpleResults" -> structure: parameter
           "new_number" of Long
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN simple_add_with_sleep
        input_number = int(params['base_number'])
        input_number += 100
        output = {'new_number': input_number}
        path = self.dfu.download_web_file(
            {'file_url': "http://kbase.us/wp-content/uploads/2016/09/Kbase_Logo_newWeb.png",
             'download_type': 'Direct Download'}).get(
            'copy_file_path')

        params = {'input_sleep': 120}
        self.sj.simple_sleep(params)

        #END simple_add_with_sleep

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method simple_add_with_sleep return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]

    def simple_add_hpc_client_group(self, ctx, params):
        """
        :param params: instance of type "SimpleParams" (Insert your typespec
           information here.) -> structure: parameter "base_number" of Long,
           parameter "workspace_name" of String
        :returns: instance of type "SimpleResults" -> structure: parameter
           "new_number" of Long
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN simple_add_hpc_client_group
        input_number = int(params['base_number'])
        input_number += 100
        output = {'new_number': input_number}
        path = self.dfu.download_web_file(
            {'file_url': "http://kbase.us/wp-content/uploads/2016/09/Kbase_Logo_newWeb.png",
             'download_type': 'Direct Download'}).get(
            'copy_file_path')
        #END simple_add_hpc_client_group

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method simple_add_hpc_client_group return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]

    def simple_add_hpc_client_group_extra_simple(self, ctx, params):
        """
        :param params: instance of type "SimpleParams" (Insert your typespec
           information here.) -> structure: parameter "base_number" of Long,
           parameter "workspace_name" of String
        :returns: instance of type "SimpleResults" -> structure: parameter
           "new_number" of Long
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN simple_add_hpc_client_group_extra_simple
        input_number = int(params['base_number'])
        input_number += 100
        output = {'new_number': input_number}
        #END simple_add_hpc_client_group_extra_simple

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method simple_add_hpc_client_group_extra_simple return value ' +
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
