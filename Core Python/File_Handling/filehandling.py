try:
    with open("w.txt") as f2:
        pass
except:
    print("File not available")
else:
    f2.close()
    #f3.close()
    print("File closed")