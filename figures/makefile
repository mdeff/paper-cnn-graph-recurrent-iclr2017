all: moving_mnist.pdf

moving_mnist.pdf: moving_mnist.py
	python moving_mnist.py
	pdfcrop moving_mnist.pdf moving_mnist.pdf

gcnn_rnn.pdf: gcnn_rnn.eps
	repstopdf gcnn_rnn.eps

clean:
	#rm -f gcnn_rnn.pdf
	rm -f moving_mnist.pdf

.PHONY: all clean
