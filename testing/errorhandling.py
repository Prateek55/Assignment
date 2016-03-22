with open("../collisions/error_log_copy") as error_file:
	for line in error_file:
		line=line[:-1]
		line=line.replace("#","")
		if "__P__" in line:
			concept=line.split("__P__")[-1]
			sem=line.split("__P__")[:-1]
			toWrite=concept+"(N) -> "
			for word in sem:
				toWrite+=word+","
			toWrite=toWrite[:-1]
			print toWrite
		if "__N__" in line:
			concept=line.split("__N__")[-1]
			sem=line.split("__N__")[:-1]
			toWrite=concept+"(P) -> "
			for word in sem:
				toWrite+=word+","
			toWrite=toWrite[:-1]
			print toWrite
