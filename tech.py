import csv
import re
from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import sys, getopt
from bs4 import BeautifulSoup
import urllib2
from urllib2 import urlopen
#Function converting pdf to string
def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text
#Function to extract names from the string, generally in a resume the name is in the first 2 charachters of the string
def extract_name(string):
    spitted = string.split()
    print(' '.join(spitted[:2]))
#Function to extract Phone Numbers from string using regular expressions
def extract_phone_numbers(string):
    r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    phone_numbers = r.findall(string)
    return [re.sub(r'\D', '', number) for number in phone_numbers]
#Function to extract Email address from a string using regular expressions
def extract_email_addresses(string):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    return r.findall(string)
#Converting pdf to string
resume_string = convert("/home/ashay/cvscan/data/sample/cv3.pdf")
#Removing commas in the resume for an effecient check
resume_string = resume_string.replace(',','')
#Converting all the charachters in lower case
resume_string = resume_string.lower()

def extract_information(string):
    string.replace (" ", "+")
    query = string
    #replaces whitespace with a plus sign for Google compatibility purposes
    soup = BeautifulSoup(urlopen("https://en.wikipedia.org/wiki/" + query), "html.parser")
    #creates soup and opens URL for Google. Begins search with site:wikipedia.com so only wikipedia
    #links show up. Uses html parser.
    for item in soup.find_all('div', attrs={'id' : "mw-content-text"}):
        print(item.find('p').get_text())
        print('\n')

with open('technicalskills.csv', 'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)
#Sets are used as it has a a constant time for lookup hence the overall the time for the total code will not exceed O(n)
s = set(your_list[0])
skills = []
print('\n')
extract_name(resume_string)
print('\n')
print('Phone Number is')
print(extract_phone_numbers(resume_string))
print('\n')
print('Email id is')
print(extract_email_addresses(resume_string))
for word in resume_string.split(" "):
    if word in s:
        skills.append(word)
skill = set(skills)
print('\n')
print("Following are his/her Technical Skills")
print(skill)

with open('nontechnicalskills.csv', 'rb') as f:
    reader = csv.reader(f)
    your_list1 = list(reader)
#Sets are used as it has a a constant time for lookup hence the overall the time for the total code will not exceed O(n)
s1 = set(your_list1[0])
nontechskills = []
for word in resume_string.split(" "):
    if word in s1:
        nontechskills.append(word)
nontechskills = set(nontechskills)
print('\n')
print("Following are his/her Non Technical Skills")
print(nontechskills)
print('\n \n')
skill = list(skill)
for i in range(len(skill)):
    print(skill[i])
    extract_information(skill[i])
