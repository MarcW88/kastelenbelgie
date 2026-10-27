# Configuration des liens d'affiliation — Kastelen België

Modifier **uniquement** `content/affiliate-links.json` : remplacer la valeur `affiliateUrl: null` par l'URL de suivi personnelle, complète et valide, fournie par le programme Tiqets ou Booking.com correspondant.

- `loppem-tiqets` : billet Loppem, CTA de `/bezoeken/bezoekbare-kastelen/`.
- `ordingen-booking` : hôtel Kasteel van Ordingen, CTA de `/bezoeken/kastelen-overnachten/`.
- `chateau-du-lac-booking` : Martin’s Château du Lac, même page.

Tant que `affiliateUrl` vaut `null`, le générateur utilise `publicUrl` : il ne s'agit **pas** d'un lien attribuant des commissions.

Le générateur `scripts/build.mjs` remplace l'URL du bouton correspondant au moment du build. Lorsqu'une URL affiliée est configurée, le lien sortant porte `rel="noopener noreferrer sponsored"`; dans le cas contraire, il porte `rel="noopener noreferrer"`. La mention de transparence dans chaque page est toujours visible.

IMPORTANT : ne pas inventer ou construire de paramètres d'affiliation ; utiliser le lien suivi personnel fourni par la plateforme et vérifier qu'il cible bien le produit annoncé. Aucun identifiant secret n'est nécessaire dans ce fichier. Les autres pages (familles, parc) ne sont pas encore reliées à ces emplacements et ne doivent pas être considérées comme monétisées.

Cette branche est issue de `feat/monetization-castle-overnights` (PR #6). Elle inclut donc aussi les changements de cette PR. Ne pas fusionner séparément sans reconciliation. Les fichiers HTML générés doivent être régénérés et les checks de la branche protégée validés par le workflow habituel avant fusion.
