# # Create the config
# config = """
# name: "{name}"

# data:
#     src1: "{source_language1}"
#     trg1: "{target_language1}"
#     src2: "{source_language2}"
#     trg2: "{target_language2}"

#     train1: "{data_dir}/train1.{bpe_size}.bpe"
#     train2: "{data_dir}/train2.{bpe_size}.bpe"

#     dev:   "{data_dir}/dev.{bpe_size}.bpe"
#     test:  "{data_dir}/test.{bpe_size}.bpe"
#     level: "bpe"                    # Here we specify we're working on BPEs.
#     lowercase: False                
#     max_sent_length: 30             # Extend to longer sentences.
#     src_vocab: "{src_vocab_path}"
#     trg_vocab: "{trg_vocab_path}"

# testing:
#     beam_size: 5
#     alpha: 1.0
#     sacrebleu:                      # sacrebleu options
#         remove_whitespace: True     # `remove_whitespace` option in sacrebleu.corpus_chrf() function (defalut: True)
#         tokenize: "intl"            # `tokenize` option in sacrebleu.corpus_bleu() function (options include: "none" (use for already tokenized test data), "13a" (default minimal tokenizer), "intl" which mostly does punctuation and unicode, etc) 

# training:
#     #load_model: "{model_path}/1.ckpt" # if uncommented, load a pre-trained model from this checkpoint
#     random_seed: 42
#     optimizer: "adam"
#     normalization: "tokens"
#     adam_betas: [0.9, 0.999] 
#     scheduling: "plateau"           # Alternative: try switching from plateau to Noam scheduling
#     patience: 5                     # For plateau: decrease learning rate by decrease_factor if validation score has not improved for this many validation rounds.
#     learning_rate_factor: 0.5       # factor for Noam scheduler (used with Transformer)
#     learning_rate_warmup: 1000      # warmup steps for Noam scheduler (used with Transformer)
#     decrease_factor: 0.7
#     loss: "crossentropy"
#     learning_rate: 0.0003
#     learning_rate_min: 0.00000001
#     weight_decay: 0.0
#     label_smoothing: 0.1
#     batch_size: 4096
#     batch_type: "token"
#     eval_batch_size: 3600
#     eval_batch_type: "token"
#     batch_multiplier: 1
#     early_stopping_metric: "ppl"
#     epochs: 30                     # Decrease for when playing around and checking of working. Around 30 is sufficient to check if its working at all
#     validation_freq: 2000          # Set to at least once per epoch.
#     logging_freq: 200
#     eval_metric: "bleu"
#     model_dir: "{model_path}"
#     overwrite: False               # Set to True if you want to overwrite possibly existing models. 
#     shuffle: True
#     use_cuda: True
#     max_output_length: 100
#     print_valid_sents: [0, 1, 2, 3]
#     keep_last_ckpts: 3

#     multitask: True
#     mixing_ratio:[1.0 , 0.1]
#     ref_updates: 1000 #epohs * updates per epoch

# model:
#     initializer: "xavier"
#     bias_initializer: "zeros"
#     init_gain: 1.0
#     embed_initializer: "xavier"
#     embed_init_gain: 1.0
#     tied_embeddings: True        # Joint vocabulary.
#     tied_softmax: True
#     encoder:
#         type: "transformer"
#         num_layers: 6
#         num_heads: 4             # Increase to 8 for larger data.
#         embeddings:
#             embedding_dim: 256   # Increase to 512 for larger data.
#             scale: True
#             dropout: 0.2
#         # typically ff_size = 4 x hidden_size
#         hidden_size: 256         # Increase to 512 for larger data.
#         ff_size: 1024            # Increase to 2048 for larger data.
#         dropout: 0.3
#     decoder:
#         type: "transformer"
#         num_layers: 6
#         num_heads: 4              # Increase to 8 for larger data.
#         embeddings:
#             embedding_dim: 256    # Increase to 512 for larger data.
#             scale: True
#             dropout: 0.2
#         # typically ff_size = 4 x hidden_size
#         hidden_size: 256         # TODO: Increase to 512 for larger data.
#         ff_size: 1024            # TODO: Increase to 2048 for larger data.
#         dropout: 0.3
# """.format(name=experiment_name, 
#            source_language=src_lang, 
#            target_language=trg_lang,
#            data_dir=data_dir, 
#            model_path=model_path, 
#            src_vocab_path=bpe_vocab_file,
#            trg_vocab_path=bpe_vocab_file, 
#            bpe_size=bpe_size)
# with open("transformer_{name}.yaml".format(name=experiment_name),'w') as f:
#     f.write(config)