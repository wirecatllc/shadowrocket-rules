def getDownloadLink(file, target):
    if "github" not in file:
        return file['file']
    
    if target == "github":
        return "https://raw.githubusercontent.com/{}/{}/{}".format(file['github']['repo'], file['github']['branch'], file['file'])
    elif target == "jsdelivr":
        return "https://cdn.jsdelivr.net/gh/{}@{}/{}".format(file['github']['repo'], file['github']['branch'], file['file'])
    
    return None