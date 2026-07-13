---
semantic_id: ESE-SAF-001
id: ESE-SAF-001-fr
language: fr
paired_with: ESE-SAF-001-en
version: 0.1.0
status: draft
safety_level: L0-L4
localization_layer: universal-core
---

# Manuel de sécurité du laboratoire

Lisez ce manuel avec le [contrat technique partagé](../shared/technical-contract.md).
Le contrat régit les limites numériques et les portes de compétence. Cette édition
régit les consignes en français. Avant usage, l'établissement doit compléter les
données de déploiement, citer les règles applicables, inspecter les locaux, former le
personnel et approuver le système.

## 1. Rôles, autorité et encadrement

L'autorité institutionnelle de sécurité approuve le manuel, les analyses de risques,
les permis L3/L4, les sorties de quarantaine et les actions correctives. Le responsable
du laboratoire tient les locaux et dossiers. Le responsable d'activité rédige la
procédure et les plages attendues. L'enseignant confirme l'état prêt et maîtrise la
mise sous tension. Le technicien entretient le matériel et les stocks séparés. Chaque
apprenant vérifie la tâche, signale l'incertitude, exerce le droit d'arrêt et conserve
des preuves honnêtes.

Un auteur ne peut approuver seul une activité dangereuse ni une porte à enjeu élevé.
Appliquez les ratios du contrat : au moins un enseignant/assistant formé pour 12
apprenants en L1/L2 et pour 8 en L3 non familier. L3/L4 et les premières expositions
prescrites exigent un encadrement direct : le responsable voit le travail, peut
intervenir et isoler l'énergie immédiatement. L'autoformation non accompagnée exclut
toujours le secteur, la haute tension, les batteries à forte énergie, la puissance RF
et toute activité L3/L4.

## 2. Niveaux d'autorisation

- **L0 :** accueil, observation, simulation, assemblage vérifié hors énergie.
- **L1 :** travaux fondamentaux approuvés et limités en courant dans l'enveloppe L1.
  G1 est obligatoire avant toute mise sous tension autonome.
- **L2 :** instruments de table en très basse tension, brasage, batteries protégées
  et rotation bornée approuvés dans l'enveloppe L2.
- **L3 :** énergie de défaut supérieure maîtrisée par l'établissement, conversion de
  puissance, packs batterie, dangers thermiques/mécaniques, produits/revêtements ou RF légale.
- **L4 :** secteur, haute tension, stockage à forte énergie, lasers ou équipement critique.

L'activité prend le niveau le plus élevé déclenché. L'autorisation est personnelle,
limitée à une tâche/niveau, datée et expirante ; elle ne se transfère ni entre personnes,
ni entre appareils, ni entre activités. L'enseignant vérifie le dossier avant travail.

## 3. Entrée et règles quotidiennes au poste

1. N'entrez que pour un travail programmé et autorisé ; repérez l'enseignant,
   l'isolement, les sorties, le rassemblement, les premiers secours, la réponse
   incendie et le point de quarantaine.
2. Attachez les cheveux ; fixez vêtements lâches et bijoux ; portez des chaussures
   fermées si l'activité l'exige. Écartez nourriture, boissons et produits non autorisés.
3. Inspectez poste, câbles, outils, ventilation et accès de secours. Étiquetez et
   mettez en quarantaine les dommages ; n'improvisez pas une réparation.
4. Dégagez sorties et cheminements. Disposez les outils pour pouvoir reculer sans
   franchir l'appareil.
5. Consignez les identifiants, l'état fonctionnel/d'étalonnage, la révision de
   l'activité, les plages attendues et les limites d'énergie avant raccordement.
6. Répétez la séquence de pré-mise sous tension à chaque modification.
7. Ne travaillez que sur une configuration alimentée à la fois. Ne recâblez jamais
   sous tension. Ne contournez jamais interverrouillage, DDR/GFCI, terre, fusible ou carter.
8. Le contrôle par un pair complète sans remplacer le point de contrôle enseignant.

## 4. EPI et protections techniques

L'analyse de risques choisit les protections dans cet ordre : supprimer/substituer le
danger, isoler ou protéger, limiter énergie et exposition, imposer une procédure, puis
ajouter les équipements de protection individuelle (EPI). Les lunettes sont la base
pour construction, coupe, brasage, rotation et mise sous tension avec risque de projection.
Choisissez protection thermique, chimique, faciale, auditive ou respiratoire selon
l'exposition évaluée et la fiche de données de sécurité (FDS). Les gants peuvent créer
un risque d'entraînement ou de perte de dextérité ; ils ne sont pas une protection
électrique générique.

Employez une aspiration locale pour fumées de brasage et procédés chimiques évalués.
Vérifiez la capture à la source avant chauffage. Les dispositifs ESD protègent le
matériel ; retirez le bracelet si l'activité peut exposer la personne à un danger
électrique non couvert par la méthode ESD approuvée.

## 5. Mise sous tension, mesure et arrêt

Prévoyez tension, courant, puissance, température et mouvement. Calculez l'énergie des
condensateurs et batteries. Vérifiez le composant, conducteur et la sonde les moins bien
assignés. Réglez la limitation de courant, sortie coupée. Raccordez, obtenez le contrôle,
retirez les mains, alimentez et comparez immédiatement aux plages attendues. Un écart
inexpliqué impose l'arrêt ; il n'autorise pas à augmenter la limite.

Mesurez continuité/résistance hors tension. Ne raccordez l'ampèremètre que sur l'entrée
protégée par fusible et le calibre correct ; ne placez jamais une entrée courant aux bornes
d'une source. Gardez les doigts derrière les protège-doigts. Ne supprimez jamais la terre
de protection d'un oscilloscope et appliquez le contrat partagé.

