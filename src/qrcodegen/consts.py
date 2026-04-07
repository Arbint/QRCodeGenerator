import os
from pathlib import Path
from enum import Enum

def GetPrjDirRelative():
    scriptFilePath = os.path.abspath(__file__)
    moduleDir = os.path.dirname(scriptFilePath)
    srcDir = os.path.dirname(moduleDir)
    prjDir = os.path.dirname(srcDir)
    return os.path.normpath(prjDir) 

def GetPrjDirByPyprojectToml():
    current = Path(__file__).resolve()
    for parent in [current] + list(current.parents):
        if(parent/"pyproject.toml").is_file():
            return parent

    raise FileNotFoundError(f"trying to resolve the project root path by looking for the directory that contains the pyproject.toml file, but cannot find one")

def GetPrjDir():
    try:
        return GetPrjDirByPyprojectToml()
    except FileExistsError as e:
        print(f"{e}, trying to now use the relative path to find the root dir")
        return GetPrjDirRelative()

def GetScriptsDir():
    return os.path.join(GetPrjDir(), "scripts")

def GetAssetDir():
    return os.path.join(GetPrjDir(), "assets")

def GetOutputDir():
    prjDir = GetPrjDir() 
    outputDir = os.path.normpath(os.path.join(prjDir, "output"))
    if not os.path.exists(outputDir):
        os.mkdir(outputDir)

    return outputDir



