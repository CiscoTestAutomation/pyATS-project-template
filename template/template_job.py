#*******************************************************************************
#*                           Easypy Job File Template
#* ----------------------------------------------------------------------------
#* ABOUT THIS TEMPLATE - Please read
#*
#* - Any comments with "#*" in front of them (like this entire comment box) are
#*   for template clarifications only and should be removed from the final
#*   product.
#*
#* - Anything enclosed in <> must be replaced by the appropriate text for your
#*   application
#*
#* Author:
#*    Siming Yuan, Cisco Systems Inc.
#*
#* Support:
#*    pyats-support-ext@cisco.com
#*
#* Read More:
#*   For the complete and up-to-date user guide on pyATS, visit:
#*   https://pyats.dev/
#*
#*******************************************************************************

'''template_job.py

This is an example docstring for an a job file. The header should describe which
scripts are included as part of this job, their required topology, and any other
information which may concern the person that runs this job.

Purpose:
    < State Purpose Here >

Usage:
    bash$ pyats run job template_job.py

Description:
    < descriptiveText >

Requirements:
    - < yourRequirements >

Noes:
    <something>

'''

#
# optional author information
#
__author__ = 'Cisco Systems Inc.'
__copyright__ = 'Copyright (c) 2017, Cisco Systems Inc.'
__contact__ = ['pyats-support@cisco.com', 'pyats-support-ext@cisco.com']
__date__= 'June 15, 2015'
__version__ = 2.0

#
# import block
#
import os
import logging
import argparse

from pyats.easypy import run

# import logic statements from datastructures module
from pyats.datastructures.logic import And, Or, Not

#*******************************************************************************
#* PARSING COMMAND LINE ARGUMENTS
#*
#*  pyATS features argument propagation: propagating custom command
#*  line arguments to jobfile & the testscript. In a nutshell, the requirement
#*  is simple: parse only what you need using parse_known_args(), leave the 
#*  rest in sys.argv.
#*
#*  If your jobfile requires additional command line arguments, you'll need to
#*  create an argparse section here. 
#*
#*  note - argparse modules are already imported for your convenience above.
#*
#*******************************************************************************

#
# create your custom job file argument parser here
#
parser = argparse.ArgumentParser(description='example job file cli args parser')
parser.add_argument('--argument_a',
                    help='example argument a',
                    default = None)
parser.add_argument('--argument_b',
                    help='example argument b',
                    default = None)

#*******************************************************************************
#* MAIN FUNCTION
#*
#*  Each job file must have a main() function where testscripts/task runs are
#*  defined. After a job file is imported, pyATS will lookup main() function
#*  to run. 
#*
#*  main() funtion shall have a single argument called 'runtime'. This allows
#*  the engine to automatically pass in the current runtime object. The
#*  following should be performed within the main() function:
#*      - parse any custom command-line arguments
#*      - configure logger log-levels, if any
#*      - run each and every testscript file
#*
#*  Examples
#*  --------
#*      
#*      def main(runtime):
#*
#*          # do parse command line job file arguments
#*          args = parser.parse_known_args()
#*
#*          # configure some loggers
#*          logging.getLogger('pyats.aetest').setLevel('DEBUG')
#*          logging.getLogger('mymodule.myfeature').setLevel('INFO')
#*
#*          # simple run
#*          run(testscript = "/path/to/my/script.py", runtime = runtime)
#*
#*          # specify a custom task id
#*          run(testscript = "/path/to/my/script.py",
#*              task_id = "custom_task_id",
#*              runtime = runtime)
#*
#*          # passing script arguments from job file to script
#*          run(testscript = "/path/to/my/script.py",
#*              task_id = "custom_task_id",
#*              runtime = runtime,
#*              script_arg_1 = 'some value 1',
#*              script_arg_2 = 'some value 2',
#*              script_arg_x = 'some value X')
#*
#*          # calling with AEtest options
#*          run(testscript = "/path/to/my/script.py",
#*              submitter = 'chambers',
#*              runtime = runtime)
#*
#*          # making life complicated
#*          run(testscript = "/path/to/my/script.py",
#*              runtime = runtime,
#*              task_id = "custom_task_id",
#*              script_arg_1 = 'some value 1',
#*              script_arg_2 = 'some value 2',
#*              script_arg_x = args.myargument,
#*              submitter = 'chambers')
#*
#*  for detailed jobfile description, visit:
#*  https://pubhub.devnetcloud.com/media/pyats/docs/easypy/jobfile.html
#*
#*******************************************************************************

# compute the script path from this location
script_path = os.path.dirname(__file__)

# 
# main logic, run testscripts inside
#
def main(runtime):
    
    # parse custom command-line arguments
    custom_args = parser.parse_known_args()[0]
 
    #**************************************
    #* Log Levels
    #*
    #*  within the job file main() section, you can set the various logger's
    #*  loglevels for your following testscripts. This allows users to modify
    #*  the logging output within the job file, for various modules & etc,
    #*  without modifying testscript and libraries.

    # set log levels for various modules
    # eg, set aetest to INFO, set your library to DEBUG
    logging.getLogger('pyats.aetest').setLevel('INFO')
    logging.getLogger('libs').setLevel('DEBUG')
    

    #***************************************************************************
    #* SCRIPT ARGUMENTS
    #*
    #*  Aside from standard run() and infrastructure arguments, all other 
    #*  keyword arguments (*kwargs) to run() api are effectively script
    #*  parameters.
    #***************************************************************************
    #
    # run the template script
    # 
    run(testscript= os.path.join(script_path, 'template_script.py'),
        runtime = runtime,
        script_arg_one = 'value',
        script_arg_two = 'value')