# NovelProteinFinder
(Written in 2024 by a.l.o gaenssle, check github.com/gaenssle/NovelProteinFinder for updates)

This program has been written to easily download a list of PULS from the PUL-DB (http://www.cazy.org/PULDB/) and export the data into a csv table. It also gives the option to filter the obtained PULs based on PUL length (number of genes in the PUL) and specific proteins present in the PUL.

This program imports html files from the PUL DB, extracts and filters the data
- It takes a file or link as input and extract the html data into a csv file
- It then allows you to filter the data bases on two types:
	* PUL length (accepts a range)
	* Specific proteins in puls (accepts selections from a list)


OVERALL REQUIREMENTS:
- The data has to be a link to a specific PULDB website or the source code from the given website
- There are default name endings but they can be changed

REQUIRE PYTHON MODULES:
- bs4 (beautiful soup)
- matplotlib
- pandas
- tkinter
(re, os, sys)


