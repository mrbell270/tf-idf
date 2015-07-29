from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint


class MyHTMLParser(HTMLParser):
    def __init__(self):
        self.HTMLData = ''
        self.DataTags = ['a', 'p']
        self.WriteData = 0
        self.reset()

    def handle_starttag(self, tag, attrs):
        # print "Start tag:", tag
        if tag in self.DataTags:
            self.WriteData += 1
        for attr in attrs:
            # print "     attr:", attr
            pass

    def handle_endtag(self, tag):
        if tag in self.DataTags:
            self.WriteData -= 1
        # print "End tag  :", tag

    def handle_data(self, data):
        # print "Data     :", data
        if self.WriteData > 0:
            self.HTMLData += ' ' + data

    def handle_comment(self, data):
        # print "Comment  :", data
        pass

    def handle_entityref(self, name):
        pass
        # c = unichr(name2codepoint[name])
        # print "Named ent:", c

    def handle_charref(self, name):
        if name.startswith('x'):
            c = unichr(int(name[1:], 16))
        else:
            c = unichr(int(name))
        # print "Num ent  :", c

    def handle_decl(self, data):
        pass # print "Decl     :", data
