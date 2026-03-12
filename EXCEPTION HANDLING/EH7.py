try:
    data={"id":101,"name":"Amit"}
    print(data["salary"])
except KeyError:
    print("Key Not Found.")