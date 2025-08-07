import requests

while True:
    
    url = "https://jsonplaceholder.typicode.com/"

    print("""\n
    BIENVENIDO A LA INTERFAZ DE CONSUMO DE LA API JSONPLACEHOLDER
        
        1. Listar títulos de posts del usuario con userId=1
        2. Añadir post
        3. Actualizar post
        0. Terminar ejecución
        \n\n
    """)
    m = int(input("> "))
    if m == 0:
        break

    elif m == 1:
        
        query = url + "posts?userId=1"
        response = requests.get(query)
        if response.status_code == 200:
            data = response.json()
            for post in data:
                print(post["title"])
        else:
            print("Error durante la ejecución de la consulta")
    
    elif m == 2:
        title = input("Ingrese el título de su nuevo post: ")
        content = input("Ingrese el contenido de su neuvo post: ")

        query = url + "posts"

        body = {
            "userId" : 1,
            "title" : title,
            "body" : content
        }

        response = requests.post(query, json=body)

        if response.status_code == 201:
            print("Post agregado correctmente.")
        else:
            print("Ocurrió un fallo al agregar el post")

    elif m == 3:
        title = input("Ingrese el título del recurso a actualizar: ")
        new_title = input("Ingrese el nuevo título: ")

        query = url + "posts/1?" + title

        body = {"title" : new_title}

        response = requests.put(query, json=body)

        print(response.status_code)

        if response.status_code == 200:
            print("Título del post actualizado correctmente.")
        else:
            print("Ocurrió un fallo al agregar el post")

