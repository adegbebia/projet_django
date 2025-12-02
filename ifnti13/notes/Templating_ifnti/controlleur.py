from jinja2 import Environment
from os.path import dirname, abspath

def generate_pdf(context):
    '''INSTANCIATION D’UN NOUVEL ENVIRONNEMENT
    AVEC DES OPTIONS DE BALISES PERSONNALISÉES'''
    
    # Créer un environnement Jinja2 avec des balises personnalisées
    j2_env = Environment(
        variable_start_string=r"\VAR{",
        variable_end_string="}",
        block_start_string=r"\BLOCK{",
        block_end_string="}",
        comment_start_string=r"\COMMENT{",
        comment_end_string="}"
    )
    
    '''DECLARATION DE FICHIER'''
    # Fichier à lire contenant le template avec les balises
    fichier_in = open("ifnti/liste_eleves.tex", 'r')
    # Fichier en sortie accueillant les données fournies
    fichier_out = open("out/template_out.tex", 'w')
    
    # Lecture du template
    template = fichier_in.read()
    
    # Contexte à utiliser pour le rendu
    monContext = context
    monContext["image_path"] = dirname(abspath(__file__)) + "/out/images/"
    
    '''APPLICATION DE L’ENVIRONNEMENT ÉDITÉ SUR LE TEMPLATE'''
    j2_template = j2_env.from_string(template)
    
    # Écriture dans le fichier en sortie
    fichier_out.write(j2_template.render(monContext))
    fichier_out.close()
    
    # Génération du PDF à partir du fichier LaTeX
    mon_pdf = build_pdf(open("out/template_out.tex", 'r'))
    mon_pdf.save_to("out/liste_eleves.pdf")
    
    '''FERMETURE DE CANAUX'''
    fichier_in.close()