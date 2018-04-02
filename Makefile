build-cpu:
	docker build -t colemurray/medium-show-and-tell-caption-generator -f Dockerfile .

run-predict:
	docker run -v ${PWD}:/opt/app \
		-e PYTHONPATH=$PYTHONPATH:/opt/app \
		-it colemurray/medium-show-and-tell-caption-generator  \
		python3 /opt/app/medium_show_and_tell_caption_generator/inference.py \
		--model_path /opt/app/etc/show-and-tell.pb \
		--input_files /opt/app/imgs/trading_floor.jpg \
		--vocab_file /opt/app/etc/word_counts.txt
