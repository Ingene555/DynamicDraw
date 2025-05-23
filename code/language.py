import locale
import pickle as pkl
import os

def writeFile(data, file):
    with open(file, 'wb') as f:
        pkl.dump(data, f)

def readFile(file):
    with open(file, 'rb') as f:
        return pkl.load(f)


if os.path.exists('language.ini'):
        try:
            a=readFile('language.ini')
            lang=a if a in ['fr', 'en'] else 'en'
        except Exception as e:
            langue_systeme, encoding = locale.getdefaultlocale()
            lang=langue_systeme.split('_')[0] if langue_systeme.split('_')[0] in ['fr', 'en'] else 'en'
            writeFile(lang, "language.ini")
else:
    langue_systeme, encoding = locale.getdefaultlocale()
    lang=langue_systeme.split('_')[0] if langue_systeme.split('_')[0] in ['fr', 'en'] else 'en'
    writeFile(lang, 'language.ini')


dicoFR={
    'copy': 'Copier',
    'copy index': 'Copier le code point Unicode',
    'insert': 'Inserer',
    'close': 'Fermer',
    'copy all': "Copier tout",
    'export all': 'Tout exporter',
    'group': 'Groupe',
    'angle': 'Angle',
    'fill':'Couleur',
    'dash': 'Tiret',
    'title': 'Titre',
    'scale': 'Echelle',
    'text':'Texte',
    'image':'Image',
    'fill': 'Couleur',
    'outline':'Contour',
    'start':'Debut',
    'extent':'Fin',
    'width': 'Epaisseur',
    'family':'Police',
    'weight':'Gras',
    'italic':'Italique',
    'underline':'Souligner',
    'overstrike':'Barrer',
    'height':'Hauteur',
    'long':'Longueur',
    'dash offset': 'Decalage',
    'first':'Debut',
    'last': 'Fin',
    'both':'Tout',
    'none':'Aucun',
    'arrow':'Fleche',
    'cap':'Bout',
    'join': 'Jointure',
    'butt':'Bout',
    'round':'Rond',
    'projecting':'Sallie',
    '':'Aucun',
    'miter':'Mitre',
    'bevel':'Biseau',
    'spline steps':'Lissage',
    'smooth':'Lisse',
    'center':'Centre',
    'e':'E',
    'en':'EN',
    'es':'ES',
    'n':'N',
    'ne':'NE',
    'nw':'NO',
    's':'S',
    'se':'SE',
    'sw':'SO',
    'w':'O',
    'wn':'ON',
    'ws':'OS',
    'anchor':'Ancrage',
    'left':'Gauche',
    'right':'Droite',
    'justify':'Allignement',
    'style':'Style',
    'pieslice':'Part',
    'chord':'Corde',
    'arc':'Arc',
    'window':'Widget',
    'stipple':'pointillé',
    'gray25':'Gray25',
    'gray50':'Gray50',
    'gray75':'Gray75',
    'size':'Taille',
    'select an image': 'Sectionnez une image',
    'choose a color': 'Choisissez une couleur',
    'erase':'Effacer',
    'button':'Bouton',
    'checkbutton':'Bouton à cocher',
    'entry': 'Champ d\'entrée',
    'frame': 'Frame',
    'label': 'Label',
    'labelframe': 'Cadre de label',
    'listbox': 'Liste',
    'menubutton': 'Bouton menu',
    'message': 'Message',
    'radiobutton': 'Bouton radio',
    'scale': 'Échelle',
    'scrolledtext': 'Champ de saisie',
    'scrollableframe': 'Frame déroulant',
    'spinbox': 'Champ numérique',
    'activebackground': 'Fond actif',
    'activeforeground': 'Ecrit actif',
    'aspect':'Aspect',
    'border': 'Bordure',
    'background': 'Fond',
    'buttonbackground': 'Fond de bouton',
    'buttoncursor': 'Curseur de bouton',
    'foreground':'Couleur d\'ecriture',
    'flat': 'Plat',
    'raised':'Soulevé',
    'groove':'Rainure',
    'sunken': 'Creux',
    'ridge': 'Crête',
    'buttondownrelief':'Relief pressé',
    'buttonuprelief': 'Relief non pressé',
    'top':'Haut',
    'bottom':'Bas',
    'compound': 'Composé',
    'cursor':'Curseur',
    'direction': 'Direction',
    'below': 'En dessous',
    'above': 'Au dessus',
    'offrelief':'Relief inactif',
    'from': 'De',
    'to':'Vers',
    'highlightbackground':'Fond en évidence',
    'highlightcolor':'Ecrit en évidence',
    'highlightthickness':'Bordure en évidence',
    'indicatoron':'Indicateur',
    'insertbackground':'Fond d\'insertion',
    'insertborderwidth':'Bordure d\'insertion',
    'insertwidth':'Epaisseur d\'insertion',
    'labelanchor':'Ancre du label',
    'length':'longueur',
    'horizontal':'Horizontale',
    'vertical': 'Verticale',
    'orient':'Orientation',
    'overrelief':'Relief actif',
    'relief':'Relief',
    'selectbackground':'Fond de selection',
    'selectcolor': 'Couleur de selection',
    'selectborderwidth': 'Epaisseur de selection',
    'selectimage':'Image de slection',
    'show':'Affichage',
    'showvalue':'Afficher la Valeur',
    'sliderlength':'Longueur du slider',
    'sliderrelief':'Relief du slider',
    'label':'Label',
    'troughcolor':'Couleur du chemin',
    'wraplength':'longueur d\'enveloppe',
    'select':'Selectionner',
    'command type': 'Type de command',
    'separator':'Separateur',
    'lift':'En avant',
    'duplicate':'Dupliquer',
    'copy':'Copier',
    'past':'Coller',
    'mirror': 'Miroir',
    'edit':'edition',
    'delete':'Supprimer',
    'normal':'Normal',
    'all':'remplissage',
    'no color':'Noir-Blanc',
    'file':'Fichier',
    'new':'Nouveau',
    'open':'Ouvrir',
    'save':'Sauvegarder',
    'saveas':'Sauvegarder en',
    'exit':'Quitter',
    'render':'Rendu',
    'object':'Objet',
    'line':'Ligne',
    'polygon':'Polygone',
    'square':'Carre',
    'triangle': 'Triangle',
    'pentagon':'Pentagone',
    'hexagon':'Hexagone',
    'oval':'Oval',
    'arc':'Arc',
    'widget':'Widget',
    'text':'Texte',
    'option':'Option',
    'langue':'Langue',
    'new':'Nouveau',
    'thereisanotherworkinprogressdoyouwanttocreateanotherone':'Il y a un travail en cours,\nVoulez-vous en créer un autre ?',
    'error': 'Erreur',
    'unabletoreadfile':'Impossible de lire le fichier',
    'closing':'Fermeture',
    'doyouwanttosave':'Voulez-vous sauvegarder ?',
    'the program must restart to apply the change':'Le programme doit redémarrer pour appliquer le changement',
    'restart':'Redémarrage',
    'info':'Info',
    'the change will be applied on next startup':'Le changement sera appliqué au prochain démarrage',
    'sauvegarder l\'image sous':"Sauvegarder l'image sous",
    'cannotmovemorethantwoobjects':'Impossible de deplacer plus de deux objets',
    'more':'Plus',
    'convertisor':'Convertisseur',
    'help':'Aide',
    'action':'Action',
    'shortcut':'Raccourci',
    'undo':'Undo',
    'redo':'Redo',
    'setpoint':'Définir les points',
    'moveobject':'Deplacer l\'objet',
    'raccourci clavier':'Raccourci clavier'
}

