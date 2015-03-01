"""create an encoder which is ready to serialize bokeh examples"""

import json
class SageEncoder(json.JSONEncoder):
  """
  intercept the default encoder by checking for the sage classes
  """
  def default(self, obj):
    """
    intercept sage.rings.integer.Integer and sage.rings.real_mpfr.RealLiteral
    :param obj: object of the intercepted types
    :return: serializable object base on the intercepted type
    """
    if isinstance(obj, sage.rings.integer.Integer):
        return int(obj)
    if isinstance(obj,sage.rings.real_mpfr.RealLiteral):
        return float(obj)
    # Let the base class default method raise the TypeError
    return json.JSONEncoder.default(self, obj)

#
# singleton instance of the class SageEncoder
#
sage_encoder=SageEncoder()

#
# save the old encoder
#
default_encoder=json.JSONEncoder.default

#
# replace old by ours
#
json.JSONEncoder.default=sage_encoder.default