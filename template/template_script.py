#*******************************************************************************
#*                           Test Script Template
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

'''template.py

< describe your testscript >

Topology:
    <describe and/or draw your topology here>

Arguments:
    <name> (<type>): <description of your testscript argument>

Examples:
    < provide examples on how to use this test script. >

References:
    < provide references here. >

Notes:
    < provide notes if needed >

'''

# optional author information
__author__ = 'Cisco Systems Inc.'
__copyright__ = 'Copyright (c) 2019, Cisco Systems Inc.'
__contact__ = ['pyats-support-ext@cisco.com']
__credits__ = []
__date__= 'March 16, 2019'
__version__ = 2.0

# imports statements
import logging

from pyats import aetest

logger = logging.getLogger(__name__)

#*******************************************************************************
#* TESTSCRIPT PARAMETERS
#*
#*  testscripts are driven by data. These data are called 'parameters' within
#*   scripts. Parameters follows a predefined inheritance rule:
#*      - child section parameters inherits parent section parameters.
#*
#*  this relationship can be charted as (<- denoting parent of):
#*
#*      TestScript <- CommonSetup   <- Subsections
#*           \---- <- Testcase      <- Setup/Test/Cleanup
#*            `--- <- CommonCleanup <- Subsections
#*
#*  or, in set theory, using TestScript/CommonSetup/Subsection as example:
#*          +----------------------------------------------+
#*          | +-----------------------------+  Subsections |
#*          | | +------------+  CommonSetup |   parameters |
#*          | | | TestScript |   parameters |              |
#*          | | | parameters |              |              |
#*          | | +------------+              |              |
#*          | +-----------------------------+              |
#*          +----------------------------------------------+
#*
#*  to define TestScript parameter defaults, create a dictionary named
#* 'parameters' directly within your testscript.
#*      parameters = {
#*          <keys>: <values>,
#*      }
#*
#*  if this testscript was called with script arguments (provided in job file),
#*  these script arguments are updated into this TestScript parameter
#*  dictionary (overwriting any conflicting ones).
#*
#* Read More:
#*    https://pubhub.devnetcloud.com/media/pyats/docs/aetest/parameters.html
#*******************************************************************************

#
# testscript default parameters
#
parameters = {
    '<name>': '<value>',
}

#*******************************************************************************
#* COMMON SETUP SECTION
#*
#*  use common setup section to configure and perform the initial setup of your
#*  testscript environment. All common configurations & etc shared among your
#*  script testcases shall be configured here.
#*
#*  Example:
#*    - check that all required parameters/script arguments are provided
#*    - verify the required topology is present.
#*    - connect to all testbed devices
#*    - check that all configured devices are ready to go
#*    - if there is any failure encountered at this stage, block testcases from
#*      further execution and exit gracefully
#*    - After the mandated checks pass, apply base configuration that is
#*      applicable for the following testcases
#*
#*  https://pubhub.devnetcloud.com/media/pyats/docs/aetest/structure.html#common-setup
class CommonSetup(aetest.CommonSetup):
    '''Common Setup Section

    < common setup docstring >

    Subsections:
        < list the # of subsections and their intentions >

        < subsection > : < descriptions >
    '''

    #******************************
    #* subsection: check parameters
    #*
    #*  suggested subsection. use this subsection to check that your script's
    #*  required arguments & parameters are indeed provided to the testscript.
    @aetest.subsection
    def check_parameters(self, **parameters):
        '''Checking Parameters

        < docstring >

        Arguments:
            < list the mandatory arguments/parameters verified by this script >
        '''

        mandatory_parameters = [
            'testbed',
            #* < and any other mandatory parameters >
        ]
        for parameter in mandatory_parameters:
            assert parameter in parameters, "missing mandated parameter '%s'" \
                                            % parameter

    #******************************
    #* subsection: validate topology
    #*
    #*  suggested subsection. use this subsection to verify that the provided
    #*  topology, links & devices are present.
    @aetest.subsection
    def validate_topology(self, testbed, **parameters):
        '''Validating Topology

        < docstring >
        '''

        # skip this subsection if no testbed was provided
        assert testbed, 'Testbed was not provided'

        # verify all routers exists
        if 'routers' in parameters:
            for rtr in parameters['routers']:
                assert rtr in testbed, 'testbed missing router: %s' % rtr

        # convert labels to devices
        if 'labels' in parameters:
            for label, hostname in parameters['labels'].items():
                parameters['labels'][label] = testbed.devices[hostname]

        # validate links are all there
        if 'links' in parameters:
            link_names = [link.name for link in testbed.links]

            for link in parameters['links']:
                assert link in link_names, "Link missing: %s"  % link

        # etc.

    #******************************
    #* subsection: connect to devices
    #*
    #*  suggested subsection. use this subsection to connect to your testbed
    #*  devices and verify connection is up
    @aetest.subsection
    def connect_to_devices(self, testbed):
        '''Connect to Devices

        < docstring >
        '''

        testbed.connect()

    #******************************
    #* subsection: configure_interfaces
    #*
    #*  configure your device interfaces
    @aetest.subsection
    def configure_interfaces(self, testbed):
        '''Configure Device Interfaces

        < docstring >
        '''

        #***********************************************************************
        #* Dynamic IP Address Generation
        #*
        #*  It is strongly suggested that device interface IP addresses be
        #*  dynamically generated as part of the common setup section. This can
        #*  be easily accomplished using Python 'ipaddress' module.
        #*
        #*  store the generated ip addresses information into interface object's
        #*  'ipv4' and 'ipv6' attributes. Note that the stored values should
        #*  be ipaddress.IPv4Address and ipaddress.IPv6Address objects instead
        #*  of string values.
        #*
        #*  Refer to ipaddress module for more information
        #*      https://docs.python.org/3/library/ipaddress.html
        #***********************************************************************

        #* < configure device interface code >
        #*
        #*  eg:
        #*      for device in testbed:
        #*          for interface in device:
        #*              device.configure(...)

    #******************************
    #* subsection: configure_tgen
    #*
    #*  configure your traffic generators, if any
    @aetest.subsection
    def configure_tgen(self, **parameters):
        '''Configure Traffic Generators

        < docstring >
        '''

        if 'tgns' in parameters:
            #* < configure tegn code >
            #*
            #*  eg:
            #*      for tgn in parameters['tgen']:
            #*          ...
            pass

    #******************************
    #* subsection: base_configs
    #*
    #*  apply base configurations to your devices
    @aetest.subsection
    def base_configs(self, testbed):
        '''Apply base configurations to your testbed devices

        < docstring >
        '''

        #* < apply base configs to device >
        #*
        #*  eg:
        #*      for device in testbed:
        #*          device.configure(...)


    #**********************************
    #* Any Other Subsections
    #*
    #*  use the following template for any further subsections that you need
    #*
    #*  def < subsectiop name >(self, <parameters>):
    #*      '''< descriptive name >
    #*
    #*       < docstring/description >
    #*      '''
    #*
    #*      < your code here>
    #*
    #*      # provide result if necessary
    #*      self.< result >()
    #*


