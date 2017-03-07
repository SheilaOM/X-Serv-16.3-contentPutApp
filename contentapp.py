#!/usr/bin/python3

"""
 contentApp class
 Simple web application for managing content

 Copyright Jesus M. Gonzalez-Barahona, Gregorio Robles 2009-2015
 jgb, grex @ gsyc.es
 TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
 October 2009 - March 2015
"""

import webapp


class contentApp (webapp.webApp):
    """Simple web application for managing content.

    Content is stored in a dictionary, which is intialized
    with the web content."""

    # Declare and initialize content
    content = {'/': 'Root page',                        #Variables de clase.
               '/page': 'A page'
               }

    def parse(self, request):
        """Return the resource name (including /)"""
        self.toma()
        return (request.split(' ', 1)[0], request.split(' ', 2)[1], request.split('=')[-1])

    def process(self, parsed):
        """Process the relevant elements of the request.

        Finds the HTML text corresponding to the resource name,
        ignoring requests for resources not in the dictionary.
        """

        method, resourceName, content = parsed


        if resourceName in self.content.keys():
            httpCode = "200 OK"
            htmlBody = "<html><body>" + self.content[resourceName] \
                + "</body></html>"

        elif '?' in resourceName:
            recurso, resto = resourceName.split('?')
            _, contenido = resto.split('=')
            self.content[recurso] = contenido
            self.persiste
            httpCode = "200 OK"
            htmlBody = "<html><body>" + self.content[recurso] \
                + "</body></html>"
        elif method in ["PUT", "POST"]:
            import urllib.parse
            self.content[resourceName] = urllib.parse.unquote(content)              #Para que salgan los signos (+,?,¿,=,....)
            self.persiste()
            httpCode = "200 OK"
            htmlBody = "<html><body>" + self.content[resourceName] \
                + "</body></html>"
        else:
            httpCode = "200 OK"
            htmlBody = "<html><body>" + resourceName + " No esta. Lo puedes crear<br>" \
                "<form method='POST' action=''><input type='text' name='contenido'><input type='submit' value='Enviar'></form>" \
                + "</body></html>"
        return (httpCode, htmlBody)

    def persiste(self):
        fich = open('diccionario.txt', 'w')
        for element in self.content:
            fich.write(element + ":" + self.content[element] + "\n")
        fich.close()

    def toma(self):
        import os.path
        if os.path.infile('diccionario.txt'):
            fich =  open('diccinario.txt', 'r')
            for linea in fich.readlines():
                recurso, contenido = linea[:-1].split(": ")
                self.content[recurso] = contenido
            fich.close()

if __name__ == "__main__":
    testWebApp = contentApp("localhost", 1234)
