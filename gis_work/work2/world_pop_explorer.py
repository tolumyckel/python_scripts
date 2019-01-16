# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
# Name:        world_pop_explorer.py
#
# Purpose:     Provide some functions to analyze the data in
#              world_pop_by_country.py
#
# Author:      David Viljoen
#
# Created:     24/11/2017
#-------------------------------------------------------------------------------

from world_pop_by_country import data as country_populations

# Key = country and value is number (i.e. not text containing commas)
#
country_populations_dict = dict()

def main():
    lines = country_populations.split('\n')
    print "country_populations has the following columns:"
    print lines[0]
    print repr(lines[0])
    ci = lines[162]
    print "\nData is UTF-8 encoded.  That is, printed as is:"
    print ci
    print "\nData prined with .decode('utf-8'):"
    print ci.decode('utf-8')
    print get_continents()

def get_country_count():
    """Return the number of countries in country_populations.  Create a list
	   where each element of the list contains a line of data from
	   country_populations and return the length of this list"""

    countries_list = country_populations.split('\n')
    countries_list.remove(countries_list[0])
    return len(countries_list)

def conv_num_with_commas(number_text):
    """Convert a number with commas (str) to a number.
       e.g. '1,000' would be converted to 1000"""

    num_list = list(number_text)
    while ',' in num_list:
        num_list.remove(',')

    num = int(''.join(num_list))
    return num

def get_top_five_countries():
    """Return a list of names of the top five countries in terms of population"""

    countries_list = country_populations.split('\n')
    top_five = []
    for i in range(5):
        i += 1
        top_five.append(countries_list[i].split('\t')[1])
    return top_five


def set_country_populations_dict():
    """Sets the country_populations_dict dictionary where key is country name
         and value is a tuple containing two elements:
            1. A numeric version of the comma separated number in the
               Pop 01Jul2017 column
            2. The % decrease as a number
    """


    countries_list = country_populations.split('\n')
    for i in range(get_country_count()):
        i += 1
        country = countries_list[i].split("\t")[1]
        pop_2017 = conv_num_with_commas(countries_list[i].split("\t")[-2])
        if countries_list[i].split("\t")[-1][0] == "-":
            percent_dec = float(countries_list[i].split("\t")[-1][1:].strip("%"))
        else:
            percent_dec = 0
        #print type((pop_2017,percent_dec))

        country_populations_dict[country] = (pop_2017,percent_dec)
    return country_populations_dict

def get_population(country_name):
    """Given the name of the country, return the population as of 01Jul2017
       from country_populations_dict.  If the country_populations_dict is
       empty (i.e. no keys or values), then run set_country_populations_dict
       to initialize it."""

    if len(country_populations_dict) == 0:
        set_country_populations_dict()
        return country_populations_dict[country_name][0]
    else:
        return country_populations_dict[country_name][0]

def get_continents():
    """Return the list of continents"""

    countries_list = country_populations.split('\n')
    continents = []
    for i in range(get_country_count()):
        i += 1
        continent = countries_list[i].split("\t")[2]
        if continent not in continents:
            continents.append(continent)
    return continents


def get_continent_populations():
    """Returns a dict where the key is the name of the continent and
       the value is the total of all countries on that continent"""

    countries_list = country_populations.split('\n')
    continent_pop = dict()
    total = 0
    for i in range(get_country_count()):
        i += 1
        if countries_list[i].split("\t")[2] in get_continents():
            total += conv_num_with_commas(countries_list[i].split("\t")[-2])
            continent_pop[countries_list[i].split("\t")[2]] = int(total)
    return continent_pop

if __name__ == '__main__':
    main()
