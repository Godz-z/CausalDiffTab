# python main.py --dataname adult --mode train --no_wandb --exp_name test;
# python main.py --dataname default --mode train --no_wandb --exp_name 1our;
# python main.py --dataname shoppers --mode train --no_wandb --exp_name 1our;
# python main.py --dataname magic --mode train --no_wandb --exp_name 1our;
# python main.py --dataname beijing --mode train --no_wandb --exp_name 1our;
# python main.py --dataname news --mode train --no_wandb --exp_name 1our;
# python main.py --dataname adult --mode test --report --no_wandb --exp_name 1our;
# python main.py --dataname default --mode test --report --no_wandb --exp_name 1our;
# python main.py --dataname shoppers --mode test --report --no_wandb --exp_name 1our;
# python main.py --dataname magic --mode test --report --no_wandb --exp_name 1our;
# python main.py --dataname beijing --mode test --report --no_wandb --exp_name 1our;
# python main.py --dataname news --mode test --report --no_wandb --exp_name 1our;
# python main.py --dataname magic --mode test --report --no_wandb --exp_name 1our;
# python main.py --dataname shoppers --exp_name test2 --mode train --no_wandb;
# python main.py --dataname shoppers --mode test --report --no_wandb --exp_name test2;
# python main.py --dataname beijing --exp_name test4 --mode train --no_wandb;
# python main.py --dataname beijing --mode test --report --no_wandb --exp_name test4;
# python main.py --dataname news --exp_name test2 --mode train --no_wandb;
# python main.py --dataname news --mode test --report --no_wandb --exp_name test2;
# python main.py --dataname adult_dcr --mode train --no_wandb --exp_name 4;
# python main.py --dataname default_dcr --mode train --no_wandb --exp_name 4;
# python main.py --dataname shoppers_dcr --mode train --no_wandb --exp_name 4;
# python main.py --dataname beijing_dcr --mode train --no_wandb --exp_name 4;
# python main.py --dataname news_dcr --mode train --no_wandb --exp_name 4;
# python main.py --dataname adult_dcr --mode test --report --no_wandb --exp_name 4;
# python main.py --dataname default_dcr --mode test --report --no_wandb --exp_name 4;
# python main.py --dataname shoppers_dcr --mode test --report --no_wandb --exp_name 4;
# python main.py --dataname beijing_dcr --mode test --report --no_wandb --exp_name 4;
# python main.py --dataname news_dcr --mode test --report --no_wandb --exp_name ;
# python eval/eval_quality.py --dataname default --exp_name test;
# python eval/eval_quality.py --dataname magic --exp_name ours12;
# python eval/eval_quality.py --dataname shoppers --exp_name ours12;
# python eval/eval_quality.py --dataname default --exp_name ours13;
python main.py --dataname diabetes --mode train --no_wandb --exp_name test
python main.py --dataname diabetes --mode test --exp_name test --report --no_wandb
python main.py --dataname diabetes --mode test --exp_name test --no_wandb
python main.py --dataname beijing --mode test --exp_name tabdiff --no_wandb
python main.py --dataname default --mode test --exp_name test --no_wandb
python main.py --dataname magic --mode test --exp_name tabdiff --no_wandb
python eval/eval_quality.py --dataname diabetes --exp_name test