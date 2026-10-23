# BFL image automation — Kastelen België

Source canonique : `MarcW88/bloc-notes-numerique` :
- `scripts/generate_bfl_images.py` (copie conforme)
- `.agents/skills/editorial-image-planner/SKILL.md` (déjà installé, SHA identique)
- `.github/workflows/generate-editorial-images.yml` (déclencheurs adaptés au site)
- `.content/image-requests/_template.json` (chemin source de la fiche adapté)

## Installer le secret

Ouvrir https://github.com/MarcW88/kastelenbelgie/settings/secrets/actions et ajouter un **Repository secret** nommé `BFL_API_KEY`. Insérer la clé BFL uniquement dans le formulaire secret.

## Lancer

1. Préparer une demande `PENDING` selon le planner (une requête approuvée, faible risque de tromperie, image appropriée).
2. Ajouter exactement le `marker` dans `content/kasteel/<slug>/body.html` à l'emplacement voulu.
3. Publier ces deux changements sur `main`. Le workflow GitHub Actions a les autorisations `contents: write` et pousse l'illustration dans `assets/generated/`, l'insertion dans le fichier source et l'état `GENERATED`.
4. La reconstruction du site conserve l'image car le générateur réutilise les `body.html`.
5. Pour régénérer une image, modifier le JSON en `REGENERATE`.

Endpoint : `https://api.bfl.ai/v1/flux-2-pro-preview`.
La clé doit être présente avant l'exécution d'une demande active. Aucun appel ni coût BFL n'est déclenché par la simple installation de ce workflow.

Sécurité du patrimoine : ne pas représenter une image IA comme une photographie fidèle d'un château réel ; pour les faits architecturaux, utiliser des photographies authentiques autorisées ou indiquer clairement le caractère illustratif.
