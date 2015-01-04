#!/usr/bin/env python2

import time
import serial

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('--verbose', action='store_true',
    help="use verbose output")

group = parser.add_argument_group('serial')
group.add_argument('-d', '--device', default='/dev/ttyUSB0', 
    help="device path (default %(default)s)")
group.add_argument('-b', '--baud', metavar='BAUDRATE', type=int, default=9600, 
    help="device baud rate (default: %(default)s)")
group.add_argument('-t', '--timeout', default=0.1, 
    help="read timeout value (default: %(default)s)")

group = parser.add_argument_group('device')
group.add_argument('--restart', '--reset', action='store_true',
    help="restart device before taking action")

subparsers = parser.add_subparsers(dest='action',
    help="action to perform")

exec_subparser = subparsers.add_parser('exec',
    help="upload and execute file")
exec_subparser.add_argument('source',
    help="path to source file")

upload_subparser = subparsers.add_parser('upload',
    help="upload file to destination")
upload_subparser.add_argument('source',
    help="path to source file")
upload_subparser.add_argument('destination', nargs='?',
    help="path to destination")

delete_subparser = subparsers.add_parser('delete',
    help="delete file from device")
delete_subparser.add_argument('target',
    help="target of file deletion")

args = parser.parse_args()

com = serial.Serial(args.device, args.baud, timeout=args.timeout)

def read():
    buff = ""
    line = com.readline()
    while line:
        buff += line
        line = com.readline()
    return buff

def write(line):
    com.write("%s\r\n" % line.strip("\r\n"))
    time.sleep(0.25)

def write_file(src, dst):
    write("file.open('%s', 'w')" % dst)
    write("file.close()")
    write("file.open('%s', 'a+')" % dst)
    write("file.write([[")
    with open(src, 'rb') as f:
        for line in f:
            write(line)
    write("]])")
    write("file.close()")

if args.restart:
    write("node.restart()")
    read()
    time.sleep(3)

if args.action == 'delete':
    write("file.remove('%s')" % args.target)
elif args.action == 'upload':
    dst = args.destination or args.source
    write_file(args.source, dst)
    if args.verbose: print read()
    else: read()
elif args.action == 'exec':
    dst = "temp%s.lua" % int(time.mktime(time.gmtime()))
    write_file(args.source, dst)
    if args.verbose: print read()
    else: read()
    write("require \"%s\"" % dst.rstrip('.lua'))
    print read()
    write("file.remove('%s')" % dst)
    if args.verbose: print read()
    else: read()
    
com.close()
