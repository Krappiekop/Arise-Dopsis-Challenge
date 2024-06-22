import os
import random
import shutil

# Definieer de paden
input_dir = "Data/input/images_resized"
output_dir = "Data/input/images_resized_annotated"

# Controleer of de output directory bestaat, zo niet maak deze aan
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Krijg een lijst van alle bestanden in de input directory
all_files = os.listdir(input_dir)

# Filter alleen de bestanden die afbeeldingen zijn
image_files = [f for f in all_files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]

# Kies 50 willekeurige afbeeldingen
selected_files = random.sample(image_files, 50)

# Verplaats de geselecteerde bestanden naar de output directory
for file_name in selected_files:
    src_path = os.path.join(input_dir, file_name)
    dst_path = os.path.join(output_dir, file_name)
    shutil.move(src_path, dst_path)

print(f"{len(selected_files)} bestanden zijn verplaatst van {input_dir} naar {output_dir}.")
