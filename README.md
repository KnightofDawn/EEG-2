# Kaggle Competition

> Yushi Wang, Jie Fu, Yumeng Yin

This competition was mainly done by `Yushi Wang`. 

Due to the configuration problems with `neon`, we haven't had enough time to tune the hyperparameters. Our solution is first do some filtering in the frequency-domain, and then train a CNN in the space-domain.

---

We put code, experimental procedure, documents, discussion and resources here. As for project management, we use Trello. For light chat, we stick with Gitter.

## Related libraries
* SKlearn
* Neon, https://github.com/NervanaSystems/neon
* Theano, http://deeplearning.net/software/theano/
* Keras
* RoBO
* Hyperopt, https://github.com/hyperopt/hyperopt

## Docs to read
1. https://www.kaggle.com/anlthms/grasp-and-lift-eeg-detection/convnet-0-89   Sample code with `Neon`

## Procedure
1. Do filtering in the frequency-domain
2. Transform back to space-domain, and train deep neural networks
3. Tune hyperparameters using `RoBO` or `hyperopt`


### Folders
When submitting, we create our own folders, such as `fj_submit` - `rnn_baseline`. 

### Documentations
Dense documentation is desired. So put all the thoughts and related stuff in `markdown` files associated with the code and data.
