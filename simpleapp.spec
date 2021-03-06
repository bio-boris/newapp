/*
A KBase module: simpleapp
*/

module simpleapp {
    /*
        Insert your typespec information here.
    */
    typedef structure {
        int base_number;
        string workspace_name;
    } SimpleParams;

    typedef structure {
        int new_number;
    } SimpleResults;

    funcdef simple_add(SimpleParams params)
        returns (SimpleResults output) authentication required;

    funcdef simple_add_multiprocessing(SimpleParams params)
        returns (SimpleResults output) authentication required;

    funcdef simple_add_with_sleep(SimpleParams params)
        returns (SimpleResults output) authentication required;
    
    funcdef simple_add_with_sleep_client(SimpleParams params)
        returns (SimpleResults output) authentication required;

    funcdef simple_add_hpc_client_group(SimpleParams params)
        returns (SimpleResults output) authentication required;

    funcdef simple_add_hpc_client_group_extra_simple(SimpleParams params)
        returns (SimpleResults output) authentication required;

  funcdef example_method_logs(SimpleParams params)
    returns (SimpleResults output) authentication required;


};
