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

```
@inproceedings{gcrn,
  title = {Structured Sequence Modeling with Graph Convolutional Recurrent Networks},
  author = {Seo, Youngjoo and Defferrard, Micha\"el and Vandergheynst, Pierre and Bresson, Xavier},
  booktitle = {International Conference on Neural Information Processing (ICONIP)},
  year = {2017},
  archiveprefix = {arXiv},
  eprint = {1612.07659},
  url = {https://arxiv.org/abs/1612.07659},
}
```

## Resources

* PDF: [arXiv](https://arxiv.org/abs/1612.07659), [ICONIP](https://doi.org/10.1007/978-3-030-04167-0_33), [EPFL](https://infoscience.epfl.ch/record/227513).
* Reviews: <https://openreview.net/forum?id=S19eAF9ee>
* Code: <https://github.com/youngjoo-epfl/gconvRNN>.

## Compilation

Compile the latex source into a PDF with `make`.
Run `make clean` to remove temporary files and `make arxiv.zip` to prepare an archive to be uploaded on arXiv.

## Figures

All the figures are in the [`figures`](figures/) folder.
PDFs can be generated with `make figures`.
