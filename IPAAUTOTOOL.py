import git
import os
import shutil
import subprocess
import commands
def main():
    tool_path = os.getcwd()
    path = os.path.expanduser('~') + "/Desktop/IPAAUTOTEMP"
    if os.path.exists(path):
        shutil.rmtree(path)
    """ git """
    git.Repo.clone_from(url='git@github.com:LiFaNSuperMan/LFSocketHelper.git', to_path=path,b="master")
    print('clone git success')
    """ judge podfile"""
    podfile_path = path + '/Podfile'
    if os.path.exists(podfile_path):
        os.chdir(path)
        print("podfile is exits , execute pod")
        podcmd = 'pod update --no-repo-update'
        process = subprocess.Popen(podcmd,shell=True)
        process.wait()
        code = process.returncode
        if code != 0:
            print 'TODO: except'
        f = os.popen('xcodebuild -list')
        print f.readlines()
        # (status, output) = commands.getoutput('xcodebuild -list')
        # print status, output
        os.chdir(tool_path)
    exportOption = open('exportOption.plist','w')

    teamID = '9GZ45VG9NP'
    method = 'development'
    provisionFileBundleID = 'podTest'
    dic = {'teamID': teamID , 'method':method , 'provisionFileBundleID' : provisionFileBundleID}
    plistfile_content='''<?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
    <plist version="1.0">
    <dict>
        <key>compileBitcode</key>
        <false/>
        <key>method</key>
        <string>{method}</string>
        <key>signingStyle</key>
        <string>automatic</string>
        <key>stripSwiftSymbols</key>
        <true/>
        <key>teamID</key>
        <string>{teamID}</string>
        <key>thinning</key>
        <string>none</string>
    </dict>
    </plist>
    '''.format(**dic)
    exportOption.write(plistfile_content)







if __name__ == "__main__":
    main()
