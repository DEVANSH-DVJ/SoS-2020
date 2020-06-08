file = open('MIT 6.042J.tex', 'w')

for i in range(23, 78):
	file.write('\\newpage\n\\begin{figure}[H]\n    \\centering\n    \\includegraphics[scale=0.25]{"./MIT-6.042J/MIT-6042J-')
	if i in range(1, 10):
		file.write('00' + str(i))
	if i in range(10, 100):
		file.write('0' + str(i))
	if i in range(100, 1000):
		file.write(str(i))
	file.write('"}\n\\end{figure}\n')
