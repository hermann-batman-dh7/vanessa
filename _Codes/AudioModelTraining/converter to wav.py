import os
from pydub import AudioSegment

def convert_aac_to_wav(input_folder, output_folder):
    # Verifique se a pasta de saída existe, se não, crie-a
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Percorra todos os arquivos na pasta de entrada
    for filename in os.listdir(input_folder):
        if filename.endswith(".aac"):
            file_path = os.path.join(input_folder, filename)
            
            # Carregue o arquivo .aac usando pydub
            audio = AudioSegment.from_file(file_path, format="aac")
            
            # Gere o nome do arquivo de saída com extensão .wav
            output_filename = os.path.splitext(filename)[0] + ".wav"
            output_path = os.path.join(output_folder, output_filename)
            
            # Salve o arquivo convertido em .wav
            audio.export(output_path, format="wav")
            print(f"Arquivo convertido: {output_filename}")

if __name__ == "__main__":
    # Especifique a pasta de entrada e a pasta de saída
    input_folder_path = "C:/Users/Rossz/Documents/GitHub/vanessa/Assets/part1"
    output_folder_path = "C:/Users/Rossz/Documents/GitHub/vanessa/Assets/part1conv"

    convert_aac_to_wav(input_folder_path, output_folder_path)
