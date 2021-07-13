import argparse
import datetime
import os
import sys
import time

# import the pyDaisyHat package from the daisyHat submoduel path
pathToPyDaisyHatPackage = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib", "daisyHat", "python"))
sys.path.append(pathToPyDaisyHatPackage)

import pyDaisyHat

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # We pass this argument from CMake
    parser.add_argument("--elf", action="store", type=str,
                        help="The firmware image to flash")
    # This argument is implicitly added by daisyhat_add_custom_test()
    parser.add_argument("--config", action="store", type=str,
                        help="The daisyHat config file")
    args = parser.parse_args()

    # read daisyHat config file from the provided path (e.g. daisyHat.config.json)
    # or use the override (as provided with environment variable DAISYHAT_CONFIG_FILE_OVERRIDE)
    pyDaisyHat.readConfigFile(args.config)
    # create DaisySeed object to interact with the seed "Alice" (as configured in the config file)
    seed = pyDaisyHat.DaisySeed("Alice")
    # flash the firmware image
    seed.uploadFirmwareElfAndStartSerial(args.elf)

    # start the test execution on the seed
    seed.startTestExecution()

    # let "Alice" measure the time between two signals from us on the host side
    seed.serialConnection.sendSignal("before_host_delay")
    time.sleep(0.5)
    seed.serialConnection.sendSignal("after_host_delay")

    # measure the time until a signals from "Alice" arrives
    start = datetime.datetime.now()
    seed.serialConnection.awaitSignal("after_seed_delay")
    end = datetime.datetime.now()
    timeDiff = end - start
    timeDiffMs = timeDiff.total_seconds() * 1000
    # expect that there was some delay (accurate time 
    # measurement is not possible, the serial line timing is
    # too inaccurate)
    pyDaisyHat.EXPECT_GT(timeDiffMs, 500)

    # wait for the test to complete on "Alice"
    result = seed.awaitTestResult()
    # also consider our own assertion results
    result = result and pyDaisyHat.numFailedAssertions == 0

    # return the result to the test environment
    sys.exit(0 if result == True else 1)
