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
    content = {'/': 'Root page',
               '/page': 'A page'
               }

    def parse(self, request):
        """Return the resource name (including /)"""

        return request.split(' ', 2)[1]

    def process(self, resourceName):
        """Process the relevant elements of the request.

        Finds the HTML text corresponding to the resource name,
        ignoring requests for resources not in the dictionary.
        """

        if resourceName in self.content.keys():
            httpCode = "200 OK"
            htmlBody = "<html><body>" + self.content[resourceName] \
                + "</body></html>"
        else:
            httpCode = "404 Not Found"
            htmlBody = "Not Found"
        return (httpCode, htmlBody)


if __name__ == "__main__":
    testWebApp = contentApp("localhost", 1234)
