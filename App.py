# from AppOpener import open, give_appnames
# import psutil
# from fast_autocomplete import AutoComplete

# def app_list():
#     appList = give_appnames()
#     appDict = {}

#     for app in appList:
#         appDict[app] = {}
#     return appDict

# def open_app(firstArg):
#     "Open an application."
#     print("Opening...")
#     appname = str(firstArg).lower()

#     appDict = app_list()

#     autoCompleteApp = AutoComplete(words=appDict)
#     search = autoCompleteApp.search(word=appname, max_cost=3, size=1)

#     try:
#         open(str(search))
#         return ("Successfully opened")
#     except:
#         return ("Failed")

# def close_app(firstArg):
#     print("Closing...")
#     app_name = str(firstArg)

#     running_apps=psutil.process_iter(['pid','name']) #returns names of running processes
#     found=False
#     for app in running_apps:
#         sys_app=app.info.get('name').split('.')[0].lower()

#         if sys_app in app_name.split() or app_name in sys_app:
#             pid=app.info.get('pid') #returns PID of the given app if found running
            
#             try: #deleting the app if asked app is running.(It raises error for some windows apps)
#                 app_pid = psutil.Process(pid)
#                 app_pid.terminate()
#                 found=True
#             except: pass
            
#         else: pass
#     if not found:
#         return(app_name+" not found running")
#     else:
#         return(app_name+' closed')
    
            

# if __name__ == '__main__':
#     print(app_list())