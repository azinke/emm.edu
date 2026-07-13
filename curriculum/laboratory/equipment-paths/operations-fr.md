# Fiches d'exploitation du poste — français

**Identifiant sémantique :** M03-E4-OPS-01
**Langue :** fr
**Version :** 0.1.0-draft
**Ressource appariée :** `operations-en.md`
**État :** ni répétée ni approuvée pour la sécurité

Ces fiches ne s'appliquent qu'à l'enveloppe de tâche à énergie limitée approuvée
localement et à l'autorisation actuelle de l'apprenant. Arrêtez-vous si une
étiquette, une limite, une source, un cordon, une protection ou une autorisation
manque ou reste ambiguë.

## Plan commun du poste

```text
ARRIÈRE / services fixes
+------------------------------------------------------------------+
| [A] source approuvée, SORTIE COUPÉE [B] instrument [C] PC données|
|                                                                  |
| [D] zone DUT hors tension           [E] rangement sondes/cordons |
|     fiche d'inspection ici              aucun métal libre         |
|                                                                  |
| [F] preuves/carnet      [G] pièces : BON / RETOUR / QUARANTAINE  |
+------------------------------------------------------------------+
AVANT / voie de retrait de l'apprenant       [H] arrêt d'urgence
```

Gardez liquides, sacs et métaux étrangers hors du plan. L'arrêt d'urgence et la
sortie restent accessibles. `0V_REF` désigne la référence du signal, non la terre
de protection.

## Surcouches des parcours

| Zone | Minimal | Standard | Avancé |
|---|---|---|---|
| A | source très basse tension approuvée et limitée en courant | alimentation de laboratoire, sortie coupée, limite préréglée | source programmable, sortie verrouillée jusqu'à la revue |
| B | multimètre numérique plus analyseur logique/dispositif MCU caractérisé | multimètre, oscilloscope/générateur, analyseur logique/sonde de débogage selon la tâche | instrument de précision/automatisé avec fiche du montage et du plan de référence |
| C | dispositif d'acquisition hors ligne ; réseau inutile | dispositif hors ligne d'exportation/construction | contrôleur d'automatisation hors ligne et destination des données brutes |
| D | plaque d'essai/carte basse tension seulement | même DUT avec dégagement des sondes | montage revu avec raccords protégés/détrompés, le cas échéant |

Un appareil avancé n'autorise ni une énergie supérieure ni le travail sans
surveillance.

## Guide rapide QG-01 — Contrôlez avant la mise sous énergie

1. Confirmez avec l'enseignant votre autorisation, l'identifiant de tâche, le
   parcours matériel et l'enveloppe approuvée.
2. Lisez les étiquettes de la source, de l'instrument, des cordons, sondes,
   montages et DUT. Placez en `QUARANTAINE` tout élément endommagé, périmé,
   inconnu ou incompatible ; ne l'essayez pas sur un DUT.
3. Toutes les sources étant coupées et l'énergie stockée dissipée par la méthode
   approuvée, contrôlez polarité, valeurs, conducteurs exposés, référence du
   signal et courts-circuits possibles.
4. Calculez ou relevez le courant de défaut, la puissance, l'énergie stockée et la
   température accessible maximaux de la tâche. Arrêtez-vous si la limite
   approuvée manque.
5. Réglez tension et limite de courant, sortie coupée. Choisissez fonction, borne,
   calibre, atténuation, seuil et référence du signal de l'instrument.
6. Demandez le contrôle pair/enseignant exigé. Gardez une main prête à couper
   l'énergie sans passer le bras au-dessus du circuit.

## Guide rapide QG-02 — Mettez sous énergie, observez, arrêtez

1. Annoncez la mise sous énergie et n'activez que la source approuvée.
2. Observez courant, indicateurs de température, odeur, bruit et premier point
   d'essai attendu avant de poursuivre.
3. Arrêtez immédiatement en cas de chaleur, odeur, fumée ou bruit inattendu,
   source instable, isolant endommagé, limitation de courant non prévue, mesure
   hors limites, perte de la référence du signal ou situation incertaine.
4. Coupez l'énergie ; ne touchez pas avant que l'énergie stockée et la température
   soient sûres selon la méthode approuvée. Avertissez l'enseignant et conservez
   la configuration et les preuves.
5. Consignez l'arrêt comme preuve. Ne cachez pas un presque-accident et ne modifiez
   pas le montage avant la décision d'inspection ou de quarantaine.

## Guide rapide QG-03 — Multimètre numérique

- Contrôlez boîtier, cordons, isolation, bornes, étiquette fusible/fonction et
  échéance. Confirmez l'approbation pour la tâche ; une catégorie marquée
  n'élargit pas l'enveloppe du cursus.
- Pour tension/résistance, utilisez les bornes commune et tension/résistance. Ne
  mesurez jamais résistance ou continuité sur un circuit sous tension.
- La mesure par l'entrée courant est exclue, sauf consigne et qualification
  distinctes qui l'autorisent explicitement.
- Contrôlez une lecture plausible sur une source ou un montage d'essai approuvé
  avant et après une mesure liée à la sécurité.
- Conservez valeur, unité, calibre, stabilité, points d'essai, polarité,
  identifiant du multimètre et contribution pertinente de la résolution/
  résistance d'entrée.

