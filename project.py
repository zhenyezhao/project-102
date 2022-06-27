import dropbox
class Transferdata:
    def __init__(self,access_token):
        self.access_token=access_token
    def uploadfile(self,source,destination):
        dpx=dropbox.Dropbox(self.access_token)
        file=open(source,'rb')
        dpx.file_upload(file.read(),destination)
def main():
    accesstoken='sl.BJx0Jz24I_Hp4zsLLwH_kcDYIe68ONwAPYNkSOW5qtVhJmz0Fw-6ggS9WY59K-Gw97hrfgittr1kTa_9oHWqsupryfDXRugw4LXnnaH5PzhZ_oVtdFuWxn-rbQ_EEvrYUEH0oEQ'
    transferdata=Transferdata(accesstoken)
    source=input('enter the file')
    destination=input('enter the dropbox path')
    transferdata.uploadfile(source,destination)
    print('file has to be moved to the destination')
if __name__ == '__main__':
    main()