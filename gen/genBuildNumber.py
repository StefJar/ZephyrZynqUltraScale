#!/usr/local/bin/python3
# encoding: utf-8
'''
genBuildNumber -- generates an incrementing build number

genBuildNumber generates an incrementing build number

@author:     Stefan Jaritz

@copyright:  2025 Stefan Jaritz

@license:    GPL

@deffield    updated: Updated
'''

import sys

import os
import enum
import logging
import datetime

from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter

__all__ = []
__version__ = 1.0
__date__ = '2025-01-02'
__updated__ = '2025-01-02'

_C_HEADER_FILENAME = "_gen_buildNumber.h"

_HEADER_TXT_TMPL ="""/*
 * {fn}
 *
 *  generated {date}
 * 
 */

#ifndef BUILD_NUMBER_H_
#define BUILD_NUMBER_H_

// firmware version
#define FW_BUILD_NUMBER {BN}

#endif /* BUILD_NUMBER_H_ */

"""

class CLIError(Exception):
    '''Generic exception to raise and log different fatal errors.'''
    def __init__(self, msg):
        super(CLIError).__init__(type(self))
        self.msg = "E: %s" % msg
    def __str__(self):
        return self.msg
    def __unicode__(self):
        return self.msg

def main(argv=None): # IGNORE:C0111
    '''Command line options.'''
    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)
   
    program_name = os.path.basename(sys.argv[0])
    program_version = "v%s" % __version__
    program_build_date = str(__updated__)
    program_version_message = '%%(prog)s %s (%s)' % (program_version, program_build_date)
    program_shortdesc = __import__('__main__').__doc__.split("\n")[1]
    program_license = '''%s

  Created by user_name on %s.
  Copyright Stefan Jaritz. All rights reserved.

  Licensed under the Apache License 2.0
  http://www.apache.org/licenses/LICENSE-2.0

USAGE
''' % (program_shortdesc, str(__date__))

    try:
        # Setup argument parser
        parser = ArgumentParser(description=program_license, formatter_class=RawDescriptionHelpFormatter)
        parser.add_argument('-V', '--version', action='version', version=program_version_message)

        parser.add_argument('-w', '--workingDir',
            help = "working directory default: %(default)s",
            type=str,
            default=os.path.join(os.getcwd(),"..","src")
        )
        # Process arguments
        args = parser.parse_args()
                
        logging.basicConfig(level=logging.DEBUG)
        
        logging.info("working dir {}".format(args.workingDir))
        print("generate build number")

        if not os.path.exists(args.workingDir):
            logging.error("working dir does not exists")
            return -1
        
        buildNbrFile = os.path.join(args.workingDir,"buildNumber.txt")
        
        if True == os.path.isfile(buildNbrFile):
            with open(buildNbrFile, "r") as f:
                numberStr = f.read()
            buildN = int(numberStr)
        else:
            logging.warning("build number file does not exist. Searched at {}".format(buildNbrFile))
            buildN = int(0)
        
        buildN += 1
        
        logging.info("new build number {}".format(buildN))
        
        with open(buildNbrFile, "w") as f:
            logging.info("save new build number")
            numberStr = str(buildN)
            f.write(numberStr)
        
        buildNbrHeaderFile = os.path.join(args.workingDir,_C_HEADER_FILENAME)
        
        with open(buildNbrHeaderFile, "w") as f:
            logging.info("create header file")
            txt = _HEADER_TXT_TMPL.format(
                fn=_C_HEADER_FILENAME,
                date = datetime.datetime.now(), 
                BN = buildN
            )
            f.write(txt)
        
        print("done")
        return 0
    except KeyboardInterrupt:
        ### handle keyboard interrupt ###
        return 0
    except Exception as e:
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        return 2

if __name__ == "__main__":
    sys.exit(main())
