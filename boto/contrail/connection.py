#-----------------------
# This derived from aws connection handling boto.connection
# while current implementation of connection to contrail ws doesn't
# require most of the aws parameters, inherited classes provides wrapper
# for contrail to aws connection map
# boto.contrail packages should use this connection
# classes and methods renamed for contrail and some method redefinition
# needs to be done. WIP
#--------------------

# Parts of this code were copied or derived from github.com/boto/boto
# The following notice applies to that code.

# Copyright (c) 2006-2012 Mitch Garnaat http://garnaat.org/
# Copyright (c) 2012 Amazon.com, Inc. or its affiliates.
# Copyright (c) 2010 Google
# Copyright (c) 2008 rPath, Inc.
# Copyright (c) 2009 The Echo Nest Corporation
# Copyright (c) 2010, Eucalyptus Systems, Inc.
# Copyright (c) 2011, Nexenta Systems Inc.
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# Parts of this code were copied or derived from sample code supplied by AWS.
# The following notice applies to that code.
#
#  This software code is made available "AS IS" without warranties of any
#  kind.  You may copy, display, modify and redistribute the software
#  code either by itself or as incorporated into your code; provided that
#  you do not remove any proprietary notices.  Your use of this software
#  code is at your own risk and you waive any claim against Amazon
#  Digital Services, Inc. or its affiliates with respect to your use of
#  this software code. (c) 2006 Amazon Digital Services, Inc. or its
#  affiliates.

"""
Handles basic connections to Contrail WS
"""

from boto.connection import HostConnectionPool, ConnectionPool, HTTPRequest, HTTPResponse, AWSAuthConnection, AWSQueryConnection



class CWSAuthConnection(AWSAuthConnection):
    def __init__(self, host, aws_access_key_id=None,
                 aws_secret_access_key=None,
                 is_secure=True, port=None, proxy=None, proxy_port=None,
                 proxy_user=None, proxy_pass=None, debug=0,
                 https_connection_factory=None, path='/',
                 provider='cws', security_token=None,
                 suppress_consec_slashes=True,
                 validate_certs=True):
        """
        :type host: str
        :param host: The host to make the connection to

        :keyword str aws_access_key_id: Your AWS Access Key ID (provided by
            Amazon). If none is specified, the value in your
            ``AWS_ACCESS_KEY_ID`` environmental variable is used.
        :keyword str aws_secret_access_key: Your AWS Secret Access Key
            (provided by Amazon). If none is specified, the value in your
            ``AWS_SECRET_ACCESS_KEY`` environmental variable is used.

        :type is_secure: boolean
        :param is_secure: Whether the connection is over SSL

        :type https_connection_factory: list or tuple
        :param https_connection_factory: A pair of an HTTP connection
            factory and the exceptions to catch.  The factory should have
            a similar interface to L{httplib.HTTPSConnection}.

        :param str proxy: Address/hostname for a proxy server

        :type proxy_port: int
        :param proxy_port: The port to use when connecting over a proxy

        :type proxy_user: str
        :param proxy_user: The username to connect with on the proxy

        :type proxy_pass: str
        :param proxy_pass: The password to use when connection over a proxy.

        :type port: int
        :param port: The port to use to connect

        :type suppress_consec_slashes: bool
        :param suppress_consec_slashes: If provided, controls whether
            consecutive slashes will be suppressed in key paths.

        :type validate_certs: bool
        :param validate_certs: Controls whether SSL certificates
            will be validated or not.  Defaults to True.
        """
        AWSAuthConnection.__init__(self, host, aws_access_key_id,
                                   aws_secret_access_key, is_secure, port, proxy,
                                   proxy_port, proxy_user, proxy_pass, debug, https_connection_factory,
                                   path, provider, security_token, suppress_consec_slashes, validate_certs)


   

class CWSQueryConnection(CWSAuthConnection):

    APIVersion = ''
    ResponseError = BotoServerError

    def __init__(self, aws_access_key_id=None, aws_secret_access_key=None,
                 is_secure=True, port=None, proxy=None, proxy_port=None,
                 proxy_user=None, proxy_pass=None, host=None, debug=0,
                 https_connection_factory=None, path='/', security_token=None,
                 validate_certs=True):
        CWSAuthConnection.__init__(self, host, aws_access_key_id,
                                   aws_secret_access_key,
                                   is_secure, port, proxy,
                                   proxy_port, proxy_user, proxy_pass,
                                   debug, https_connection_factory, path,
                                   security_token=security_token,
                                   validate_certs=validate_certs)