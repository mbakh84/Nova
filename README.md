<strong>Nova, is a basic program to proccess images from a <a href = "https://www.space.com/15396-variable-stars.html" target = "_self">Variable star</a> and draw a linear-graph based on light magnitude of the star🌟.<br>this is my project that i presented in a Scientific festival in high school.</strong><br><br>
at the begining, as the template impage, you should crop an image and spcify a zone around the variable star. this zone most have at least 5 another stars.
then you give all images addresses to program. and here the miracle will begins!

at first, program detects zone in each picture, which is same as template image. then for Reducing the effect of air pollution on the image, Nova scans border of picture. if we have air pollution, the border of a image is brighter than anothers. Nova will reduce this effect and then, it saves datas on a linear-graph.

at last, we have a graph, which shows the change of star's light magnitude.

*template picture is a croped picture, program use it to detect same stars Pattern in other images called zone(images are included the zone)

*make sure that you have installed <strong> CV2 , Numpy & matplotlib </strong>libraries
