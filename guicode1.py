from tkinter import *
from tkinter import filedialog
from ttkthemes import themed_tk as tk
import tkinter.messagebox
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import HTMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from tkinter import ttk
import io
import bs4
import nltk
import re
from nltk.corpus import stopwords
stop = stopwords.words('english')
import shutil

#----------title----------#
root = tk.ThemedTk()
root.get_themes()
root.set_theme("radiance")
root.title("CV_Analyzer")


#---------menubar---------#
menubar = Menu(root,activeborderwidth=0)
root.config(menu=menubar,highlightthickness=0)
root.config(bg='#ddd', menu=menubar)

#--------submenu----------#

subMenu1 = Menu(menubar,tearoff=0)
subMenu2 = Menu(menubar,tearoff=0)
subMenu3 = Menu(menubar,tearoff=0)


def _Light_Theme():
    root.configure(bg='#eee')
    subMenu1.configure(bg="#eee",fg='#161b21')
    subMenu2.configure(bg="#eee",fg='#161b21')
    subMenu3.configure(bg="#eee",fg='#161b21')
    f1.configure(bg="#eee")
    f2.configure(bg="#eee")
    f3.configure(bg="#eee")
    f4.configure(bg="#eee")
    label.configure(bg="#eee",fg='#161b21')
    label1.configure(bg="#eee", fg='#161b21')
    label2.configure(bg="#eee", fg='#161b21')
    label3.configure(bg="#eee", fg='#161b21')
    qualification.configure(bg="#eee", fg='#161b21')
    experience.configure(bg="#eee", fg='#161b21')
    coding.configure(bg="#eee", fg='#161b21')
    skills.configure(bg="#eee", fg='#161b21')
    achievements.configure(bg="#eee", fg='#161b21')
def _Dark_Theme():
    root.configure(bg='#161b21')
    subMenu1.configure(bg="#161b21",fg='#eee')
    subMenu2.configure(bg="#161b21",fg='#eee')
    subMenu3.configure(bg="#161b21",fg='#eee')
    f1.configure(bg="#161b21")
    f2.configure(bg="#161b21")
    f3.configure(bg="#161b21")
    f4.configure(bg="#161b21")
    label.configure(bg="#161b21", fg='#eee')
    label1.configure(bg="#161b21", fg='#eee')
    label2.configure(bg="#161b21", fg='#eee')
    label3.configure(bg="#161b21", fg='#eee')
    qualification.configure(bg="#161b21", fg='#eee')
    experience.configure(bg="#161b21", fg='#eee')
    coding.configure(bg="#161b21", fg='#eee')
    skills.configure(bg="#161b21", fg='#eee')
    achievements.configure(bg="#161b21", fg='#eee')

def _browse():
    raise_frame(f3)


def _quit():
    root.quit()

def _about():
    tkinter.messagebox.showinfo('CV_analyzer','Cv_Analyser 1.0   "An ML and NLP implementation"\n\n@ cv.analyzer@gmail.com\n\nVerifies CVs and arrange them according to users requirements.')

menubar.add_cascade(label="File",menu=subMenu1)
subMenu1.add_command(label="Open",command=_browse)
#subMenu1.add_separator()
subMenu1.add_command(label="Exit",command=_quit)

menubar.add_cascade(label="Settings",menu=subMenu2)
subMenu2.add_command(label="Light Theme",command_=_Light_Theme)
subMenu2.add_command(label="Dark Theme",command_=_Dark_Theme)

menubar.add_cascade(label="About",menu=subMenu3)
subMenu3.add_command(label="About CV_Analyzer",command=_about)

#-------windowConfig--------#

root.geometry('700x500')
root.configure(bg='#eee')
root.iconbitmap(r'cv_analyzer.ico')
root.resizable(0, 0)


def raise_frame(frame):
    frame.tkraise()

f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)

for frame in (f1, f2 ,f3,f4):
    frame.grid(row=0, column=0, sticky='news')



path = ''
def extract_text_from_pdf(pdf_path):
    global path
    path=pdf_path
    resource_manager = PDFResourceManager()
    fake_file_handle = io.BytesIO()
    converter = HTMLConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)
        text = fake_file_handle.getvalue()
    # close open handles
    converter.close()
    fake_file_handle.close()
    if text:
        return text




def _browse(case):
    if __name__ == '__main__':
        fileHTML = 'pdfconverted1.html'
    if case == 'HTML' :

        fileConverted = open(fileHTML, "wb")
        fileConverted.write(convert)
        fileConverted.close()





