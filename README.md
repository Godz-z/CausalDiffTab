# CausalDiffTab: Mixed-Type Causal-Aware Diffusion for Tabular Data Generation

## Latest Update

- [2025.07]：Our code is released!

## Environment Setup

Create the main environment with CausalDiffTab.yaml. This environment will be used for all tasks except for the evaluation of additional data fidelity metrics (i.e., $\alpha$-precision and $\beta$-recall scores)

```
conda env create -f CausalDiffTab.yaml
```

Create another environment with [synthcity.yaml](synthcity.yaml) to evaluate additional data fidelity metrics

```
conda env create -f synthcity.yaml
```

## Datasets Preparation

### Using the datasets experimented in the paper

Download raw datasets:

```
python download_dataset.py
```

Process datasets:

```
python process_dataset.py
```

## Training CausalDiffTab

To train an unconditional CausalDiffTab model across the entire table, run

```
python main.py --dataname <NAME_OF_DATASET> --mode train
```

Current Options of ```<NAME_OF_DATASET>``` are: adult, default, shoppers, magic, beijing, news

Wanb logging is enabled by default. To disable it and log locally, add the ```--no_wandb``` flag.

To disable the learnable noise schedules, add the ```--non_learnable_schedule```. Please note that in order for the code to test/sample from such model properly, you need to add this flag for all commands below.

To specify your own experiment name, which will be used for logging and saving files, add ```--exp_name <your experiment name>```. This flag overwrites the default experiment name (learnable_schedule/non_learnable_schedule), so, similar to ```--non_learnable_schedule```, once added to training, you need to add it to all following commands as well.

## Sampling and Evaluating CausalDiffTab (Density, MLE, C2ST)

To sample synthetic tables from trained CausalDiffTab models and evaluate them, run
```
python main.py --dataname <NAME_OF_DATASET> --mode test --report --no_wandb
```

This will sample 20 synthetic tables randomly. Meanwhile, it will evaluate the density, mle, and c2st scores for each sample and report their average and standard deviation. The results will be printed out in the terminal, and the samples and detailed evaluation results will be placed in ./eval/report_runs/<EXP_NAME>/<NAME_OF_DATASET>/.

## Evaluating on Additional Fidelity Metrics ($\alpha$-precision and $\beta$-recall scores)
To evaluate TabDiff on the additional fidelity metrics ($\alpha$-precision and $\beta$-recall scores), you need to first make sure that you have already generated some samples by the previous commands. Then, you need to switch to the `synthcity` environment (as the synthcity packet used to compute those metrics conflicts with the main environment), by running
```
conda activate synthcity
```
Then, evaluate the metrics by running
```
python eval/eval_quality.py --dataname <NAME_OF_DATASET>
```

Similarly, the results will be printed out in the terminal and added to ./eval/report_runs/<EXP_NAME>/<NAME_OF_DATASET>/

## Acknowledgement
This repo is built upon the previous work Tabdiff's [[codebase]](https://github.com/MinkaiXu/TabDiff).
