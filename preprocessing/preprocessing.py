import os

print "Start Preprocessing ... "

print "Generate new Author.csv"
os.system("python gen_author.py")

print "Generate new Conference.csv"
os.system("python gen_conference.py")

print "Generate new Journal.csv"
os.system("python gen_journal.py")

print "Generate new Paper.csv"
os.system("python gen_paper.py")

print "Generate new PaperAuthor.csv"
os.system("python gen_paperauthor.py")

print "\nFinish"