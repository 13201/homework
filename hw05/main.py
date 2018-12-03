import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self,n):
        '''/n_row'''

        html = '''
        <html>
        <body>
        <table>
        '''
        html += '<h1>'"Multiplication Table"
        html += '</h1>'

        for i in range(1,10):
            html += '<TR>'
            for  j  in range (1,i+1):
                html+=("<TD>{}x{}={:2} </TD>".format(j, i, i*j))
            html += '</TR>'
            

        html += '''
        </table>
        </body>
        </html>
        '''

        self.write(html)

class OneHandler(tornado.web.RequestHandler):
    def get(self,n):
        '''/n_row'''

        html = '''
        <html>
        <body>
        <table>
        '''
        html += '<h1>'"Multiplication Table"
        html += '</h1>'

        if (n is None):
            n=9
        else:
            int ( n )
            n = int (self.get_argument( 1,n ))

        for i in range(1,n+1):
            html += '<TR>'
            for  j  in range (1,i+1):
                html+=("<TD>{}x{}={:2} </TD>".format(j, i, i*j))
            html += '</TR>'
            

        html += '''
        </table>
        </body>
        </html>
        '''

        self.write(html)

application = tornado.web.Application([
    (r"/(?:/([0-9]))?", MainHandler),
    (r"(?:/([0-9]))?", OneHandler),
],debug=True)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