#*******************************************************************************
#* TESTCASES
#*
#*  define new testcases by creating a class that inherits from aetest.Testcase
#*  top level class. You may define an arbitrary number of testcases in each 
#*  script. They will run in the order of definition as it appears in this file.  
#*
#*  https://pubhub.devnetcloud.com/media/pyats/docs/aetest/structure.html#testcases
class TemplateTestcase(aetest.Testcase):
    '''TemplateTestcase

    < docstring description of this testcase >

    Arguments:
        < data required to run this testcase >
    '''

    #**********************************
    #* Testcase Unique Id, Name & Description
    #*
    #*   Testcase uid should be unique to a test script. Below is their 
    #*   default values:
    #*
    #*      uid             unique id of this Testcase class
    #*      name            alternative descriptive name, default uid
    #*      description     docstring of this Testcase class
    #*
    #*   To set and alternative uid/name/description for each testcase, set the
    #*   Testcase class's 'uid', 'name' and 'description' attributes. Note that
    #*   uid cannot contain spaces.
    #*
    #*   Example:
    #*
    #*      class MyExampleTestcase(aetest.Testcase):
    #*          '''docstring for this testcase'''
    #*
    #*          uid = 'a_new_uid_for_my_example_testcase'
    #*          name = 'my meaningful testcase name'
    #*          description = 'a new description for my example testcase'
    #*
    #*   Note:
    #*      it's best to use to default to using the docstring for testcase
    #*      description

    # set alternative testcase uid
    # uid = '< testcase id >'

    # set a meaningful name to testcase
    # name = '< meaningful testcase name> '

    #**********************************
    #* Testcase Grouping
    #*
    #*  testcase grouping is an optional feature. It allows users to group/tag
    #*  testcases by common names, and enables group executions where only
    #*  a select groups of testcases is run.
    #*
    #*  associate testcases to groups by by setting its 'groups' attribute with
    #*  a list of groups names (strings). By default, testcases are not
    #*  associated to any groups.
    #*
    #*  Read More:
    #*  https://pubhub.devnetcloud.com/media/pyats/docs/aetest/control.html#testcase-grouping
    #
    # testcase groups
    #
    groups = ['group_A', 'group_B']

    #**********************************
    #* Testcase Data
    #*
    #*  define all the data required for the testcase to operate.
    #*  these data attributes should be define withe the testcase definition.
    #*
    #*      <data> = <value>
    #*
    #*  Example:
    #*      data_one = 'some values for data_one'
    #*      data_two = 'some values for data_two'
    #*      ... etc

    #**********************************
    #* Setup Section
    #* 
    #*  setup section is optional within each Testcase. It is always run if
    #*  defined. If the setup section's result is not Passed, Passx or Skipped,
    #*  all test sections will be skipped as a consequence.
    @aetest.setup
    def setup(self):
        '''Testcase Setup

        < docstring description of this Setup >
        '''

        pass

    #**********************************
    #* Test Section
    #* 
    #*  each testcase contains one or more tests. Each test is run one after
    #*  the other, in their defined order. 
    @aetest.test
    def template_test(self, steps):
        '''template test

        < docstring description of this test >
        '''

        #**********************************
        #* Testcase Steps
        #*
        #*  testcases can be further broken down into steps. Doing
        #*  so provides more visual cues of the actions taken of each section
        #*  and so on. 
        #*
        #*  Steps is applicable to subsections, setups, tests and cleanups.

        with steps.start('step description of step one'):
            pass

        with steps.start('step description of step two'):
            pass
        # ... etc

    #**********************************
    #* Cleanup Section
    #*
    #*  always run last in a testcase, the cleanup section is optional, and,
    #*  when defined, runs regardless of previous testcase/setup pass/fail 
    #*  results.
    @aetest.cleanup
    def cleanup(self):
        '''template cleanup

        < docstring description of this cleanup >
        '''

        pass
   

