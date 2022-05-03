import yaml
from pathlib import Path
from utils import getDownloadLink

def buildRule(rules, ruleSets):
    res = ""
    for r in rules:
        name = r['name']
        res += "# Rule {} \n".format(name)
        if name not in ruleSets:
            raise KeyError("Rule {} cannot be find in global set".format(name))
        
        for file in ruleSets[r]["files"]:
            t = file['type']
            link = getDownloadLink(file)
            policy = None
            if "policy" in r:
                policy = r['policy']
            elif "suggested_policy" in file:
                policy = file['suggested_policy']
            else:
                raise KeyError("Undefined policy for {}".format(name))
            
            res += "{},{},{}\n".format(t, link, policy)
    return res

try:
    sourceFile = open("./source.yaml", "r")
    source = yaml.safe_load(sourceFile)
    targetFile = open('./target.yaml', "r")
    target = yaml.safe_load(targetFile)
except yaml.YAMLError as exc:
    print(exc)

bd = target['build_directory']
template = Path(target['base_template']).read_text()

for n, v in target['targets']:
    with open("{}/{}.conf".format(bd,n), "w") as f:
        conf = template.format(buildRule(v['rules']))
        f.write(conf)
    