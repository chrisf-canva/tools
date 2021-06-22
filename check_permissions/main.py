# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import argparse
import subprocess


# Press the green button in the gutter to run the script.
def read_requested_permissions(android_manifest_file):
    permissions = []
    try:
        with open(android_manifest_file) as file:
            line = file.readline().strip()
            index = 0
            while line:
                # print(f'Line {index}: [{line}]')
                content = line.strip()
                print(f'content: {content}')
                if content.startswith("<uses-permission android:name="):
                    start: int = len("<uses-permission android:name=") + 1
                    end: int = content.rindex('"')
                    print(f'start: {start}, end: {end}')
                    permission = content[start:end]
                    print(f'permission {permission}')
                    permissions.append(permission)
                index += 1
                line = file.readline().strip()
    except Exception as e:
        print(e)
        raise
    finally:
        file.close()
    permissions.sort()
    print(f'{len(permissions)} permissions: ')
    print("\n".join(permissions))
    return permissions


def get_permissions_from_pm(permissions_getter):
    result = subprocess.Popen(permissions_getter.split(' '), stdout=subprocess.PIPE)
    # print(result)
    result = result.stdout.read().decode('utf-8').strip().split('\n')
    # print(f'{type(result)}')
    print("\n".join(result))
    return result


def check_permissions(requested_permissions, permissions_from_pm):
    print(f'unknown permission: ')
    for requested_permission in requested_permissions:
        # print(f'requested_permission: {requested_permission}')
        found = False
        for line in permissions_from_pm:
            found = found or line.find(requested_permission) > -1
        if not found:
            print(f'{requested_permission}')


parser = argparse.ArgumentParser(description='Test for argparse')
parser.add_argument('--androidmanifest', '-am', help='AndroidManifest.xml file 属性，必要参数', required=True)
parser.add_argument('--permissionsgetter', '-pf', help='command to get permissions file 属性，非必要参数', required=False)
args = parser.parse_args()

if __name__ == '__main__':
    androidManifestFile = args.androidmanifest
    permissionsGetter = args.permissionsgetter or 'adb shell pm list permissions -g'

    print(f"""
          AndroidManifest.xml file: {androidManifestFile}
          permissions getter file: {permissionsGetter}
          """)

    requested_permissions = read_requested_permissions(androidManifestFile)
    permissions_from_pm = get_permissions_from_pm(permissionsGetter)
    check_permissions(requested_permissions, permissions_from_pm)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
