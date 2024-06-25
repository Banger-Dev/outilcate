def categoriser_mots_cles(mots_cles, categories):
    """
    Catégorise les mots clés en fonction des thématiques.

    Args:
    - mots_cles: List of str, les mots clés à catégoriser.
    - categories: Dict, les thématiques et leurs mots clés associés.

    Returns:
    - Dict, les mots clés catégorisés par thématique.
    """
    categorisation = {categorie: [] for categorie in categories}

    for mot in mots_cles:
        trouve = False
        for categorie, mots_cles_pertinents in categories.items():
            if mot in mots_cles_pertinents:
                categorisation[categorie].append(mot)
                trouve = True
                break
        if not trouve:
            if "Autres" not in categorisation:
                categorisation["Autres"] = []
            categorisation["Autres"].append(mot)

    return categorisation

# Exemple de catégories avec mots clés associés
categories = {
    "Énergie Houlomotrice": ["houlomotrice", "énergie houlomotrice", "houlomoteur", "centrale pelamis", "colonne d'eau oscillante"],
    "Déferlement": ["déferlement définition", "déferlement vague", "déferlement vent"],
    "Houle": ["houle et vague", "définition houle", "effet de la houle", "évolution d'une vague"],
    "Vagues": ["puissance d'une vague", "vague atlantique", "vague mer", "cycle des vagues mer", "différence vague houle"],
    "Électricité": ["énergie électrique déf", "énergie des vagues électricité", "exposé sur l'énergie"]
}

# Exemple de mots clés à catégoriser
mots_cles_a_categoriser = [
    "alternateur hydrolienne", "houlomotrice", "cagué definition", "énergie houlomotrice", 
    "houlomoteur", "centrale pelamis", "colonne d'eau oscillante", "comment mesurer la houle",
    "puissance d'une vague", "déferlement vague", "houle et vague", "évolution d'une vague"
]

# Catégoriser les mots clés
mots_cles_categorises = categoriser_mots_cles(mots_cles_a_categoriser, categories)

# Afficher les mots clés catégorisés
for categorie, mots in mots_cles_categorises.items():
    print(f"{categorie} : {mots}")
