import survey

table = survey.Pregnancies()
table.ReadRecords()
print('Number of pregnancies', len(table.records))

liveBirthsFirst = 0
liveBirthsOthers = 0
pregWeeksFirst = 0
pregWeeksOthers = 0
for record in table.records:
	if record.outcome == 1:
		if record.birthord == 1:
			liveBirthsFirst+=1
			pregWeeksFirst+=record.prglength
		else:
			liveBirthsOthers+=1
			pregWeeksOthers+=record.prglength
print("Number of Live Births for first babies", liveBirthsFirst)
print("Number of Live Births for other babies", liveBirthsOthers)
print("Average Number of Pregnancy weeks for First babies", pregWeeksFirst/liveBirthsFirst)
print("Average Number of Pregnancy weeks for Other babies", pregWeeksOthers/liveBirthsOthers)
