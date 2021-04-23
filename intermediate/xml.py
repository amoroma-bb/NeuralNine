import xml.sax

class GroupHandler(xml.sax.ContentHandler):

    def startElement(self,name,attrs):
        self.current = name
        print(name)

handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('data.xml')
