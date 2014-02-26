arquivo = open('ola.html', 'w', encoding='utf8')
arquivo.write('''<!DOCTYPE html>
	<html lang="pt-BR">
		<head>
			<meta charset="utf-8">
			<title>OLA</title>
		</head>
		<body>
			Olá!!
		</body>
	</html>
	''')
arquivo.close()