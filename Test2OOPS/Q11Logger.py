class Logger:
    def log(self,message,compile=None):
        self.message=message
        if compile=='error':
            print(f"ERROR: {message}")
        elif compile=='warning':
            print(f"WARNING: {message}")
        elif compile=='info':
            print(f"INFO: {message}")
l=Logger()
l.log("ERROR in the code","error")
l.log("warning in the code","warning")
l.log("info in the code","info")