Pour régler : coupez, isolez toutes les sources, attendez le temps de décharge indiqué,
vérifiez l'absence d'énergie avec un instrument approprié, puis touchez. Incluez batteries,
USB, programmateurs, signaux externes et sources mécaniques/pneumatiques.

## 6. Brasage, batteries, mouvement, produits et RF

Posez le fer dans son support stable, vérifiez l'aspiration, dégagez la zone chaude et
considérez pointe et soudures récentes comme chaudes. Lavez-vous les mains après flux/
brasure ; ne mangez pas et ne touchez pas le visage. Triez scories, lingettes contaminées
et matières au plomb. Brûlure, aspiration défaillante ou support instable arrêtent le poste.

Inspectez les batteries à la sortie et au retour. Arrêtez pour gonflement, choc, perforation,
corrosion, fuite, odeur/chaleur inhabituelle, isolant endommagé ou provenance inconnue.
Ne chargez, court-circuitez, écrasez, ouvrez ni transportez une batterie suspecte. Isolez
l'appareil seulement sans contact ni aggravation ; sinon évacuez la proximité et appelez
l'équipe formée. Utilisez le récipient non conducteur, compatible avec la chimie et approuvé,
bornes séparées. Un feu/emballement suit le plan incendie adopté, jamais un choix improvisé.

Protégez et immobilisez les parties mobiles ; créez une zone sans trajectoire de projection.
Coupez avant de dégager un blocage. Pour un produit, lisez la FDS, étiquetez la quantité et
préparez déversement/déchet avant ouverture. En RF, respectez fréquence, puissance, antenne,
distance et lieu approuvés. Toute incertitude de configuration ou d'autorisation impose l'arrêt.

## 7. Arrêt du travail et urgence

Toute personne peut dire **ARRÊT** sans pénalité. Répétez, retirez les mains et suivez
l'ordre d'isolement/évacuation. Si cela est sûr, la personne désignée actionne la coupure
d'urgence. Ne touchez jamais une victime potentiellement sous tension. Donnez l'alerte,
appelez le numéro affiché, ne réalisez que les premiers secours maîtrisés, évacuez et
comptez les personnes. Ne rentrez ni ne réarmez avant levée par l'autorité responsable.

Après les soins immédiats, préservez lieux et configuration si cela reste sûr. Consignez
les faits, sans blâme ni supposition. Signaler un incident ou quasi-accident ne réduit pas
la note ; dissimuler ou altérer une preuve constitue une faute professionnelle grave.

## 8. Incident, quasi-accident et quarantaine

1. **Protéger :** arrêter, isoler/évacuer, appeler et donner les secours maîtrisés.
2. **Avertir :** prévenir rapidement enseignant et autorité selon la voie locale.
3. **Séparer :** fixer `DO NOT USE / NE PAS UTILISER`, noter unité, état énergétique
   et accès ; ne déplacer que par une méthode sûre approuvée.
4. **Consigner :** employer `ESE-SAF-FRM-005` pour atteinte, rejet, dommage, situation
   dangereuse, quasi-accident, batterie/appareil endommagé et élimination.
5. **Enquêter :** rechercher conditions causales, protections défaillantes, limites des
   preuves et activités touchées. Un quasi-accident reçoit la même attention pédagogique.
6. **Décider :** seule l'autorité nommée libère, répare/reteste, retourne, recycle ou élimine.
7. **Améliorer :** affecter responsable/date/contrôle d'efficacité ; réconcilier EN/FR
   et suspendre autorisations/contenus concernés si nécessaire.

## 9. Nettoyage, stockage et déchets

Coupez et vérifiez l'absence d'énergie. Remettez les instruments en état sûr ; inspectez
et comptez cordons, carters et pointes. Laissez refroidir dans une zone signalée. Nettoyez
selon la méthode approuvée et lavez-vous les mains. Séparez réutilisable connu bon, usage
étudiant, panne pédagogique et quarantaine.

Utilisez des contenants étiquetés, fermés et compatibles pour déchets de brasage, objets
piquants, batteries, déchets électroniques, solvants/revêtements et déchets ordinaires.
Ne jetez jamais batterie, liquide chimique, lingette contaminée, scorie métallique ou
patte coupante avec les ordures, sauf autorisation explicite du plan local. Consignez
transfert, masse/nombre, responsable et destination. Une matière inconnue va en quarantaine.

## 10. Accessibilité et participation sûre

Prévoyez cheminement libre, coupure accessible, poste/siège réglable, étiquettes contrastées,
tactiles et non fondées sur la couleur, porte-sondes et voie de communication accessible.
Si la dextérité n'est pas l'acquis, une aide peut manipuler selon les directives explicites
de l'apprenant ; celui-ci choisit le montage, prédit, maîtrise les décisions d'alimentation,
interprète et commande l'arrêt. L'adaptation ne réduit ni sécurité ni niveau de preuve.

## 11. Approbation d'activité et dossiers

Tout nouveau domaine ou changement important remplit `ESE-SAF-FRM-001` avant exposition.
L'approbation couvre une révision, un local, une voie matérielle, une population et une
période identifiés. Elle contient urgence, méthodes accessibles, conditions d'arrêt,
responsable du risque résiduel, preuves de validation et déclencheurs de révision.

Employez `ESE-SAF-FRM-002` pour l'autorisation personnelle, `ESE-SAF-FRM-003` pour
l'inspection compétente, `ESE-SAF-FRM-004` pour les exercices planifiés et
`ESE-SAF-FRM-005` pour événements/quarantaine/déchets. Un formulaire vierge n'est pas
une preuve. Conservez selon les règles de confidentialité/rétention et limitez les
données personnelles ou médicales.

