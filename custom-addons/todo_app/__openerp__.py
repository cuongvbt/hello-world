{
	'name': 'To-Do Application',
	'description': 'Manage your personal tasks with this helpful module',
	'author': 'Cuong VBT',
	'depends': ['mail','purchase'],
	'application': True,
	'data': [
		'todo_view.xml',
		'security/ir.model.access.csv',
		'security/todo_access_rules.xml'
	],
}