dicoEN={
    'copy':'Copy',
    'copy index': 'Copy the Unicode code point',
    'insert': 'Insert',
    'close': 'Close',
    'copy all': 'Copy all',
    'export all': 'Export all',
    'group': 'Group',
    'angle': 'Angle',
    'fill': 'Fill',
    'dash':'Dash',
    'title':'Title',
    'scale': 'Scale',
    'text': 'Text',
    'image':'Image',
    'fill':'Fill',
    'outline':'Outline',
    'start':'Start',
    'extent':'Extent',
    'width':'Width',
    'family':'Family',
    'weight':'Weight',
    'italic':'Italic',
    'underline':'Underline',
    'overstrike':'Overstrike',
    'height':'Height',
    'long':'width',
    'dash offset': 'Dash offset',
    'first':'First',
    'last':'Last',
    'both':'Both',
    'none':'None',
    'arrow':'Arrow',
    'cap':'Cap',
    'join':'Join',
    'butt': 'Butt',
    'round':'Round',
    'projecting':'Projecting',
    '':'None',
    'miter':'Miter',
    'bevel':'Bevel',
    'smooth':'Smooth',
    'spline steps':'Spline steps',
    'center':'Center',
    'e':'E',
    'en':'EN',
    'es':'ES',
    'n':'N',
    'ne':'NE',
    'nw':'NW',
    's':'S',
    'se':'SE',
    'sw':'SW',
    'w':'W',
    'wn':'WN',
    'ws':'WS',
    'anchor':'Anchor',
    'left':'Left',
    'right':'Right',
    'justify':'Justify',
    'style':'Style',
    'pieslice':'Pieslice',
    'chord':'Chord',
    'arc':'Arc',
    'window':'Widget',
    'stipple':'Stipple',
    'gray25':'Gray25',
    'gray50':'Gray50',
    'gray75':'Gray75',
    'size':'Size',
    'select an image': 'Select an image',
    'choose a color': 'Choose a color',
    'erase':'Erase',
    'button': 'Button',
    'checkbutton': 'Check button',
    'entry': 'Input area',
    'frame': 'Frame',
    'label': 'Label',
    'labelframe':'Label frame',
    'listbox': 'List box',
    'menubutton': 'Menu button',
    'message': 'Message',
    'radiobutton': 'Radio button',
    'scale': 'Scale',
    'scrolledtext': 'Text area',
    'scrollableframe': 'Scrollable frame',
    'spinbox': 'Spin box',
    'activebackground': 'Active background',
    'activeforeground': 'Active foreground',
    'aspect':'Aspect',
    'border': 'Border',
    'background': 'Background',
    'buttonbackground': 'Button background',
    'buttoncursor': 'Button cursor',
    'foreground':'Foreground',
    'flat': 'Flat',
    'raised':'Raised',
    'groove':'Groove',
    'sunken': 'Sunken',
    'ridge': 'Ridge',
    'buttondownrelief':'Button down relief',
    'buttonuprelief': 'Button up relief',
    'top':'Top',
    'bottom':'Bottom',
    'compound': 'Compound',
    'cursor':'Cursor',
    'direction': 'Direction',
    'below': 'below',
    'above': 'Above',
    'offrelief':'Off relief',
    'from': 'From',
    'to':'To',
    'highlightbackground':'High light background',
    'highlightcolor':'High light color',
    'highlightthickness':'High light thickness',
    'indicatoron':'Indicatoron',
    'insertbackground':'Insert background',
    'insertborderwidth':'Insert border width',
    'insertwidth':'Insert width',
    'labelanchor':'Label anchor',
    'length':'length',
    'horizontal':'Horizontal',
    'vertical': 'Vertical',
    'orient':'Orient',
    'overrelief':'Over relief',
    'relief':'Relief',
    'selectbackground':'Select background',
    'selectcolor': 'Select color',
    'selectborderwidth': 'Select border width',
    'selectimage':'Select image',
    'show':'Show',
    'showvalue':'Show value',
    'sliderlength':'Slider length',
    'sliderrelief':'Slider relief',
    'label':'Label',
    'troughcolor':'Trough color',
    'wraplength':'Wrap length',
    'select':'Select',
    'command type': 'Type of command',
    'separator':'Separator',
    'lift':'Lift',
    'duplicate':'Duplicate',
    'copy':'Copy',
    'past':'Past',
    'mirror': 'Mirror',
    'edit':'Edit',
    'delete':'Delete',
    'normal':'Normal',
    'all':'fill',
    'no color': 'Black-White',
    'file':'File',
    'new':'New',
    'open':'Open',
    'save':'Save',
    'saveas':'Save as',
    'exit':'Exit',
    'render':'Render',
    'object':'Object',
    'line':'Line',
    'polygon':'Polygon',
    'square':'Square',
    'triangle': 'Triangle',
    'pentagon':'Pentagon',
    'hexagon':'Hexagon',
    'oval':'Oval',
    'arc':'Arc',
    'widget':'Widget',
    'text':'Text',
    'option':'Option',
    'langue':"Language",
    'new':'New',
    'thereisanotherworkinprogressdoyouwanttocreateanotherone':'There is another work in progress,\nDo you want to create another one ?',
    'error':'Error',
    'unabletoopenfile':'Unable to read file',
    'closing':'Closing',
    'doyouwanttosave':'Do you want to save ?',
    'restart':'Restart',
    'the program must restart to apply the change':'The program must restart to apply the change',
    'info':'Info',
    'the change will be applied on next startup':'The change will be applied on next startup',
    "sauvegarder l'image sous":"Save image as",
    'cannotmovemorethantwoobjects':'Cannot move more than two objects',
    'more':'More',
    'convertisor':'Convertisor',
    'help':'Help',
    'action':'Action',
    'shortcut':'Shortcut',
    'undo':'Undo',
    'redo':'Redo',
    'setpoint':'Set points',
    'moveobject':'Move objects',
    'raccourci clavier':'Keyboard shortcut'
}

