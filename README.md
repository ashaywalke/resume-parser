# Resume-Parser

## Extracting name, email, phonenumber, skills

Code to parse information such as Name, Email, Phone Number, skillset and the technology associated with it.

## requirements
Following is the list of python libraries required

    cStringIO
    re
    csv
    pdfminer
    BeautifulSoup
    urllib2
    spacy

Spacy is an Industrial-Strength Natural Language Processing tool which is used here to detect Indian Names in the resume after pip installing spacy make sure that you install 'xx' model which supports foreign languages

    python -m spacy download xx
    

## Code

Set the directory to the one which contains the extracted files, and save your resume with the file name, resume.pdf in the same directory. 

    $ python resumeparser.py

## Sample Output

![Page](https://i.imgur.com/4U6IfvX.png)

