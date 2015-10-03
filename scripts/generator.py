#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
import os
import glob
import argparse
import catkin_pkg.packages

PACKAGE_CONTENT = r"""{package}
{line}

.. contents:: Contents:
   :local:

Summary
*******

.. ros:autopackage:: {package}
"""

TYPES_HEADER = r"""
Types
*****
"""

TYPE_HEADER = r"""
{type_name} types
{line}######

"""

TYPE_LIST = r"""* :ros:{type_file}:`{object_name}`
"""

TYPE_CONTENT = r"""
.. ros:auto{type_name}:: {object_name}
   :raw: tail
"""

def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="generator")
    parser.add_argument('rosdisto')
    parser.add_argument('dest')
    args = parser.parse_args(argv)
    ros_base_path = '/opt/ros/{0}/share'.format(args.rosdisto)
    packages = catkin_pkg.packages.find_packages(ros_base_path)
    for package_path, package in packages.items():
        rst_file_path = os.path.join(args.dest, package.name + '.rst')
        if not os.path.exists(rst_file_path):
            with open(rst_file_path, 'w') as fout:
                fout.write(PACKAGE_CONTENT.format(package=package.name,
                                                  line='+'*len(package.name)))
                types = [('message', 'msg'),
                        ('service', 'srv'),
                        ('action', 'action')]
                type_objects = {}
                for type_name, type_file in types:
                    object_files = glob.glob(os.path.join(ros_base_path, package_path, type_file, '*.' + type_file))
                    if object_files:
                        type_objects[type_name] = []
                        for object_file in object_files:
                            type_objects[type_name].append(os.path.basename(object_file).split('.')[0])
                if type_objects:
                    if 'action' in type_objects:
                        for action_name in type_objects['action']:
                            action_object = [action_name + suffix for suffix in
                                             ('Action', 'Goal', 'Feedback', 'Result',
                                              'ActionGoal', 'ActionFeedback', 'ActionResult')]
                            type_objects['message'] = [object_name for object_name in type_objects['message']
                                                       if object_name not in action_object]
                    fout.write(TYPES_HEADER)
                    for type_name, type_file in types:
                        if type_name in type_objects and type_objects[type_name]:
                            fout.write(TYPE_HEADER.format(type_name=type_name.title(),
                                                          line='#'*len(type_name)))
                            for obj in type_objects[type_name]:
                                fout.write(TYPE_LIST.format(type_file=type_file,
                                                               object_name=package.name + '/' + obj))
                            for obj in type_objects[type_name]:
                                fout.write(TYPE_CONTENT.format(type_name=type_name,
                                                               object_name=package.name + '/' + obj))

if __name__=='__main__':
    main()
