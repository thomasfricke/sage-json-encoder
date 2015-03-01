# Integrate bokeh plots into SageMath

## [Bokeh](https://github.com/bokeh/bokeh) 

is a feature rich plotting program

## [Sage aka SageMath](http://www.sagemath.org/) 

is the richest collection and integration of math tools I know.
 
 
You can easily install `bokeh` in Sage using

```
$sage -sh
$easy_install bokeh
```

However, serialisation of bokeh objects and talking to the bokeh server fails.
This behaviour can be traced back to the missing types in
the default encoder

```
sage: json.dumps( {'a': 1 })
.
.
.
TypeError: 1 is not JSON serializable
``` 

Adding the `sage_json_encoder.py` to your project fixes this, and the basic examples could be tested.