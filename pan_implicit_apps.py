#!/usr/bin/env python3
#
#  AUTHOR: Brad Atkinson
#    DATE: 11/10/2021
# PURPOSE: A script for finding app dependencies for a given App-ID

import sys
import argparse
from panos import base
import config


def connect_device():
    """Connect To Device

    Returns:
        fw_conn (PanDevice): A panos object for device
    """
    fw_ip = config.paloalto['fw_ip']
    username = config.paloalto['username']
    password = config.paloalto['password']
    try:
        fw_conn = base.PanDevice.create_from_device(
            hostname=fw_ip,
            api_username=username,
            api_password=password)
        return fw_conn
    except:
        print('Host was unable to connect to device. Please check '
              'connectivity to device.\n', file=sys.stderr)
        sys.exit(1)


def get_implicit_apps(fw_conn, app_id):
    """Get Implicit Applications

    Args:
        fw_conn (PanDevice): A panos object for device
        app_id (str): A string with the app-id

    Returns:
        results (Element): XML results from firewall
    """
    xpath = ("/predefined/application/entry[@name='{}']".format(app_id))
    results = fw_conn.op(cmd="<show><predefined><xpath>{}</xpath></predefined></show>".format(xpath), cmd_xml=False)
    return results


def process_implicit_apps(results):
    """Process Implicit Apps

    Args:
        results (Element): XML results from firewall

    Returns:
        implicit_app_list (list): A list of implicit apps
    """
    try:
        xml_list = results.findall('./result/entry/implicit-use-applications/member')
        implicit_app_list = []
        for app in xml_list:
            app_id = app.text
            implicit_app_list.append(app_id)
        return implicit_app_list
    except AttributeError:
        implicit_app_list = []
        return implicit_app_list


def main():
    """Function Calls
    """
    parser = argparse.ArgumentParser(description='To get implicit applications')
    parser.add_argument('-a', '--app',
                        type=str,
                        metavar='',
                        required=True,
                        help='The app to check')
    args = parser.parse_args()

    fw_conn = connect_device()
    results = get_implicit_apps(fw_conn, args.app)
    implicit_app_list = process_implicit_apps(results)
    
    if implicit_app_list:
        print("\nThe App-ID of '{}' has the following dependencies:\n".format(args.app))
        for app in implicit_app_list:
            print(app)
        print('\r')
    else:
        print("\nThe App-ID of '{}' has no app dependencies.\n".format(args.app))


if __name__ == '__main__':
    main()
