#ALUVIUM
#SSH CLI for mass coping data from Linux server to Windows
import paramiko
import os
import posixpath
#----00000000000---------00000000000-----------0000000000000---------MASSDATA-COPPY
#----FROM REMOTE-SERVER USING SSHELL-----------------------------------------------

def check_dict(sftp):
    print(sftp.getcwd())
    print(sftp.listdir())
    #print(dir(sftp))
    return None
#-------------------------------------------------BASIC CHECK WHERE WE ARE IN SEVER
def working_dict(sftp):
    wanted_dic=input('Please provide valid dir: ')
    sftp.chdir(wanted_dic)
    print(print(sftp.getcwd()))
    print(sftp.listdir())
#I can add -is dictionary check here later!
    return None
#-------------------------------------------------PROVIDING VALID PATH FOR CP FILES
def cp_files(sftp):
    c=input("Do u want copy all files from this folder?Press 'y' for confirmation. ")
    if c=='y':
        print('Copping files...\n')
        v_list=sftp.listdir()
        v_path=sftp.getcwd()
        out_path='D:\\tempo\\'
        for f in  v_list:
            full_p=posixpath.join(v_path,f)
            print(full_p)
            print(os.path.join(out_path,f))
            sftp.get(full_p, os.path.join(out_path,f))
        #print(f'\n{len(v_list)} files or folder were found')

# Isfile check would be good here!

    else:
        print('Bye,bye')
    return None
#--------------------------------------------------------COPPING FUN-------------
def main():
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#-------------------------------------------------------------PROVIDE VALID INFO
    ssh.connect(hostname='', username='', password='', port=22)
    sftp_cli=ssh.open_sftp()
    check_dict(sftp_cli)
    working_dict(sftp_cli)
    cp_files(sftp_cli)
    sftp_cli.close()
    ssh.close()
    print('\n\nSuccesfully finished bye,bye.')
    return None


if __name__=='__main__':
    main()