## Guide rapide QG-04 — Oscilloscope et analyseur logique

- Identifiez terre de protection, châssis, référence du signal et `0V_REF` du DUT ;
  ne supposez jamais leur isolation.
- Contrôlez sonde, atténuation, compensation, voie, seuil, fréquence
  d'échantillonnage, base de temps et déclenchement sur un signal approuvé.
- DUT hors tension, raccordez d'abord la référence du signal et retirez-la en
  dernier. Utilisez une liaison de référence courte approuvée pour le montage.
- Enregistrez les échantillons bruts ou une trace ouverte avec identifiant et
  réglages complets. Une capture d'écran ou un décodage seul ne suffit pas.
- Ne déduisez ni temps de montée, ni dépassement, ni marge analogique d'un
  analyseur uniquement numérique.

## Guide rapide QG-05 — Alimentation, générateur et dispositif MCU

- Réglez amplitude/tension, décalage, fréquence, forme et limite de courant,
  sortie coupée. Vérifiez ces réglages sur un point à vide approuvé.
- Confirmez une seule source pour le DUT ou une protection antiretour approuvée.
- Le dispositif MCU démarre dans un état sûr, exige `ARM` et redevient sûr après
  délai ou déconnexion. Sans identité, profil et état, ne le raccordez pas.
- N'employez jamais le projet de dispositif hors des circuits pédagogiques 0 V/
  3,3 V à énergie limitée ; aucune unité ne peut servir avant que sa fiche
  d'approbation porte `approved`.

## Fiches de dépannage

### TC-01 Valeur continue attendue absente

1. Coupez l'énergie et confirmez la décharge.
2. Contrôlez référence et valeurs prédites du modèle.
3. Contrôlez polarité/limite de source, bornes/fonction du multimètre, continuité,
   rangées de la plaque d'essai, valeurs et un nœud à la fois.
4. Modifiez une seule condition discriminante et prédisez le résultat avant de
   remettre sous énergie.
5. Placez en quarantaine tout cordon ou composant qui échoue au contrôle connu.

### TC-02 Acquisition plate, écrêtée ou bruitée

1. Coupez la sortie ; contrôlez référence commune et plage de tension permise.
2. Comparez `tau` ou l'intervalle minimal prédit avec intervalle et durée
   d'échantillonnage, bande passante, atténuation et déclenchement.
3. Cherchez saturation ADC, décalage du générateur, mauvais couplage, échantillons
   perdus, entrée flottante ou charge de l'entrée.
4. Vérifiez un niveau statique ou un intervalle par une méthode indépendante.

### TC-03 Le MCU ne démarre pas ou ne se débogue pas

1. Débranchez les charges ; contrôlez alimentation, limite de courant, câble,
   orientation, état reset/boot, référence du signal et dommages visibles.
2. Employez l'image de récupération et le câble/la sonde connus. Notez la sortie
   exacte de l'outil ; n'effectuez aucune opération de sécurité irréversible.
3. Testez alimentation, reset, symptôme d'horloge, identité du micrologiciel,
   multiplexage des broches et interface dans un ordre discriminant.
4. Ne modifiez qu'une variable. Ne restaurez la panne semée après évaluation que
   si la procédure de gestion de configuration l'exige.

### TC-04 Arrêtez et escaladez

Arrêtez et appelez l'enseignant pour toute source inconnue, chauffe/odeur
inattendue, isolation endommagée, surintensité répétée, protection/verrouillage
absent, liquide, blessure, fumée, feu ou doute sur la terre de protection. Ne
coupez l'énergie que si la procédure d'urgence approuvée rend l'action sûre.
Suivez la procédure du local pour incident, presque-accident et évacuation ; ces
fiches ne la remplacent pas.

## Entrée CI-01

1. Enregistrez l'identifiant du poste/configuration et chaque appareil/accessoire.
2. Confirmez autorisation actuelle et commandes/étiquettes accessibles.
3. Inspectez et contrôlez les fonctions ; notez état et échéances.
4. Comptez cordons/sondes/adaptateurs ; confirmez caractéristiques et accessoires.
5. Notez les défauts antérieurs. Placez les éléments défaillants directement en
   `QUARANTAINE` et obtenez un remplacement qualifié.
6. Chargez uniquement le micrologiciel/la configuration approuvés et créez un
   dossier de preuves brutes nommé par pseudonyme, tâche, date et tentative.

## Sortie CO-01

1. Arrêtez le stimulus, coupez la sortie puis la source, et confirmez décharge/
   refroidissement par la méthode approuvée.
2. Retirez les cordons de signal, rétablissez les réglages locaux et sauvegardez
   données brutes, configuration, empreintes fournies et références du carnet.
3. Inspectez, comptez, nettoyez à sec selon la méthode approuvée, protégez les
   sondes et enroulez les cordons sans contrainte.
4. Mettez les éléments connus en `RETOUR` ; ne transférez jamais un élément non
   vérifié dans `BON`. Étiquetez les pannes (symptôme, montage, date, déclarant,
   dernier état sûr), puis placez-les en `QUARANTAINE`.
5. Retirez les chutes et restaurez le plan. Faites valider la sortie ; consignez
   incident, presque-accident, manque ou preuve physique non résolue.

SPDX-License-Identifier: CC-BY-SA-4.0
