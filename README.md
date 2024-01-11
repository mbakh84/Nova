<strong>Nova, is a basic programm to proccess images from a <a href = "https://www.space.com/15396-variable-stars.html" target = "_self">Variable star</a> and draw a linear-graph based on light magnitude of the star🌟.	</strong>




at the begining, as the template impage, you should crop an image and spcify a zone around the variable star. this zone most have at least 5 another stars.
then you give all images addresses to programm. and here the miracle will begins!

at first, program detects zone, which is same as template image. then for Reducing the effect of air pollution on the image, Nova scans border of picture. if we have air pollution, the border of a image is brighter than anothers. Nova will reduce this effect and then, it saves datas on a linear-graph.

at last, we have a graph, which shows the change of star's light magnitude.

*make sure that you installed <strong> CV2 , Numpy & matplotlib </strong>libraries
