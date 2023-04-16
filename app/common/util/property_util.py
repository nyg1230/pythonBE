import yaml
import os

global prop

def get_prop(name = "", path = "", root = "", ext = "yml"):
    result = None
    try:
        full_path = f"{root}{path}{name}.{ext}"
        with open(full_path, "r", encoding="utf8") as f:
            result = yaml.safe_load(f)
    except Exception as e:
        print(e)
    return result

def get_value(key = None):
    result = None
    if (key is not None):
        result = prop.get(key)
    
    return result

def get_server(key = ""):
    server = get_value("server")
    return server if (key == "") else server.get(key)

name = os.environ.get("PD3_CONFIG_NAME", "application")
root = os.environ.get("PD3_CONFIG_ROOT", os.getcwd())
path = os.environ.get("PD3_CONFIG_PATH", "\\conf\\")
ext = os.environ.get("PD3_CONFIG_EXT", "yml")

try:
    print("propert load...")
    print(f"path - {root}{path}{name}.{ext}")
    prop = get_prop(name, path, root)
    print("propert load complete!")
except Exception as e:
    print("property load failed...")

try:
    profile = prop.get("profile")
    if (profile is not None):
        print(f"{profile} profile property load...")
        profile_name = f"{name}-{profile}"
        print(f"path - {root}{path}{profile_name}.{ext}")
        profile_prop = get_prop(profile_name, path, root)
        print("profile property load complete!")
        prop.update(profile_prop)
    else:
        print(f"profile not exist...")
except:
    print("profile property load failed...")
finally:
    del name
    del path
    del root
    del ext
