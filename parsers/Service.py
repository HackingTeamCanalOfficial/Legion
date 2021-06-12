#!/usr/bin/python

__author__ = 'yunshu(wustyunshu@hotmail.com)'
__version__ = '0.2'
__modified_by = 'ketchup'


class Service:
    extrainfo: str = ''
    name: str = ''
    product: str = ''
    fingerprint: str = ''
    version: str = ''

    def __init__(self, ServiceNode):
        self.extrainfo = ServiceNode.getAttribute('extrainfo')
        self.name = ServiceNode.getAttribute('name')
        self.product = ServiceNode.getAttribute('product')
        self.fingerprint = ServiceNode.getAttribute('servicefp')
        self.version = ServiceNode.getAttribute('version')
