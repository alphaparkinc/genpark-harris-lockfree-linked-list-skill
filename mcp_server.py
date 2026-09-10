import sys
import json
from client import HarrisList

def main():
    hlist = HarrisList()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "insert":
            ok = hlist.insert(params.get("key"), params.get("value"))
            res = {"inserted": ok}
        elif method == "find":
            val = hlist.find(params.get("key"))
            res = {"value": val}
        elif method == "delete":
            ok = hlist.delete(params.get("key"))
            res = {"deleted": ok}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