datas = []


def reverseEng():
    f = open('pdfconverted1.html', 'r')  # pdfconverted1.html file opened for reading.
    html_string = f.read()  # the content from file is readed and sets to "html_string".
    #print(html_string)  #just printed for checking.
    new_file = open('new_file.txt', 'w')  # a newfile "new_file.txt" opened for writing and sets to "new_file".
    new_file.write(html_string)  # contents from variable "html_string" writed to "new_file"
    soup = bs4.BeautifulSoup(html_string,"html.parser")  # the tags are removed (eg: <body>, <p>) using "bs4" sets to "soup"
    soup.get_text()  # printed for checking
    soup_text = soup.get_text()  # the texts are fetched and sets to "soup_text"
    converted = open('converted_text.txt', 'w')  # opened a new file "converted_text.txt" for writing
    converted.write(soup.get_text())  # the text contents writed to the above  created file
    f.close()  # the file "abcd.html" closed
    if converted:

        tkinter.messagebox.showinfo('CV_analyzer',
                                        'Reverse engineering completed')
    converted.close()
    new_file.close()


    with open("converted_text.txt") as file:
        lines = file.read().split()
        global datas
        datas = lines
        print(datas)
        return datas

#######################################################################################################################

li = []
def get_data(values):
    global li
    #print(values)
    li.append(values)
    print(li)
    return li
pcount = 0
ncount = 0

###########################################################################################################

def compare():


    for i in li:
        for j in datas:
            if (i==j):

                globals()['pcount'] = pcount + 1
            else:
                globals()['ncount'] = ncount + 1
    print(pcount)


#########################################################################################################################


def extract_phone_numbers(stringdata):
    r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    phone_numbers = r.findall(stringdata)
    return [re.sub(r'\D', '', number) for number in phone_numbers]

def extract_email_addresses(stringdata):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    return r.findall(stringdata)

def ie_preprocess(stringdata):
    stringdata = ' '.join([i for i in stringdata.split() if i not in stop])
    sentences = nltk.sent_tokenize(stringdata)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return sentences

def extract_names(stringdata):
    names = []
    sentences = ie_preprocess(stringdata)
    for tagged_sentence in sentences:
        for chunk in nltk.ne_chunk(tagged_sentence):
            if type(chunk) == nltk.tree.Tree:
                if chunk.label() == 'PERSON':
                    names.append(' '.join([c[0] for c in chunk]))
    return names

#with open("D:/Project/SETHU CVS/converted_text.txt") as file:# file "converted.txt" opened.
 #   stringdata = file.read()
######################################################################################################################

def check():
    if(pcount>=(len(li)/2)):
        tkinter.messagebox.showinfo('CV_Analyzer', 'Analysis Completed : '
                                                   'GooD')
        with open("converted_text.txt") as file:  # file "converted.txt" opened.
            stringdata = file.read()

        numbers = extract_phone_numbers(stringdata)
        emails = extract_email_addresses(stringdata)
        names = extract_names(stringdata)
        info = open('goodresumeinfo.csv','w')
        num = ', '.join(numbers)
        mails = ', '.join(emails)
        name = ', '.join(names)
        print("The name is ", name)
        print("The phone number is ", num)
        print("The email address is ", mails)
        shutil.copy(path, 'GoodResumes/')

        info.write(name)
        info.write(num)
        info.write(mails)
        info.close()
    else:
        tkinter.messagebox.showinfo('CV_Analyzer','Analysis Completed : '
                                    'NoT GooD')
        with open("D:/Project/SETHU CVS/converted_text.txt") as file:  # file "converted.txt" opened.
            stringdata = file.read()
        numbers = extract_phone_numbers(stringdata)
        emails = extract_email_addresses(stringdata)
        names = extract_names(stringdata)
        info = open('badresumeinfo.csv','w')
        num = ', '.join(numbers)
        mails = ', '.join(emails)
        name = ', '.join(names)
        print("The name is ", name)
        print("The phone number is ", num)
        print("The email address is ", mails)
        shutil.copy(path, 'BadResumes')

        info.write(name)
        info.write(num)
        info.write(mails)
        info.close()


###################################################################################################
def check_another():
    globals()['pcount'] = 0
    globals()['ncount'] = 0
    #if(pcount>ncount):
     #   print("good")


def new():
    li.clear()
    print(li)

def list_clear():
    li.clear()


###################################################################################################

#compare(li,datas)
#print(pcount)
#print(ncount)


#Test function
def test():
    print("Hai")

#test()


#Requirements selection

