#!/usr/bin/python
# -*- coding: UTF-8 -*-

import argparse
import os
import re


def action(body):
    lo = repr(body).lower()
    lo = re.sub(r'[^A-Za-z0-9 ]', '', lo)
    lo = re.sub(r'[ ]', '-', lo)
    branch_name = "chrisf-canva/{}".format(lo)
    print(f"the body is {branch_name}")
    return branch_name


def create(branch_name, based_branch):
    if based_branch is None:
        based_branch = "origin/master"
    os.system('git checkout -b {} {}'.format(branch_name, based_branch))


parser = argparse.ArgumentParser(description='Test for argparse')
parser.add_argument('--body', '-b', help='body 属性，必要参数', required=True)
parser.add_argument('--branch', '-br', help='based branch 属性，非必要参数', required=False)
args = parser.parse_args()

if __name__ == '__main__':
    try:
        branch = action(args.body)
        create(branch, args.branch)
    except Exception as e:
        print(e)
