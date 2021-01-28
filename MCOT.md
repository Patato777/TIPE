# Mise en cohérence des objectifs du TIPE
## Titre, motivation et ancrage au thème
### Titre de votre sujet TIPE (20 mots)
Répartition de lieux en groupes de taille égale en minimisant la distance intra-groupe *13 mots*
### Quelle est votre motivation pour le choix du sujet? (50 mots)
Il s'agit d'un sujet que j'avais déjà eu l'occasion de rencontrer et qui m'avait plu. Le grand nombre de manières de l'aborder ainsi que les problèmes de "méta-optimisation" des paramètres des algorithmes m'ont parus particulièrement attrayants. *36 mots*
### En quoi votre étude s'inscrit-elle dans le thème de l'année ? (50 mots) 
Optimiser la partition d'un ensemble de lieux pour minimiser la distance au sein d'un groupe donné permet de réduire l'empreinte environnementale lors de déplacements entre ces lieux, mais aussi, par exemple, d'optimiser la distribution de ressources lors du choix de branchement à un point d'arrivée ou un autre. *48 mots*

## Mise en Cohérence des Objectifs du TIPE
### Bibliographie commentée (650 mots)
Le partionnement de données ("clustering") informatisé est un domaine de recherche actif depuis les années 1950. Il s'agit, étant donné un ensemble de données non étiquetées, de les répartir en plusieurs classes d'objets similaires. Les applications sont nombreuses, de la numérisation d'un signal [1] à l'analyse d'images. Les approches sont nombreuses et de nombreux algorithmes existent, développés tout au long de la seconde moitié du 20° siècle et encore améliorés aujourd'hui.
En particulier, lorsque le nombre de classes est donné, une heuristique très utilisée est la méthode des k-moyennes ("k-means"). Il s'agit ici de minimiser la distance des points d'une classe au barycentre de la classe, étant donné une mesure de distance fixée au préalable. L'algorithme initial, s'executant en temps polynomial du nombre de points et de classes, a été proposé par Stuart Lloyd en 1957, mais publié 25 ans plus tard, en 1982 [1]. Edward D. Forgy publie un algorithme essentiellement identique en 1965, mais c'est en 1967 que James MacQueen le décrit sous le nom de k-means [2]. Le principe en est assez simple : des centroïdes initiaux sont choisis aléatoirement parmis tous les points, définissant chacun une classe. Les autres points sont ensuite assignés à la classe du centroïde dont ils sont le plus proche. Finalement, les barycentres sont recalculés et l'algorithme est itérés, en prenant ces barycentres comme centroïdes ininitiaux. L'algorithme s'arrête lorsque la répartition ne change plus. De nombreuses améliorations ont été proposées, proposant par exemple des manières de choisir les points initiaux [3] ou suggérant de recalculer les centroïdes à chaque assignation d'un point. L'algorithme comme ses variations classiques sont assurés de converger vers un minimum local en temps polynomial, bien que le problème soit NP-difficile.
Une autre approche possible, très généraliste, repose sur l'idée d'algorithmes évolutifs, qui peuvent être utilisés pour résoudre des problèmes très divers. Plus particulièrement, d'algorithme génétiques. 

### Problématique retenue (50 mots)

### Objectifs du TIPE (100 mots)

### Mots clés

### 5 à 10 références bibliographiques majeures
[1] S. P. Lloyd, « Least square quantization in PCM », Bell Telephone Laboratories Paper[2] J. Macqueen, Some methods for classification and analysis of multivariate observations, In 5-th Berkeley Symposium on Mathematical Statistics and Probability, 1967, p. 281–297.
[3] David Arthur and Sergei Vassilvitskii, k-means++: The Advantages of Careful Seeding, 2006.
