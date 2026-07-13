# Guide de style du cursus en français

Ce guide régit la rédaction de l'édition académique française. Il s'emploie avec
les [`conventions techniques de rédaction`](../guides/technical-authoring-conventions.md),
la [`base terminologique`](termbase.yml) et le
[`guide de style anglais`](style-guide-en.md). Les éditions française et anglaise
sont deux voies de même statut vers un seul contrat technique ; le français n'est
pas une traduction secondaire.

## Voix et structure

- Adressez-vous à l'apprenant par **vous** et à l'impératif direct : « Mesurez la
  tension », « Comparez les courbes », « Justifiez votre choix ».
- Préférez des phrases courtes, des verbes précis et un français technique
  international compréhensible au Bénin comme dans d'autres contextes francophones.
- Évitez les calques de l'anglais, les tournures idiomatiques, les doubles
  négations, l'humour culturel non nécessaire et la complexité de lecture sans
  rapport avec l'acquis évalué.
- Formulez les titres comme une question ou une affirmation technique : « La
  charge modifie la tension mesurée du diviseur », plutôt que « Diviseurs ».
- Séparez consigne, preuve, avertissement et explication. Chaque étape numérotée
  décrit une seule action observable et son point de contrôle.
- Réservez **doit** à une exigence, **devrait** à une recommandation, **peut** à
  une permission ou capacité clairement déterminée. N'effacez pas le responsable
  par une tournure passive.

## Langue technique et terminologie

- Utilisez le terme français approuvé dans la base terminologique et donnez à la
  première occurrence l'acronyme professionnel utile : circuit imprimé (PCB),
  modulation de largeur d'impulsion (PWM). Conservez GPIO, SPI, I²C, UART, FPGA,
  CMRR et PSRR lorsque les documentations et instruments les utilisent.
- Ne traduisez pas les identifiants, commandes, chemins, noms de registre, jetons
  de protocole, noms de nets, repères de composants ni messages de diagnostic.
  Expliquez-les en français après leur forme originale.
- Distinguez exactitude/justesse, précision/fidélité, résolution, tolérance,
  répétabilité et incertitude. Définissez la propriété métrologique visée.
- Précisez **terre de protection**, **masse châssis**, **masse de signal** ou
  **référence 0 V** ; le seul mot « masse » ne prouve pas leur interconnexion.
- Évitez les faux amis : *actuel* pour *current*, *éventuellement* pour
  *eventually*, *librairie* pour *library*, ou *cycle de travail* pour *duty cycle*.
  Pour *control*, choisissez *commande*, *régulation* ou *contrôle* selon le sens.
- Un synonyme régional peut accompagner le terme approuvé s'il facilite l'accès,
  sans transformer ce synonyme en piège d'évaluation.

## Nombres, notation et unités

- Employez la virgule décimale dans la prose : `3,3 V`. Le code, SPICE, les
  données machine, les noms de fichier et les numéros de version gardent le point.
- Placez une espace insécable si possible entre nombre et unité : `10 kΩ`,
  `25 °C`, `2,0 ms`. Le symbole d'unité ne prend ni pluriel ni point final.
- Employez les préfixes SI et évitez toute ambiguïté entre *billion* anglais et
  français : écrivez `1 × 10^9`, `1 GHz` ou la quantité exacte.
- Publiez `µ` et n'acceptez `u` que dans les champs d'outils limités à l'ASCII.
  Respectez la casse : `m` signifie milli, `M` méga ; `Hz`, `V`, `A`, `Ω`.
- Définissez tout symbole à sa première occurrence, conservez une notation stable,
  faites apparaître les unités lors des substitutions et annoncez les conventions
  vectorielle, complexe, de phase et efficace/crête.
- Associez chaque valeur à ses conditions : alimentation, entrée, température,
  fréquence, charge, bande passante de l'instrument, référence, tolérance et
  incertitude selon le cas.

## Consignes, questions et évaluation

- Demandez une action observable : estimer, tracer, calculer, mesurer, comparer,
  diagnostiquer, choisir, justifier ou limiter une affirmation. « Comprendre »
  n'est pas, seul, un verbe d'évaluation.
- Recueillez la prédiction avant de dévoiler l'observation ; exigez une raison et,
  si utile, un degré de confiance. Une prédiction honnête ne perd pas de points
  uniquement parce qu'elle diffère du résultat.
- Évitez les questions pièges, les négations imbriquées, les distracteurs
  grammaticaux et les connaissances locales étrangères à l'acquis. Les distracteurs
  représentent des modèles techniques ou erreurs de méthode plausibles.
- Évaluez le sens technique, les preuves, la sécurité et la clarté, non l'accent,
  l'idiome ou une grammaire non essentielle, sauf acquis linguistique explicite.
- Publiez les ressources permises, conventions numériques et terminologiques,
  barème, seuil, frontière individuel/équipe et voie de contestation du libellé.

## Contexte et affirmations

- Citez l'identifiant et la version de la fiche contexte. Montrez quelle exigence,
  quel calcul, quelle architecture, quel essai, quel coût, quelle mesure de
  sécurité ou quelle décision de cycle de vie change. Un lieu n'est pas un décor.
- Ne décrivez aucun pays ni aucune communauté uniquement par le manque. Présentez
  aussi des contextes scientifiques, industriels, artistiques, commerciaux et de
  service public ; décrivez des faits observés plutôt que des stéréotypes.
- Nommez précisément les acteurs qui ont conçu, assemblé, testé, étalonné,
  déployé ou maintenu la configuration. Le lieu d'assemblage ne suffit pas à
  établir l'origine ; appliquez le guide de contribution et son dossier.
- Limitez toute affirmation de performance aux conditions et à l'échelon de preuve
  atteint. « Cela a fonctionné une fois » ne prouve ni fiabilité, ni aptitude au
  terrain, ni rendement de fabrication généralisable.

## Contrôle de parité français–anglais

- [ ] Même identifiant sémantique, version, état, acquis, prérequis, durée, points,
      seuil, ressources permises, limites de sécurité, valeurs, équations, données,
      figures, pannes, plages attendues et total du barème.
- [ ] Français naturel, non-aligné mot à mot sur la syntaxe anglaise.
- [ ] Légendes, textes alternatifs, descriptions longues, transcriptions et
      explications des réponses sont entièrement localisés.
- [ ] Identifiants techniques et localisateurs de sources partagés inchangés.
- [ ] Toute correction technique ouvre un ticket apparié et les deux éditions sont
      corrigées, revues et publiées ensemble.
- [ ] Des apprenants des deux parcours linguistiques ont testé libellé et demande
      cognitive.

La traduction automatique ne fournit qu'un brouillon interne. Un réviseur
technique qualifié et un réviseur pédagogique francophone approuvent la diffusion.
