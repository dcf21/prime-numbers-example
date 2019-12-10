#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Routines for searching for prime numbers
"""

import argparse
import logging
import sys

from prime_numbers import PrimeNumbers


class PrimeNumbersDifferentOutput(PrimeNumbers):
    """
    Routines for searching for prime numbers
    """

    @classmethod
    def report_prime_number(cls, value):
        print("{:d}".format(value))


# Do it right away if we're run as a script
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        stream=sys.stdout,
                        format='[%(asctime)s] %(levelname)s:%(filename)s:%(message)s',
                        datefmt='%d/%m/%Y %H:%M:%S')
    logger = logging.getLogger(__name__)
    logger.info(__doc__.strip())

    # Read command-line arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--test-min', dest='test_min', type=int, default=2,
                        help="The lowest number to test.")
    parser.add_argument('--test-max', dest='test_max', type=int, default=20,
                        help="The highest number to test.")
    args = parser.parse_args()

    PrimeNumbersDifferentOutput.search_for_primes(test_min=args.test_min, test_max=args.test_max)
