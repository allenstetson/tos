#!/usr/bin/python

import web
import cgitb; cgitb.enable() # for troubleshooting

urls=("/.*", "Index")
app = web.application(urls, globals())

class Index(object):
    def GET(self):
        #output = Page(form).generateOutput('./templates/templateAnnouncementManagement.htm')
        output = "TOS page initialized."
        return output


if __name__ == '__main__':
    #print("Content-type: text/html\r\n\r\n")
    app.run()
