#by Valentin Luthringer

import pikepdf
import sys
from datetime import datetime
import pytz
import os

#####################################
pdf_file_path = 'chemin_du_pdf_a_modifier' # Spécifiez le chemin du fichier PDF
#####################################

pdf = pikepdf.Pdf.open(pdf_file_path)
pdf_info = pdf.docinfo
print("Métadonnées actuelles :")
for key, value in pdf_info.items():
    print(key, ':', value)

current_datetime = datetime.now(pytz.utc)
formatted_date = current_datetime.strftime("D:%Y%m%d%H%M%S")
pdf_file_name_without_extension = os.path.splitext(os.path.basename(pdf_file_path))[0]

######################################
pdf_info['/Title'] = "votretitre"   #pdf_file_name_without_extension  #REMPLACER ICI PAR LE NOM DU FICHIER VOULU
#pdf_info['/CreationDate'] = 'D:20230911094501' #format : D:AnnéeMoisJourHeureMinutesSecondes (pour la date de création du fichier)
pdf_info['/ModDate'] = formatted_date #format : D:AnnéeMoisJourHeureMinutesSecondes   (pour la date de modification du fichier)
pdf_info['/Producer'] = "VL SOFT"  # (pour le nom de l'outil de conversion PDF)
pdf_info['/Author'] = "auteur"  # (pour l'auteur)
#pdf_info['/Creator'] = "VL SOFT"  # (pour le logiciel)

######################################

modified_file_name = pdf_file_name_without_extension + '_modifié.pdf'
pdf.save(modified_file_name)
print(f"\nLe champ 'Title' a été modifié, et le PDF a été sauvegardé sous {modified_file_name}.")
