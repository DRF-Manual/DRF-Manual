@extend_schema{
	# extra parameters added to the schema
	parameters=[
		OpenAPiParameter{name='artist', description='Filter by artist', required=False, type=str},
		OpenAPiParameter{
			name='release',
			type='OpenAPiTypes.DATE',
			location='OpenAPiParameter.QUERY',
			description='Filter by release date',
			examples=[
				OpenAPiExample{
					'example 1',
					summary='short optional summary',
					description='longer description',
					value='1993-08-23',
				},
				...
			],
		},
	],
	# operride default docstring extraction
	description='',
	# provide Authentication class that deviates from the views default
	auth=None,
	# change the auto-generated operation name
	operation_id=None,
	# or even completely override what AutoSchema would generate. Provide raw Open API spec as Dict.
	operation=None,
	# attach request/response examples to the operation.
	examples=[
		OpenAPiExample{
			'Example 1',
			description='longer description',
			value='...',
		},
		...
	],
}