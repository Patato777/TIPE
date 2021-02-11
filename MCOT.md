# Mise en cohérence des objectifs du TIPE
## Titre, motivation et ancrage au thème
### Titre de votre sujet TIPE (20 mots)
Répartition de lieux en groupes de taille égale en minimisant la distance intra-groupe *13 mots*
### Quelle est votre motivation pour le choix du sujet ? (50 mots)
Il s'agit d'un sujet que j'avais déjà eu l'occasion de rencontrer et qui m'avait plu. Le grand nombre de manières de l'aborder ainsi que les problèmes de "méta-optimisation" des paramètres des algorithmes m'ont parus particulièrement attrayants. *36 mots*
### En quoi votre étude s'inscrit-elle dans le thème de l'année ? (50 mots) 
Optimiser la partition d'un ensemble de lieux pour minimiser la distance au sein d'un groupe donné permet de réduire l'empreinte environnementale lors de déplacements entre ces lieux, mais aussi, par exemple, d'optimiser la distribution de ressources lors du choix de branchement à un point d'arrivée ou un autre. *48 mots*

## Mise en Cohérence des Objectifs du TIPE
### Bibliographie commentée (650 mots)
Le partitionnement de données ("clustering") informatisé est un domaine de recherche actif depuis les années 1950. Il s'agit, étant donné un ensemble de données non étiquetées, de les répartir en plusieurs classes d'objets similaires. Les applications sont diverses, de la numérisation d'un signal [1] à l'analyse d'images. Le problème étant souvent NP-difficile, il n'existe pas de méthode exacte pour le résoudre. De nombreuses approches sont possibles et un grand nombre d'algorithmes existent, développés tout au long de la seconde moitié du 20° siècle et encore améliorés aujourd'hui.\
En particulier, lorsque le nombre de classes est donné, une heuristique très utilisée est celle des k-moyennes ("k-means"). Il s'agit ici de minimiser la distance des points d'une classe au barycentre de la classe, étant donné une mesure de distance fixée au préalable. L'algorithme initial, s'exécutant en temps polynomial du nombre de points et de classes, a été proposé par Stuart Lloyd en 1957, mais publié 25 ans plus tard, en 1982 [1]. Edward D. Forgy publie un algorithme essentiellement identique en 1965 et c'est en 1967 que James MacQueen le décrit sous le nom de k-means [2]. Le principe en est assez simple : des centroïdes initiaux sont choisis aléatoirement parmis tous les points, définissant chacun une classe. Les autres points sont ensuite assignés à la classe du centroïde dont ils sont le plus proche. Finalement, les barycentres sont recalculés et l'algorithme est itéré. De nombreuses améliorations ont été proposées, proposant par exemple des manières de choisir les points initiaux [3] ou suggérant de recalculer les centroïdes à chaque assignation d'un point, par exemple. L'algorithme comme ses variations classiques sont assurés de converger vers un minimum local en temps polynomial.\
Une autre approche possible, très généraliste, repose sur l'idée d'algorithmes évolutifs, plus particulièrement, sur l'utilisation d'algorithmes génétiques. Ils peuvent être utilisés pour résoudre des problèmes d'optimisation très variés.\
Proposés à l'origine par John Holland en 1975 [4], ils ont été améliorés et adaptés à des problèmes spécifiques durant toute la fin du XX° siècle. L'un des points faisant l'objet d'un grand nombre de propositions d'amélioration réside dans la manière de choisir les individus à reproduire afin de maintenir une grande diversité tout en assurant une convergence assez rapide, le tout en un temps raisonnable. Plusieurs méthodes ont ainsi été proposée, avec plus ou moins de succès, faisant l'objet de comparaisons notamment par Goldberg et Deb [5]. La mise en oeuvre d'un algorithme génétique pour un problème particulier demande souvent un certain nombre d'adaptations, sources de recherche majeur dans le domaine. En effet, avant même l'utilisation de l'algorithme, se pose la question de la modélisation des solutions. Si Holland préconisait un codage binaire, qui correspondait à sa modélisation du fonctionnement de l'algorithme [4], d'autres possibilités existent, comme l'utilisation de nombre réels comme chromosomes ou d'alphabets à plus de 2 caractères, qui, ainsi que l'a montré Michalewicz, peuvent faire preuve d'une grande efficacité expérimentale. Un autre problème majeur est la façon de traiter des individus ne correspondant pas à des solutions potentielles, quand l'ensemble des solutions est strictement inclus dans l'ensemble des chromosomes possibles. Là encore, plusieurs approches sont possibles. Michalewicz a ainsi présenté un certain nombre de manières de les comparer aux autres, en les conservant dans la population pour maintenir la diversité [6], des méthodes de "réparation", adaptées aux problèmes, existent aussi, ainsi que des opérateurs de sélection et de mutation spécifiques permettant de ne produire que des individus dans la bonne forme, dans le cas du problème du voyageur de commerce, par exemple [7]. D'autres variantes encore existent.\
Enfin, l'implémentation pratique d'un algorithme génétique, au-delà de la modélisation du problème, demande une réflexion sur les paramètres, notamment la probabilité de mutation, de croisement ou le nombre d'individus. Si le choix dépend du problème, des paramètres standards se sont très vites répandus, à la suite d'une étude de De Jong, sur une suite particulière, dès 1975. En 1986, Grefenstette proposa néanmoins, afin d'avoir des paramètres plus adaptés au problème étudié, l'utilisation de "méta-algorithmes génétiques", où la population évoluée serait les paramètres eux-mêmes. *649 mots*

