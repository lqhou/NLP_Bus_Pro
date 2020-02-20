# 使用BERT实现疫情谣言的自动判别

## 目录说明：

bert_master：Google官方提供的代码\\
bert_model_zh_cn：官方提供的基于中文的预训练好的BERT模型\\
data：实验使用的数据\\
get_data：爬取腾讯较真平台数据的代码\\
output：预测阶段的输出存放在此\\
saved_model：保存我们基于自己的数据微调后训练好的BERT模型（使用疫情数据、含部分微博数据）\\
saved_model_ori：保存我们基于自己的数据微调后训练好的BERT模型（使用微博数据）\\
calculate_acc.py：基于预测结果计算混淆矩阵和准确率\\
fake_news_classifier.py：基于BERT实现分类的代码部分\\

## 训练和预测

训练：python3 fake_news_classifier.py --task_name=fake_news --do_train=true --do_eval=true --data_dir=./data/ --vocab_file=./bert_model_zh_cn/vocab.txt --bert_config_file=./bert_model_zh_cn/bert_config.json --init_checkpoint=./bert_model_zh_cn/bert_model.ckpt --max_seq_length=128 --train_batch_size=8 --learning_rate=2e-5 --num_train_epochs=3.0 --output_dir=./saved_model/

预测：python3 fake_news_classifier.py --task_name=fake_news --do_predict=true --data_dir=./data/ --vocab_file=./bert_model_zh_cn/vocab.txt --bert_config_file=./bert_model_zh_cn/bert_config.json --init_checkpoint=./saved_model/ --max_seq_length=128 --output_dir=./output


由于模型的文件较大，请在公众号后台回复“fake news”获取云盘链接。