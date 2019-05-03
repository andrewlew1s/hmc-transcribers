# Bizniz

## Welcome to our 121 Software Development project's github repo! 
Bizniz is a business card transcriber power by deep learning. Either explore the app at [Bizniz](http://hmc-121-transcribers-hmcscribes.s3-website-us-west-2.amazonaws.com/) or follow the following instructions to run the app on your own machine. 

## Launch the front-end
### Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


## Launch the API
In the base directory of the repository simply run:
```
gunicorn --bind 0.0.0.0:8000 wsgi
```

Small caveat, due to Github restrictions on large files, neither of the models employed in our API are in the repository. Those files can be access at [Image Segmentation Model](https://drive.google.com/open?id=1-4Yttk9XY4W1O4Db9pojBt8xZkVIDE_j) and [Text classification model](https://drive.google.com/open?id=1-Ck33p3o9LZum5M6n6QhiUCjXi94_rmf).
