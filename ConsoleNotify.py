from win10toast import ToastNotifier

def notify(address):
    toaster = ToastNotifier()
    toaster.show_toast("Bitcoin Address Alert: "+ address, "Notification Data of Something ")
