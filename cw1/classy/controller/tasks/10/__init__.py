"""
[Clustering, k-means] Cluster the data sets train_smpl, train_smpl_<label> (apply required
filters and/or attribute selections if needed), using the k-means algorithm:
● first excluding the class attribute (use classes to clusters evaluation to achieve this). This will
emulate the situation when the learning is performed in unsupervised manner.
● then including the class attribute. This will emulate the general data analysis scenario.

"""