dico_wdt={
    'button': 'Button',
   'checkbutton': 'Checkbutton',
   'entry': 'Entry',
   'frame': 'Frame',
   'label': 'Label',
   'labelframe': 'LabelFrame',
   'listbox': 'Listbox',
   'menubutton': 'Menubutton',
   'message': 'Message',
   'radiobutton': 'Radiobutton',
   'scale': 'Scale',
   'scrolledtext': 'ScrolledText',
   'scrollableframe': 'ScrollableFrame',
   'spinbox': 'Spinbox',
}

dicoFR_as_keys={}
for keys, values in (dicoFR.items()):
    dicoFR_as_keys[values]=keys

dicoEN_as_keys={}
for keys, values in (dicoEN.items()):
    dicoEN_as_keys[values]=keys


dicoLANG={'fr':dicoFR,
          'en':dicoEN}
dicoLANG_as_keys={
    'fr':dicoFR_as_keys,
    'en':dicoEN_as_keys}
dicoLANG_NAME={'Français':'fr',
               'English':'en'}
language=dicoLANG[lang]
language_as_keys=dicoLANG_as_keys[lang]
def setLang():
    global language
    language=dicoLANG[lang]

def getLang(arg):
    arg=arg.strip().lower()
    return language[arg]

def getLangKey(arg):
    arg=arg.strip()
    return language_as_keys[arg]

def getLangWdt(arg):
    arg=arg.strip().lower()
    return dico_wdt[arg]

def setLang(value):
    global lang, language
    lang=value

def actualize():
    global language
    language=dicoLANG[lang]
    #language=dicoLANG[lang]