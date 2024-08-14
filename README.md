# huggingface-transformers

## Setup on NERSC

Log into Perlmutter with your credentials.

```
export PROJECT_ID={project_id}
export USERNAME={username}

module load python
module load pytorch/2.3.1

cd $CFS/$PROJECT_ID/users/$USERNAME

git clone https://github.com/vganapati/huggingface-transformers.git

cd huggingface-transformers

conda create -n huggingface
conda activate huggingface
pip install "transformers[sentencepiece]"
```

Create a file with all the setup parameters in your home directory:
```
cd $HOME
vi env_hugging_face
```

Copy in the following:
```
export PROJECT_ID={project_id}
export USERNAME={username}
module load python
module load pytorch/2.3.1
cd $CFS/$PROJECT_ID/users/$USERNAME/huggingface-transformers
conda activate huggingface
```

## Start up 

```
source ~/env_hugging_face
```