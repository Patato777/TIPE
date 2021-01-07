# Notes

variance inter-classes dans le cas du saut de Ward\
d(A,B) = d(gA,gB)x(NaNb)/(Na+Nb) (saut de Ward) http://maths.cnam.fr/IMG/pdf/Classification-2008-2.pdf (p.22)\
CAH (choix des barycentres initiaux)-> réalocation dynamique\
Isodata (Ball & Hall 1965) http://maths.cnam.fr/IMG/pdf/Classification-2008-2.pdf (p.17) "Un certain nombre de contraintes sont imposées pour empêcher la formation de classes d’effectifs trop faibles ou de diamètre trop grand."\
kmeans: montrer la convergence dans le cas du nombre d'éléments par classe fixé (si convergence il y a)\
kmeans: choix des centres de départ : CAH ou kmeans++ ou méthode déjà programmée
Michalewicz pour les algos génétiques: https://cs.adelaide.edu.au/~zbyszek/papers.html
Tuto recommandé par Wikipédia : https://mpatacchiola.github.io/blog/2017/03/14/dissecting-reinforcement-learning-5.html
https://en.wikipedia.org/wiki/Genetic_algorithm
Chromosome :
    - 1D-array : position = point, valeur = pool
    - 1D-array : position = pool, valeur = vecteur contenant les points
    - 1D-array : position = pool (pos. 1 à 5 : pool 1, etc.), valeur = point
Voyageur de commerce, mais en changeant la fonction d'évaluation
Inversion operator?

TODO:
    - Génétique

## Papers

To read:
 - E. Diday, The dynamic clusters method in nonhierarchical clustering, International Journal of Computer & Information Sciences 2 (1973), n°1, 61–88.
 - J. A. Hartigan et M. A. Wong, Algorithm AS 136 : a k-means clustering algorithm, Applied Statistics 28 (1979), 100–108.
 - Jir ́ı Matousek. On approximate geometric k-clustering. Discrete & Computational Geometry, 24(1):61–84, 2000.

Reading:
 - D.E Goldberg and K. Deb. A comparative analysis of selection schemes used in genetic algorithms. In G.J.E. Rawlins, editor, Foundations of Genetic Algorithms , pages 69{93. Morgan Kaufmann, 1991.

Finished:
 - Ball, Geoffrey H., Hall, David J. (1965) Isodata: a method of data analysis and pattern classification, Stanford Research Institute, Menlo Park,United States. Office of Naval Research. Information Sciences Branch (https://apps.dtic.mil/dtic/tr/fulltext/u2/699616.pdf) *Nothing to get from*
 - J. Macqueen, Some methods for classification and analysis of multivariate observations, In 5-th Berkeley Symposium on Mathematical Statistics and Probability, 1967, p. 281–297. https://www-m9.ma.tum.de/foswiki/pub/WS2010/CombOptSem/kMeans.pdf (p. 3) *The original definition of kmeans*
 - David Arthur and Sergei Vassilvitskii, k-means++: The Advantages of Careful Seeding, 2006 http://ilpubs.stanford.edu:8090/778/1/2006-13.pdf *An interesting way to chose base nodes*
 - Stuart P. Lloyd. Least squares quantization in pcm. IEEE Transactions on Information Theory, 28(2):129–136, 1982 https://web.stanford.edu/class/ee398a/handouts/papers/Lloyd%20-%20Least%20Squares%20Q%20in%20PCM.pdf *Original kmeans algorithm, too focused on its particular physics problem*
 - http://deptinfo.unice.fr/twiki/pub/Minfo04/IaDecision0405/Prsentationdesalgorithmesgntiquesetdeleursapplicationsenconomie_P.pdf *Basic explanation of GAs* 
 - https://cs.adelaide.edu.au/~zbyszek/Papers/p17.pdf p.9 (Method of Powell & Skolnick)
		"Genetic algorithms (Holland 1975), on the other hand, penalize unfeasible individuals (e.g., Goldberg 1989), however, there is no general rules for designing penalty functions."
		"It might be worthwhile to experiment with methods where penalties are based rather on the distance between a point and the feasible search space: penalty(X)=dist(X;F) such methods provide better results in many combinatorial optimization problems (Richardson et al. 1989)" *Some methods to handle unfeasible solutions in GAs*
 - https://www.hindawi.com/journals/mpe/2015/906305/ (2D chromosomes) Section 3
		"Permutations are a popular representation for some combinatorial optimization problems [6, 22, 23]." *Good ideas (to adapt to 1D) for a GA corresponding to my problem*
 - Mitchell, Melanie (1996). An Introduction to Genetic Algorithms. Cambridge, MA: MIT Press. ISBN 9780585030944
	"(For more technical comparisons of different selection methods, see Goldberg and Deb 1991, Bäck and Hoffmeister 1991, de la Maza and Tidor 1993, and Hancock 1994.)"
	"Schaffer et al. found that the best settings for population size, crossover rate, and mutation rate were independent of the problem in their test suite. These settings were similar to those found by Grefenstette:population size 20–30, crossover rate 0.75–0.95, and mutation rate 0.005–0.01." *A really good summary about GAs* 
 - Peter J. B. Hancock, An Empirical Comparison of Selection Methods in Evolutionary Algorithms *A comparision between the main selection methods, using a simple example*

Paywall:
 - Leonard Kaufman et Peter J. Rousseeuw, Finding Groups in Data – An Introduction to Cluster Analysis, John Wiley & Sons, 1990

Unavailable:
 - R. Forgy, Cluster Analysis of Multivariate Data : Efficiency versus Interpretability of Classification, Biometrics (1965), n°21, 768–769 *One of the original kmeans algorithm*
 - Richardson,J.T., M.R. Palmer, G. Liepinsand and M. Hilliard (1989). Some Guidelines for Genetic Algorithms with Penalty Functions. In Proceedings of the Third International Conference on Genetic Algorithms, Los Altos, CA, Morgan Kaufmann Publishers, 191-197. *How to manage unfeasible solutions using penalty functions*

## Genetic Algorithm
Différentes méthodes de sélection (wheel, avec/sans sigma scaling et windowing; rank; tournament), de réparation
Avec/sans élitisme
3D plot du meilleur résultat (en moyenne ?) en fonction de la probabilité de mutation et de crossover
Paramètres : P(crossover),P(mutation),taille de pop
### Using a 1D-array of the nodes, the position indicating their pools

1. Generate initial population by shuffling interval [|1;n|]
2. Evaluate each chromosome
3. Repeat n/2 times : select 2 chromosome (using their fitness), cross them or not, add the 2 results to the new population
4. Mutate or not the chromosome
5. Back to step 2
