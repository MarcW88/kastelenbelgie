# Demandes d'images BFL — Kastelen België

Moteur importé de `MarcW88/bloc-notes-numerique` sans modification de sa logique de génération, d'approbation, de polling ou de réinsertion.

## Emplacement du secret
GitHub > Settings > Secrets and variables > Actions > New repository secret.
Nom EXACT : `BFL_API_KEY`. Ne jamais écrire la clé dans le dépôt.

## Fonctionnement
L'agent `.agents/skills/editorial-image-planner/SKILL.md` décide si une image générée est appropriée, puis remplit un JSON copié depuis `_template.json`. Par défaut toutes les demandes sont `NOT_NEEDED` : aucune dépense BFL automatique.

L'API n'est appelée que si `required=true`, `allow_ai_generation=true`, `truth_risk=LOW` et `status=PENDING` ou `REGENERATE`. Les bâtiments patrimoniaux identifiables demandant une représentation factuelle exacte doivent utiliser une vraie photo sourcée et rester `BLOCKED`, sauf illustration clairement non documentaire.

**Différence technique avec Bloc Notes :** le champ `page` doit viser la source durable des pages (par exemple `content/kasteel/gravensteen/body.html` ou `content/kastelen/brussel/body.html`), jamais un `kasteel/.../index.html` généré automatiquement. Placer le marqueur unique dans ce fichier source, là où la figure doit apparaître. Le build natif `node scripts/build.mjs` reprend ensuite cette source, préservant les images lors de la reconstruction du site.

```html
<!-- EDITORIAL_IMAGE:gravensteen-editorial -->
```

`output_path` doit être sous `assets/generated/`. Images produites au format PNG, JPEG ou WebP. Dimensions par défaut : 1024×672. Le rendu figure inclut un alt et un ratio responsive.

Workflow : `.github/workflows/generate-editorial-images.yml` → `python3 scripts/generate_bfl_images.py` → génération via FLUX.2 Pro Preview → sauvegarde → insertion HTML dans la source → commit sur main. `GENERATED` permet de réinsérer l'image existante sans refaire de requête BFL.

Vérifier sans API : `python3 scripts/generate_bfl_images.py --check-only`.

Démarrage manuel : GitHub Actions → Generate approved editorial images with BFL → Run workflow. Le secret seul ne lance **aucune** génération sans demande approuvée. Ne pas appeler ce workflow avec une clé exposée dans un fichier ou un log.
