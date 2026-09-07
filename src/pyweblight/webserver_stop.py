#!/usr/bin/env python

"""
Stop the webserver
"""

import http.client

port = 8001


def main():
    conn = http.client.HTTPConnection(f"localhost:{port}")
    conn.request("QUIT", "/")
    print(conn.getresponse())


if __name__ == "__main__":
    # Only contact the server when run as a script. Importing this module --
    # which sphinx autodoc, pytest and any consumer does -- must not send QUIT.
    main()
