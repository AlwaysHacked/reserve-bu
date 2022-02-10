def printtitle(text) -> None:
	print('\x1b[94m%s\x1b[0m' % text, end='\t')

def printActiveButton(text: str) -> None:
	print('\x1b[30;42m ' + text + ' \x1b[0m', end='\t')

def printInactiveButton(text: str) -> None:
	print('\x1b[41m %s \x1b[0m' % text, end='\t')
