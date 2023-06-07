import requests
import datetime
import random
import json
from tkinter import filedialog
from tkinter.messagebox import askyesno, showinfo
# Javascript to get onlyinfo
# Array.from(document.querySelectorAll(".b-photos__item__img")).map(img => img?.src)
# const d = new Set()
data_file = open("data/alina.json")
urls = json.load(data_file)

IMAGES_PREFIX = "alina_rose"
# result_dir = "D:\\totig\\totig\\Imagenes\\Only\\alina_rose"
result_dir = f"C:\\Users\\ricar\\OneDrive\\Imágenes\\Only\\{IMAGES_PREFIX}"

def save_image(image_content, dir, name):
    with open(dir + f"\\{IMAGES_PREFIX}-{name}.jpg", 'wb') as img:
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
    showinfo("El resultado será", f"Origen (Json): {data_file}\n" + f"Resultado: {data_file}")
    data_file = open(data_file.name)
    urls = json.load(data_file)

    for url in urls:
        try:
            response = requests.get(url, stream=True, allow_redirects=True)
            image_content = response.content
            save_image(image_content, result_dir, str(datetime.datetime.now().time().microsecond + random.random() *100))
        except: 
            print("Error")

    repeat = askyesno("Proceso completado","¿Desea realizar otra descarga?")

    if repeat: 
        main()

main()