### Problématique retenue (50 mots)
On souhaite adapter et implémenter plusieurs algorithmes pour regrouper n points donnés par leurs distances aux autres en k classes d'autant de points, en minimisant la somme des distances au sein de chaque classe et comparer leurs performances. *39 mots*

### Objectifs du TIPE (100 mots)
Je me propose d'implémenter en Python :
- un algorithme "exact", qui générerait exhaustivement toutes les solutions possibles pour déterminer la meilleure
- un algorithme de kmeans, ainsi que plusieurs heuristiques pour le choix des points initiaux
- un algorithme génétique, avec plusieurs opérateurs de sélection et de croisement
- ainsi que potentiellement d'autres algorithmes plus simples

d'optimiser leurs paramètres, d'étudier leurs complexités et de comparer leurs performances, d'abord entre plusieurs variantes du même algorithme, puis entre les algorithmes, pour différentes configurations de points, notamment sur des données réelles, comme les villes de l'Essonne. *89 mots*

### Positionnement thématique
- Choix du thème 1 : Informatique pratique
- Choix du thème 2 : Mathématiques appliquées
- Choix du thème 3 : Informatique théorique

### Mots clés
- Français : Partitionnement, k-moyennes, algorithmes génétiques, graphe, optimisation
- Anglais : Clustering, kmeans, genetic algorithms, graph, optimisation

### 5 à 10 références bibliographiques majeures
[1] S. P. Lloyd, « Least square quantization in PCM », Bell Telephone Laboratories Paper\
[2] J. Macqueen, Some methods for classification and analysis of multivariate observations, In 5-th Berkeley Symposium on Mathematical Statistics and Probability, 1967, p. 281–297.\
[3] David Arthur and Sergei Vassilvitskii, k-means++: The Advantages of Careful Seeding, 2006.\
[4]  J. H. Holland, Adaptation In Natural And Artificial Systems, University of Michigan Press (1975)\
[5] D.E Goldberg and K. Deb. A comparative analysis of selection schemes used in genetic algorithms. In G.J.E. Rawlins, editor, Foundations of Genetic Algorithms , pages 69-93. Morgan Kaufmann, 1991.\
[6] Michalewicz, Z., A Survey of Constraint Handling Techniques in Evolutionary Computation Methods, Proceedings of the 4th Annual Conference on Evolutionary Programming, MIT Press, Cambridge, MA, 1995, pp. 135-155.\
[7] Larranaga, Pedro & Kuijpers, Cindy & Murga, R. & Inza, I. & Dizdarevic, S.. (1999). Genetic Algorithms for the Travelling Salesman Problem: A Review of Representations and Operators. Artificial Intelligence Review. 13. 129-170.
