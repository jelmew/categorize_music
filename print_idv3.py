import sqlite3
import eyed3
import fnmatch
import os
from os.path import join, getsize

def listDirs(dir):
    for root, subFolders,files in os.walk(dir,topdown=False):
        list_of_files=[os.path.join(root,f) for f in files]
        mp3_list=[f for f in list_of_files if ".mp3" in f]
        yield mp3_list
def main():
    #MainRunroutine
    return

#if __name__=="__main__":
def load_all_mp3_files(input_dir):
    for mp3_list in listDirs(input_dir):
            for mp3_file in mp3_list:
                eyed3_file=eyed3.load(mp3_file)
                if eyed3_file.tag==None: continue
                yield eyed3_file


if __name__=="__main__":
    conn=sqlite3.connect('example.db')
    c=conn.cursor()
    c.execute("CREATE TABLE test (artist text, title text)")
    for mp3 in load_all_mp3_files("/home/jelmer/Music"):
        insert=(mp3.tag.artist, mp3.tag.title)
        print insert
        c.execute("Insert INTO test VALUES(?,?)",insert)
        #c.execute("Insert INTO test VALUES ('text','title')")
        #c.execute("INSERT INTO test VALUES ('{}','{}')".format(mp3.tag.artist, mp3.tag.title))
    conn.commit()
    conn.close()
