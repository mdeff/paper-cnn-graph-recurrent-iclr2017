# Structured Sequence Modeling with Graph Convolutional Recurrent Networks

[Youngjoo Seo](https://www.linkedin.com/in/youngjooseo),
[Michaël Defferrard](https://deff.ch),
[Pierre Vandergheynst](https://people.epfl.ch/pierre.vandergheynst),
[Xavier Bresson](https://www.ntu.edu.sg/home/xbresson), \
International Conference on Neural Information Processing (ICONIP), 2017.

> This paper introduces Graph Convolutional Recurrent Network (GCRN), a deep learning model able to predict structured sequences of data.
> Precisely, GCRN is a generalization of classical recurrent neural networks (RNN) to data structured by an arbitrary graph.
> Such structured sequences can represent series of frames in videos, spatio-temporal measurements on a network of sensors, or random walks on a vocabulary graph for natural language modeling.
> The proposed model combines convolutional neural networks (CNN) on graphs to identify spatial structures and RNN to find dynamic patterns.
> We study two possible architectures of GCRN, and apply the models to two practical problems: predicting moving MNIST data, and modeling natural language with the Penn Treebank dataset.
> Experiments show that exploiting simultaneously graph spatial and dynamic information about data can improve both precision and learning speed.
