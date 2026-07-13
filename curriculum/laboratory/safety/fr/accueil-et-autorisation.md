---
semantic_id: ESE-SAF-002
id: ESE-SAF-002-fr
language: fr
paired_with: ESE-SAF-002-en
version: 0.1.0
status: draft
access: public-formative-and-construct
---

# Accueil sécurité et dossier d'autorisation

Ce dossier public prépare apprenants et évaluateurs. Il n'attribue ni G1, ni G3, ni
autorisation. L'autorité crée des variantes réelles inédites mais équivalentes dans
le stockage restreint et consigne les résultats avec `ESE-SAF-FRM-002`.

## Acquis de l'accueil

L'apprenant peut repérer les moyens d'urgence locaux ; classer L0–L4 ; expliquer
pourquoi la tension seule ne suffit pas ; calculer puissance de défaut et énergie d'un
condensateur ; inspecter EPI, cordons, fusibles, sondes et sources ; appliquer la
pré-mise sous tension ; commander l'arrêt ; isoler et vérifier l'absence d'énergie ;
signaler un événement ou une quarantaine sans dissimuler de preuve.

## Quiz formatif

Choisissez l'action la plus sûre et justifiez-la en une phrase.

1. Une source de 9 V peut fournir 20 A en court-circuit. La tension suffit-elle pour L1 ?
   A. oui ; B. non, classer courant/puissance de défaut et protection ; C. oui avec
   lunettes ; D. oui brièvement.
2. Un condensateur de `4700 µF` chargé à `24 V` stocke environ : A. `0,14 J` ;
   B. `0,68 J` ; C. `1,35 J` ; D. `2,71 J`.
3. Le courant vaut deux fois la prédiction sans dommage visible. Première action :
   A. relever la limite ; B. toucher pour chercher la chaleur ; C. isoler et diagnostiquer ;
   D. changer le fusible.
4. Il faudrait relier la masse d'une sonde d'oscilloscope référencée à la terre à un
   nœud de commutation non vérifié. A. agir vite ; B. supprimer la terre ; C. arrêter
   et employer la méthode différentielle/d'isolement approuvée au niveau requis ; D. fil fin.
5. Un pack lithium revient gonflé. A. essai de charge ; B. perforer ; C. appliquer la
   quarantaine sans contact prévue ; D. jeter avec les ordures.
6. Qui peut commander l'arrêt ? A. enseignant ; B. apprenant autorisé ; C. toute personne ;
   D. autorité de sécurité seulement.
7. Avant G1, alimenter un montage L1 est permis uniquement : A. seul sous 12 V ;
   B. avec accord d'un pair ; C. sur poste maîtrisé par l'enseignant, en encadrement
   direct, l'enseignant commandant chaque alimentation ; D. jamais.
8. L'entraînement au brasage avant G3 peut commencer : A. seul après G1 ; B. en L2,
   après briefing et sous encadrement direct ; C. après diplôme ; D. à domicile.
9. Un quasi-accident sans dommage est : A. ignoré ; B. signalé et analysé ; C. effacé
   pour préserver la note ; D. consigné seulement s'il se répète.
10. Une compétence antérieure permet de contester G1 en : A. montrant seulement une
    attestation ; B. supprimant la preuve ; C. réussissant une épreuve équivalente,
    inédite et formellement évaluée au même seuil ; D. signant soi-même.
11. Après coupure, on peut régler lorsque : A. les DEL sont éteintes ; B. une minute
    passe ; C. toutes sources sont isolées, le délai respecté et l'absence d'énergie
    vérifiée ; D. un pair touche sans problème.
12. Un solvant inconnu arrive sans FDS. Il est : A. L2 en petite quantité ; B. utilisé
    près d'une fenêtre ; C. mis en quarantaine avant identification/analyse ; D. dilué.

