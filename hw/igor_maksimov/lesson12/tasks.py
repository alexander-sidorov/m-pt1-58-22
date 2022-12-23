


def get_schema(url:str)->dict:
    lib={}
    new_url = url  
    schema = url.split("://")[0]

    print(schema)
    lib.update({'schema': schema})
 
    user = url.split(":")[1].replace("//","")
    print(user)
    lib.update({"user": user})

    password = url.split(":")[2].split("@")[0]
    lib.update({"password": password})
  
    host = url.split(":")[2].split("@")[1]
    lib.update({"host": host})

    port = url.split(":")[3].split("/")[0]
    lib.update({"port":port})

    res = url.split("/")[3]
    lib.update({"resource": res})

    print(lib)
    return lib

get_schema("http://gena:password@localhost:1234/resource")   