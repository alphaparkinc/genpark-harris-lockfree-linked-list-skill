from client import HarrisList

def main():
    print("=== Testing Harris Lock-Free Linked List ===")
    hlist = HarrisList()
    hlist.insert(10, "Alpha")
    hlist.insert(20, "Beta")
    hlist.insert(15, "Gamma")

    print("Find 15:", hlist.find(15))
    assert hlist.find(15) == "Gamma"

    deleted = hlist.delete(15)
    print("Deleted 15:", deleted)
    assert deleted
    assert hlist.find(15) is None
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
