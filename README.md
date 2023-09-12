<h1>$\color{green}MetaPDFModifier$ for Python</h1>

<h2>Logiciel exécutable via Python et permettant la modification rapide des métadonnées d'un fichier PDF.</h2>

[Télécharge le zip du logiciel ici](https://github.com/valuthringer/MetaPDFModifier/archive/refs/heads/main.zip)

<br>
<h2>Quelles métadonnées peuvent-être modifiées ?</h2>
<ul>
  <li>Le titre du document</li>
  <li>L'auteur du document</li>
  <li>La date de création du document</li>
  <li>La date de modification du document</li>
  <li>Le logiciel utilisé pour éditer le document</li>
</ul>

<h2>Comment installer le logiciel ?</h2>
<p>Veiller à ce que PYTHON soit installé sur le PC :</p>
<ul>
  <li>Windows 10/11 : https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5</li>
  <li>Versions antérieures de Windows : https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe</li>
</ul>
<p>Une fois Python installé, ouvrir le Powershell et taper les commandes suivantes :</p>
<ul>
  <li><code>pip install pikepdf</code></li>
  <li><code>pip install pytz</code></li>
</ul>
<p>Le logiciel est ainsi installé !</p>

<h2>Comment utiliser le logiciel ?</h2>
<p>Ouvrir avec un éditeur de texte le fichier <code>change_metadata_pdf.py</code> et modifier les lignes souhaitées :</p>
<ul>
  <li><code>pdf_file_path = 'chemin_du_pdf_a_modifier'</code></li>
  <li><code>pdf_info['/Title'] = "votretitre"</code></li>
  <li><code>pdf_info['/Author'] = "auteur"</code></li>
  <li>...</li>
</ul>
<p>Enregistrer le fichier et fermer l'éditeur de texte.</p>
<p>Exécuter <code>start.bat</code></p>
<h3>⚠️ Veiller à ne pas toucher le reste, cela évitera de devoir retélécharger le logigiciel...</h3>


<br>
<h3>by Valentin Luthringer</h3>
