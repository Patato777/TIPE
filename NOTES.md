# Notes

variance inter-classes dans le cas du saut de Ward\
d(A,B) = d(gA,gB)x(NaNb)/(Na+Nb) (saut de Ward) http://maths.cnam.fr/IMG/pdf/Classification-2008-2.pdf (p.22)\
CAH (choix des barycentres initiaux)-> réalocation dynamique\
Isodata (Ball & Hall 1965) http://maths.cnam.fr/IMG/pdf/Classification-2008-2.pdf (p.17) "Un certain nombre de contraintes sont imposées pour empêcher la formation de classes d’effectifs trop faibles ou de diamètre trop grand."\
kmeans: montrer la convergence dans le cas du nombre d'éléments par classe fixé (si convergence il y a)\
kmeans: choix des centres de départ : CAH ou kmeans++ ou méthode déjà programmée

TODO:
 - base seeds: plusieurs méthodes: kmeans++, CAH, random, "baseseeds"
 - tests

To read:
 - R. Forgy, Cluster Analysis of Multivariate Data : Efficiency versus Interpretability of Classification, Biometrics (1965), n°21, 768–769
 - E. Diday, The dynamic clusters method in nonhierarchical clustering, International Journal of Computer & Information Sciences 2 (1973), n°1, 61–88.
 - J. A. Hartigan et M. A. Wong, Algorithm AS 136 : a k-means clustering algorithm, Applied Statistics 28 (1979), 100–108.
 - Stuart P. Lloyd. Least squares quantization in pcm. IEEE Transactions on Information Theory, 28(2):129–136, 1982
 - Jir ́ı Matousek. On approximate geometric k-clustering. Discrete & Computational Geometry, 24(1):61–84, 2000.

 Reading:
 - David Arthur and Sergei Vassilvitskii, k-means++: The Advantages of Careful Seeding, 2006 http://ilpubs.stanford.edu:8090/778/1/2006-13.pdf
 
 Finished:
 - Ball, Geoffrey H., Hall, David J. (1965) Isodata: a method of data analysis and pattern classification, Stanford Research Institute, Menlo Park,United States. Office of Naval Research. Information Sciences Branch (https://apps.dtic.mil/dtic/tr/fulltext/u2/699616.pdf) *Nothing to get from*
 - J. Macqueen, Some methods for classification and analysis of multivariate observations, In 5-th Berkeley Symposium on Mathematical Statistics and Probability, 1967, p. 281–297. https://www-m9.ma.tum.de/foswiki/pub/WS2010/CombOptSem/kMeans.pdf (p. 3) *The original definition of kmeans*
 
Paywall:
 - Leonard Kaufman et Peter J. Rousseeuw, Finding Groups in Data – An Introduction to Cluster Analysis, John Wiley & Sons, 1990
