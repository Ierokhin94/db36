#! /usr/bin/env python
# -*-coding: utf-8-*-
import sys, libxml2

import optparse

def validate(xml_mephi, dtd_mephi):
  doc = libxml2.parseFile(xml_mephi)
  dtd = libxml2.parseDTD(None, dtd_mephi)
  ctxt = libxml2.newValidCtxt()
  ret = doc.validateDtd(ctxt, dtd)
  dtd.freeDtd()
  doc.freeDoc()
  return ret
def main():
  op = optparse.OptionParser(description = U"Проверка на соответствие DTD",prog="dtd",version="0.1", usage=U"%prog")
  op.add_option("-x", "--xml", dest="xml", help=U"XML документ", metavar="XML_FILE")
  op.add_option("-d", "--dtd", dest="dtd", help=U"DTD документ", metavar="DTD_FILE")

  options, arguments = op.parse_args()
  if options.xml and options.dtd:
    validate(options.xml, options.dtd)
  else: 
  	op.print_help()

if __name__ == '__main__':
  main()