**Corrigé formatif :** 1 B ; 2 C (`0,5 × 0,0047 × 24² = 1,35 J`) ; 3 C ; 4 C ;
5 C ; 6 C ; 7 C ; 8 B ; 9 B ; 10 C ; 11 C ; 12 C. Une erreur renvoie à la section
du manuel et à une réévaluation avec données modifiées ; mémoriser ne valide pas une porte.

## Circuit des stations pratiques G1

L'épreuve réelle emploie du matériel vérifié à faible énergie et des valeurs changées.
Le candidat choisit EN/FR et les aides terminologiques/d'accès approuvées.

| Station | Action observable | Preuve exigée | Échec critique |
|---|---|---|---|
| A — local et arrêt | repérer coupure, sortie, fiche secours et quarantaine ; citer deux arrêts | fiche et justification orale | ne trouve pas coupure/secours ou poursuit après `ARRÊT` |
| B — inspection hors énergie | trouver défaut de cordon/fusible/polarité/calibre ; choisir EPI | défaut, conséquence, traitement | tente d'alimenter avec défaut |
| C — énergie | calculer courant/puissance de défaut et énergie du condensateur ; classer au plus haut | calculs avec unités/limites | emploie la tension seule |
| D — réglage source | sortie coupée, régler tension/courant et vérifier entrée/fusible du multimètre | configuration observée | court-circuite, mauvaise entrée ou contourne protection |
| E — alimentation maîtrisée | contrôle, mains retirées, alimenter, comparer, arrêter sur anomalie | prédiction, observation, isolement | touche/recâble sous tension ou relève une limite inexpliquée |
| F — arrêt/signalement | isoler, attendre/décharger, vérifier zéro, étiqueter un défaut simulé, transmettre | vérification et transmission complète | touche avant vérification ou dissimule |

**Décision G1 :** réussite des six lignes critiques et d'au moins 10 des 12 critères
observables publiés. Aucun total ne compense échec critique, preuve malhonnête ou refus
d'arrêt. L'établissement fixe tentatives, conservation, recours et expiration avant épreuve.

## Construit G3 de brasage/reprise

Après briefing L2, l'entraînement peut commencer sous encadrement direct avant G3.
La porte d'autonomie emploie un objet inédit équivalent et vérifie : aspiration/support ;
EPI/hygiène ; choix température/outil ; étamage/joint maîtrisé ; dépose traversante sans
arracher de pastille ; reprise CMS bornée ; polarité/orientation ; inspection selon critères ;
continuité/court-circuit ; arrêt thermique ; nettoyage/déchets. Acte exposant à la brûlure,
aspiration neutralisée, outil chaud non maîtrisé, reprise sous tension ou inspection
malhonnête constitue un échec non compensable.

## Étalonnage des évaluateurs

1. L'autorité fige construit, variantes, critères, invites et données locales de secours.
2. Deux évaluateurs répètent chaque station, vérifient limites/état et chronomètrent.
3. Ils notent séparément un ancrage réussi, limite et critique (enregistré ou simulé),
   puis résolvent tout désaccord avant accueil des candidats.
4. Les invites demandent prédiction/raison sans souffler l'action. Tout acte dangereux
   est arrêté ; l'arrêt reste une preuve valable.
5. Faites une double notation sur l'échantillon local approuvé couvrant EN/FR et accès.
   Analysez réussite, désaccord et contestations sans réduire le seuil.
6. Consignez garde des variantes, instruments, noms, date et défauts. Tout changement du
   construit ou désaccord non résolu bloque l'administration.

## Remédiation et nouvelle évaluation

L'évaluateur consigne critère manqué, conception erronée et restriction immédiate.
L'apprenant suit la voie minimale : rappel du manuel ; calcul guidé ; inspection hors
énergie ; mise sous tension modelée ; jeu de rôle arrêt/signalement ; maniement d'un fer
froid ; adaptation accessible préservant la décision. Une valeur, panne ou installation
différente vérifie ensuite le transfert. Un acte critique suspend l'alimentation concernée
jusqu'à autorisation de réévaluation. Consignez résultat, nouvelle échéance et restriction ;
n'écrasez jamais la première tentative.