#*******************************************************************************
#* COMMON CLEANUP SECTION
#*
#*  use common cleanup section to remove all changes made to the environment
#*  during testscript execution and returning them to their original states.
#*
#*  the common cleanup section should be catch-all: it is always run regardless
#*  of testcase results, and thus should coded such that it perfroms a 'best
#*  attempt' removal of any potential changes, regardless of whether they
#*  actually exists.
#*
#*  consider breaking down common cleanup subsections so that it is the reversed
#*  order of common setup's subsections
#*
#*  https://pubhub.devnetcloud.com/media/pyats/docs/aetest/structure.html#common-cleanup
class CommonCleanup(aetest.CommonCleanup):
    '''Common Cleanup Section

    < common cleanup docstring >

    Subsections:
        < list the # of subsections and their intentions >

        < subsection > : < descriptions >
    '''

    #**********************************
    #* Subsection Template
    #*
    #*   To use, remove leading #* symbole and fill as required. Be careful of
    #*   indentation as Python is indentation sensitive.
    #*
    #*  def < subsectiop name >(self):
    #*      '''< descriptive name >
    #*
    #*       < docstring/description >
    #*      '''
    #*
    #*      < your code here>
    #*
    #*      # provide result if necessary
    #*      self.< result >()
    #*


#*******************************************************************************
#* STANDALONE EXECUTION
#*
#*   If this script is to be executed in standalone mode, e.g.
#*
#*      bash$ cd /path/to/script
#*      bash$ ./script.py
#*
#*   then the following should be added as the last thing in your test script.
#*******************************************************************************
if __name__ == '__main__':

    #**********************************
    #* Local Imports
    #*
    #*  these imports are here only because they are not required when the
    #*  testscript is normally run, and is only used during standalone runs.
    #*
    #*  this avoids polluting the script namespace

    #
    # local imports
    #
    import argparse
    from pyats import topology

    #**********************************
    #* Standalone Parsers
    #*
    #*  in jobfile execution, the infrastructure and the job file passes in
    #*  necessary script arguments. To achieve the same effect in standalone
    #*  execution, you need to create script command-line arguments to do the
    #*  same job.
    #*
    #*  use 'argparse' module.
    #*      https://docs.python.org/3/library/argparse.html
    #*
    #*  Guidelines:
    #*      - all custom arguments should start with double dash '--'
    #*      - parsing should only ever be done using parse_known_args(), as
    #*        the engine also parses its argument during main()
    #*
    #*  in the example below, we've added the --testbed argument for you.

    #
    # local standalone parsing
    #
    parser = argparse.ArgumentParser(description = "standalone parser")
    parser.add_argument('--testbed', dest = 'testbed',
                        help = 'testbed YAML file',
                        type = topology.loader.load,
                        default = None)

    # do the parsing
    args = parser.parse_known_args()[0]

    #**********************************
    #* aetest.main()
    #*
    #*  this runs the testscript. Pass in any additional script arguments
    #*  in so that it becomes the base part of your testscript parameters.

    #
    # calling aetest.main() to start testscript run
    #
    aetest.main(testbed = args.testbed)

