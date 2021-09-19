import dropbox
class Transfer:
    def __init__(self,accesstoken):
        self.accesstoken=accesstoken
    def upload(self,froms,to):
        db=dropbox.Dropbox(self.accesstoken)
        f=open(froms,"rb")
        db.files_upload(f.read(),to)
froms=input("Enter The File You Want To Transfer: ")
to=input("Enter the Upload Path: ")
transfer=Transfer("qjUzxwYYxqkAAAAAAAAAAYyAXdtdMH5ghhFICbmD3NQXr2tuAaki91H6YTSCV_Lq")
transfer.upload(froms,to)
print("done")