import requests
import datetime
import random
import json
from tkinter import filedialog
from tkinter.messagebox import askyesno, showinfo
# Javascript to get onlyinfo
# Array.from(document.querySelectorAll(".b-photos__item__img")).map(img => img?.src)
# const d = new Set()
# data_file = open("data/alina.json")
# urls = json.load(data_file)

# IMAGES_PREFIX = "alina_rose"
# # result_dir = "D:\\totig\\totig\\Imagenes\\Only\\alina_rose"
# result_dir = f"C:\\Users\\ricar\\OneDrive\\Imágenes\\Only\\{IMAGES_PREFIX}"

def save_image(image_content, dir, name, image_prefix):
    with open(dir + f"\\{image_prefix}-{name}.jpg", 'wb') as img:
        img.write(image_content)

def main():
        # unique_urls = set(urls)
    # data_file = input("Introduzca la fuente de descarga (una lista json con los urls que desea)")
    data_file = filedialog.askopenfile("r")
    result_dir = filedialog.askdirectory()
    if not data_file or not result_dir: 
        finished = askyesno("Los datos introducidos no son validos","¿Desea salir?")
        if finished: return
        return main()
    showinfo("El resultado será", f"Origen (Json): {data_file.name}\n" + f"Resultado: {result_dir}")
    data_file = open(data_file.name)
    urls = json.load(data_file)
    image_prefix = result_dir.split("\\")[0].split("/")[-1]

    for url in urls:
        try:
            response = requests.get(url, stream=True, allow_redirects=True)
            image_content = response.content
            save_image(image_content, result_dir, str(datetime.datetime.now().time().microsecond + random.random() *100), image_prefix)
        except Exception as e: 
            print("Error", e)
            
    showinfo("Proceso completado")
    repeat = askyesno("Proceso completado","¿Desea realizar otra descarga?")
    print(repeat)
    if repeat: 
        main()

main()