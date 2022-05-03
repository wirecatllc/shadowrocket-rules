import yaml

try:
    sourceFile = open("./source.yaml", "r")
    source = yaml.safe_load(sourceFile)
    targetFile = open('./target.yaml', "r")
    target = yaml.safe_load(targetFile)
except yaml.YAMLError as exc:
    print(exc)