var = StringVar()
label3 = Label( f1, textvariable=var)
label3.configure(font=("Helvetica", "13"))
var.set("\n\nInput Your 'REQUIREMENTS'")
label3.pack()
label3.place(x=235,y=0)

var1 = StringVar()
qualification = Label( f1, textvariable=var1)
var1.set("Qualification")
qualification.pack()
qualification.place(x=190, y=90)

var2 = StringVar()
experience = Label( f1, textvariable=var2)
var2.set("Experiences")
experience.pack()
experience.place(x=190, y=140)

var3 = StringVar()
coding = Label( f1, textvariable=var3)
var3.set("Coding")
coding.pack()
coding.place(x=190, y=190)

var4 = StringVar()
skills = Label( f1, textvariable=var4)
var4.set("Passout year")
skills.pack()
skills.place(x=190, y=240)

var5 = StringVar()
achievements = Label( f1, textvariable=var5)
var5.set("Skills")
achievements.pack()
achievements.place(x=190, y=290)

analysebtn = ttk.Button(f1, text="Analyse",command=lambda:[compare(),check()]).place(x=180, y=340)
analysebtnss = ttk.Button(f1, text="Check_Another",command=lambda:[check_another,raise_frame(f3)]).place(x=320, y=340)
analysebtnsss = ttk.Button(f1, text="Clear_ReQ",command=lambda:[new,raise_frame(f3)]).place(x=470, y=340)


variable = StringVar(f1)
variable.set(None)
qualifications = ttk.OptionMenu(f1, variable, "None","MCA" ,"BCA", "Btech","Mtech",command=get_data).place(x=290, y=90)

variable1 = StringVar(f1)
variable1.set(None)
experiences = ttk.OptionMenu(f1, variable1, "None","Fresher" ,"One Year", "Two Years","Five Years",command=get_data).place(x=290, y=140)

variable2 = StringVar(f1)
variable2.set(None)
language1 = ttk.OptionMenu(f1, variable2, "None","C++" ,"C#", "Java","Python","JavaScript",command=get_data).place(x=290, y=190)

variable3 = StringVar(f1)
variable3.set(None)
language2 = ttk.OptionMenu(f1, variable3, "None","C++" ,"C#", "Java","Python","JS","JQuery",command=get_data).place(x=370, y=190)

variable4 = StringVar(f1)
variable4.set(None)
language3 = ttk.OptionMenu(f1, variable4, "None","C++" ,"C#", "Java","Python","JS","JQuery",command=get_data).place(x=450, y=190)

variable5 = StringVar(f1)
variable5.set(None)
language4 = ttk.OptionMenu(f1, variable5, "None","C++" ,"C#", "Java","Python","JS","JQuery",command=get_data).place(x=530, y=190)

variable6 = StringVar(f1)
variable6.set(None)
passout_year = ttk.OptionMenu(f1, variable6,"None","2016","2017","2018","2019",command=get_data).place(x=290, y=240)


variable7 = StringVar(f1)
variable7.set(None)
skills = ttk.OptionMenu(f1, variable7,"None","Good Communication Skill","Team Work","Effective Time Management","Team Work",command=get_data).place(x=290, y=290)


#end requirement selection


ttk.Button(f3,text="Upload_CV",command=lambda:[_browse(case='HTML'),raise_frame(f2)]).pack(pady=(210),padx=(260))
ttk.Button(f2,text="ReverseEngineering",command=lambda:[reverseEng(),raise_frame(f1)]).pack(pady=(210),padx=(260))
ttk.Button(f4, text='Start processing', command=lambda:raise_frame(f3)).pack(pady=(210),padx=(290))

var = StringVar()
label = Label( f4, textvariable=var)
labelname="CV ANALYZER"
labelname.casefold()
label.configure(font=("Helvetica", "13"))
var.set(labelname+"\n\nA Machine Learning and NLP innovative\n for analysing 'RESUMES' ")
label.pack()
label.place(x=215,y=120)

var = StringVar()
label1 = Label( f3, textvariable=var)
labelname.casefold()
label1.configure(font=("Helvetica", "13"))
var.set(labelname+"\n\nUpload the resume that \nyou need to analyse. ")
label1.pack()
label1.place(x=270,y=120)

var = StringVar()
label2 = Label( f2, textvariable=var)
labelname.casefold()
label2.configure(font=("Helvetica", "13"))
var.set(labelname+"\n\nArt of breaking files into \nit's simple form. ")
label2.pack()
label2.place(x=270,y=120)


root.mainloop()


