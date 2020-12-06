class GoogleNetModel(object):
	def __init__(self, model_path):
		self.model = model_path

	def eval(self, image):
		return 1

	def __str__(self):
		return str(self.model)
	
