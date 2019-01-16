# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
# Name:        world_pop_explorer_tests.py
#
# Purpose:     Test functions for functions in world_pop_explorer.py
#
# Author:      David Viljoen
#
# Created:     24/11/2017
#-------------------------------------------------------------------------------

import sys
import inspect
import world_pop_explorer as wpe
reload(wpe)

def main():
    # Find and call all functions that begin with "test"
    test_funcs = get_test_functions()
    for test_func in test_funcs:
        test_func()

# Copy/paste/change the test template below to create new test functions, where:
#    - the test function name must begin with the word "test"
#    - desc = Description of the test being made
#    - expected = Expected result from calling the function
#    - actual = Actual result from calling the function
#    - func = Function being tested (the actual function, not the name)"""
#
def template_for_test_functions():
    """Doc string to describe test function"""
    expected = ""
    actual = ""
    print_test_results(func, expected, actual)

# ------------------------------------------------------------------------------

def test_get_country_count():
    """Get country count from population list"""
    expected = 233
    actual = wpe.get_country_count()
    print_test_results(wpe.get_country_count, expected, actual)

def test_conv_num_with_commas():
    """Test for conversion of text 1,000 to number 1000"""
    expected = 4244
    actual = wpe.conv_num_with_commas('4,244')
    print_test_results(wpe.conv_num_with_commas, expected, actual)


def test_get_top_five_countries():
    """Test for top five countries where China is 1st and Brazil 5th"""
    expected = ['China', 'India', 'United States', 'Indonesia', 'Brazil']
    actual = wpe.get_top_five_countries()
    print_test_results(wpe.get_top_five_countries, expected, actual)


def test_set_country_populations_dict():
    """Test for the country Réunion"""
    expected = (876562,0)
    actual = wpe.set_country_populations_dict().get("Réunion")
    print_test_results(wpe.set_country_populations_dict, expected, actual)

def test_get_population():
    """Test for the country Réunion"""
    expected = 876562
    actual = wpe.get_population("Réunion")
    print_test_results(wpe.get_population, expected, actual)


def test_get_continents():
    """Test for number of continents"""
    expected = 5
    actual = len(wpe.get_continents())
    print_test_results(wpe.get_continents, expected, actual)


def test_get_continent_populations():
    """Test for population of Asia being larger than 4.5B"""
    expected = True
    actual = wpe.get_continent_populations()['Asia'] > 4500000000
    print_test_results(wpe.get_continent_populations, expected, actual)


# ------------------------------------------------------------------------------
# Testing helper functions  - safely ignore the rest of this script
# ------------------------------------------------------------------------------
def get_test_functions():
    """Returns a list of functions that begin with the word test in the order
       they appear in this file."""

    test_funcs = [obj for name,obj in inspect.getmembers(sys.modules[__name__])
                     if (inspect.isfunction(obj) and name.startswith('test'))]
    src = inspect.getsource(sys.modules[__name__])
    lines = src.split('\n')

    # Create a dictionary with key=function name and value is 0-based order
    # in the module
    ordered_func_names = dict()
    ordered_funcs = list()
    func_index = 0
    for line in lines:
        if line.find("def test") > -1 and not line.find('line.find') > -1:
            func_name = line.split("(")[0].split()[1]
            ordered_func_names[func_name] = func_index
            # Create an empty list with sampe number of elements as test
            # functions
            ordered_funcs.append('')
            func_index += 1
    for test_func in test_funcs:
        index = ordered_func_names[test_func.__name__]
        ordered_funcs[index] = test_func
    return ordered_funcs

def print_test_results(func_tested, expected, actual):
    """func_tested is the function being tested
       expected = Expected result of test
       actual = Actual result of test """

    if not callable(func_tested):
        raise Exception("{} is not a function".format(func_tested))

    func_name = func_tested.__name__
    desc = func_tested.__doc__

    if expected == actual:
        print "PASSED: {}".format(func_name)
        print "Detail: {}".format(desc)
    else:
        print "FAILED: {}".format(func_name)
        print "Desc:   {}".format(desc)
        print "Expect: {}".format(expected)
        print "Actual: {}".format(actual)
    print ""

if __name__ == '__main__':
    main()
