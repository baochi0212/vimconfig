Vim�UnDo� i'�ii�es�O�#�Dbʋ�Ÿx�
ԇ���o   +   --save_steps 1000 \   )                          gH.�    _�                             ����                                                                                                                                                                                                                                                                                                                                                             gE��     �         +      "--per_device_train_batch_size 32 \5��                        �                    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             gE��     �         +      !--per_device_train_batch_size 1 \5��                         �                     5�_�                       !    ����                                                                                                                                                                                                                                                                                                                                                             gE��    �         +      #--per_device_train_batch_size 1`` \5��                         �                     5�_�                       #    ����                                                                                                                                                                                                                                                                                                                                                             gE��    �         +      $MODEL_NAME="./checkpoint_spp/bge-m3"5��                        8                     �                        8                     �                        8                     �                        8                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             gF��    �         +      !--per_device_train_batch_size 1 \5��                                            �                                              5�_�                   	       ����                                                                                                                                                                                                                                                                                                                                         T       v   T    gH�    �      
   +      "if [[ $RUN_NAME == debug* ]]; then5��                         P                     5�_�                     )       ����                                                                                                                                                                                                                                                                                                                                                             gH.�    �   (   *   +      --save_steps 1000 \5��    (                 
   �             
       �    (                    �                    �    (                     �                     5�_�                       T    ����                                                                                                                                                                                                                                                                                                                                                             gH'    �         +      Tpython3 -m torch.distributed.run --nproc_per_node $NUM_GPUS -m research.BGE_M3.run \5��       T                 .                     5��