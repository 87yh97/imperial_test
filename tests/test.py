import select
import subprocess

def get_conversion(self, source_unit, target_unit, source_value, precision):
       
       	converter = subprocess.Popen(	
       		["python3", "src/converter.py", "--from", source_unit, "--to", target_unit, "--precision", str(precision)], 
       		stdin=subprocess.PIPE,
       		stdout=subprocess.PIPE,
       		stderr=subprocess.STDOUT,
       		text = True,
       		bufsize = 1024
       	)
       
       
       	rready, _, _ = select.select([converter.stdout], [], [], 1)
       	while len(rready) > 0:
       		rready, _, _ = select.select([converter.stdout], [], [], 1)
       		converter.stdout.read(1)
       
       
       	outs, errs = converter.communicate(input=str(source_value))
       	number = outs.split(" ").pop().strip()
       	return number	

class TestConverter():

	def test_inches_to_metre(self):
		number = get_conversion(self, "inches", "metre", 1, 2)
		assert number == '0.03'		
	
	def test_yards_to_inches(self):
		number = get_conversion(self, "yards", "inches", 13.4, 3)
		assert number == '482.4'		
	
	def test_mm_to_mile(self):
		number = get_conversion(self, "mm", "mile", 9817256, 10)
		assert number == '6.1001600652'		





