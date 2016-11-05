def getVisitData():
    data = {}
    data = _getDummyData(data)
    data = _getMonData(data)
    data = _getTueData(data)
    data = _getWedData(data)
    data = _getThuData(data)
    data = _getFriData(data)
    return data

def _getMonData(data, date = "11/07/2016"):
    data[date] = []
    event = {}
    event['startTime'] = "9:00"
    event['endTime'] = "10:00"
    event['title'] = "Morning Standup - Weta Crew"
    event['location'] = "Weta Office (The Locked Room)"
    event['attendees'] = sorted(["Tim", "Ronald", "Wil", "Allen", "Bex", "Ken",
                                 "Justin R.", "Justin S.", "Damon", "Corey", "Patrick"])
    data[date].append(event)

    event = {}
    event['startTime'] = "10:00"
    event['endTime'] = "11:00"
    event['title'] = "Kick Off / Meet & Greet"
    event['location'] = "Stage 26"
    event['attendees'] = sorted(["Tim", "Ronald", "Wil", "Allen", "Bex", "Ken",
                                 "Justin R.", "Justin S.", "Damon", "Corey", "Patrick"])
    data[date].append(event)

    event = {}
    event['startTime'] = "11:00"
    event['endTime'] = "12:00"
    event['title'] = "Dan F. - Timeline View / Usability Testing"
    event['location'] = "Wheels Room"
    event['attendees'] = sorted(["Corey"])
    data[date].append(event)

    event = {}
    event['startTime'] = "11:00"
    event['endTime'] = "12:00"
    event['title'] = "Damon goes to Stage"
    event['location'] = "Stage 26"
    event['attendees'] = sorted(["Damon"])
    data[date].append(event)

    event = {}
    event['startTime'] = "11:00"
    event['endTime'] = "13:00"
    event['title'] = "T4 Highlights in Depth / Demo"
    event['location'] = "2nd Floor Conference Room"
    event['attendees'] = sorted(["VPSP"])
    data[date].append(event)

    event = {}
    event['startTime'] = "11:00"
    event['endTime'] = "13:00"
    event['title'] = "Install 11.5 on SBX with LEI Systems"
    event['location'] = "2nd Floor Conference Room"
    event['attendees'] = sorted(["Ronald"])
    data[date].append(event)

    event = {}
    event['startTime'] = "12:00"
    event['endTime'] = "13:00"
    event['title'] = "wtMigrate Demo"
    event['location'] = "Wheels Room"
    event['attendees'] = sorted(["Damon", "Corey", "Patrick"])
    data[date].append(event)

    event = {}
    event['startTime'] = "13:00"
    event['endTime'] = "14:00"
    event['title'] = "LUNCH"
    event['location'] = ""
    event['attendees'] = sorted(["All Crew"])
    data[date].append(event)

    event = {}
    event['startTime'] = "14:00"
    event['endTime'] = "16:00"
    event['title'] = "Meet Mitoki Nishii"
    event['location'] = "Artist Desk"
    event['attendees'] = sorted(["Corey", "Damon"])
    data[date].append(event)

    event = {}
    event['startTime'] = "14:00"
    event['endTime'] = "18:00"
    event['title'] = "Ronald and Wil Collaboration"
    event['location'] = "At Desks"
    event['attendees'] = sorted(["Ronald", "Wil"])
    data[date].append(event)

    event = {}
    event['startTime'] = "14:00"
    event['endTime'] = "16:00"
    event['title'] = "T4 Post Mortem"
    event['location'] = "1st Floor Conference Room"
    event['attendees'] = sorted(["VPSP", "Justin R.", "Tim"])
    data[date].append(event)

    event = {}
    event['startTime'] = "16:00"
    event['endTime'] = "18:00"
    event['title'] = "Meet Stevie Deane"
    event['location'] = "Artist Desk"
    event['attendees'] = sorted(["Corey", "Damon"])
    data[date].append(event)

    event = {}
    event['startTime'] = "16:00"
    event['endTime'] = "17:00"
    event['title'] = "T5 Requirements Gathering (outline)"
    event['location'] = "1st Floor Conference Room"
    event['attendees'] = sorted(["VPSP", "Justin R.", "Tim"])
    data[date].append(event)

    event = {}
    event['startTime'] = "17:00"
    event['endTime'] = "18:00"
    event['title'] = "T5 Requirements Gathering (stage % LAB priorities)"
    event['location'] = "1st Floor Conference Room"
    event['attendees'] = sorted(["VPSP", "Justin R.", "Tim"])
    data[date].append(event)

    event = {}
    event['startTime'] = "18:00"
    event['endTime'] = "19:00"
    event['title'] = "Daily Recap"
    event['location'] = "Weta Office (The Locked Room)"
    event['attendees'] = sorted(["Tim", "Ronald", "Wil", "Allen", "Bex", "Ken",
                                 "Justin R.", "Justin S.", "Damon", "Corey", "Patrick"])
    data[date].append(event)
    return data

def _getTueData(data, date = "11/08/2016"):
    data[date] = []
    event = {}
    event['startTime'] = "9:00"
    event['endTime'] = "10:00"
    event['title'] = "Morning Standup - Weta Crew"
    event['location'] = "Weta Office (The Locked Room)"
    event['attendees'] = sorted(["Tim", "Ronald", "Wil", "Allen", "Bex", "Ken",
                                 "Justin R.", "Justin S.", "Damon", "Corey", "Patrick"])
    data[date].append(event)

    event = {}
    event['startTime'] = "10:00"
    event['endTime'] = "11:00"
    event['title'] = "Software and Deployment Training for IT Support"
    event['location'] = "Level 3, 6B"
    event['attendees'] = sorted(["Ronald", "Wil", "Tim", "(TimB)"])
    data[date].append(event)

    event = {}
    event['startTime'] = "10:00"
    event['endTime'] = "11:00"
    event['title'] = "Constraints / Jitter"
    event['location'] = "1st Floor Conference Room"
    event['attendees'] = sorted(["Justin R.", "Allen", "(Albert)", "(DanN)"])
    data[date].append(event)

    event = {}
    event['startTime'] = "10:00"
    event['endTime'] = "12:00"
    event['title'] = "Corey and Damon go to Stage"
    event['location'] = "Stage 26"
    event['attendees'] = sorted(["Corey", "Damon"])
    data[date].append(event)

    event = {}
    event['startTime'] = "11:00"
    event['endTime'] = "12:00"
    event['title'] = "BlueJeans, RGS for Debugging"
    event['location'] = "1st Floor Conference Room"
    event['attendees'] = sorted(["Ronald", "Wil", "Justin R.", "Tim", "(TimB)"])
    data[date].append(event)

    event = {}
    event['startTime'] = "12:00"
    event['endTime'] = "13:00"
    event['title'] = "wetaos and Filesystem Configuration"
    event['location'] = "1st Floor Conference Room"
    event['attendees'] = sorted(["Ronald", "Wil", "Damon", "(TimB)"])
    data[date].append(event)

    event = {}
    event['startTime'] = "12:00"
    event['endTime'] = "13:00"
    event['title'] = "Stage Operator Speed"
    event['location'] = "Stage 26"
    event['attendees'] = sorted(["Justin R.", "Allen", "(DanN)"])
    data[date].append(event)

    event = {}
    event['startTime'] = "13:00"
    event['endTime'] = "14:00"
    event['title'] = "LUNCH"
    event['location'] = ""
    event['attendees'] = sorted(["All Crew"])
    data[date].append(event)

    event = {}
    event['startTime'] = "14:00"
    event['endTime'] = "15:00"
    event['title'] = "Weta team skype call to WGTN"
    event['location'] = "1st Floor Conference Room"
    event['attendees'] = sorted(["Tim", "Ronald", "Wil", "Allen", "Bex", "Ken", "VPSP",
                                 "Justin R.", "Justin S.", "Damon", "Corey", "Patrick"])
    data[date].append(event)

    event = {}
    event['startTime'] = "15:00"
    event['endTime'] = "18:00"
    event['title'] = "Pre-scout in 11.1"
    event['location'] = "Stage 26"
    event['attendees'] = sorted(["Corey", "Justin R.", "Allen", "Ronald", "Damon", "Tim", "VPSP"])
    data[date].append(event)

    event = {}
    event['startTime'] = "18:00"
    event['endTime'] = "19:00"
    event['title'] = "Daily Recap"
    event['location'] = "Weta Office (The Locked Room)"
    event['attendees'] = sorted(["Tim", "Ronald", "Wil", "Allen", "Bex", "Ken",
                                 "Justin R.", "Justin S.", "Damon", "Corey", "Patrick"])
    data[date].append(event)
    return data

def _getWedData(data, date = "11/09/2016"):
    data[date] = []
    event = {}
    event['startTime'] = "9:00"
    event['endTime'] = "10:00"
    event['title'] = "Morning Standup - Weta Crew"
    event['location'] = "Weta Office (The Locked Room)"
    event['attendees'] = sorted(["Tim", "Ronald", "Wil", "Allen", "Bex", "Ken",
                                 "Justin R.", "Justin S.", "Damon", "Corey", "Patrick"])
    data[date].append(event)

    event = {}
    event['startTime'] = "10:00"
    event['endTime'] = "11:00"
    event['title'] = "LEI scriptShelf follow up"
    event['location'] = "1st Floor Conference Room"
    event['attendees'] = sorted(["Ronald", "Wil", "Tim", "(DanN)"])
    data[date].append(event)

    event = {}
    event['startTime'] = "10:00"
    event['endTime'] = "11:00"
    event['title'] = "Stage Operator Speed (part II)"
    event['location'] = "Stage 26"
    event['attendees'] = sorted(["Allen", "Justin R.", "(DanF)"])
    data[date].append(event)

    event = {}
    event['startTime'] = "10:00"
    event['endTime'] = "11:30"
    event['title'] = "Meet Paolo Ziemba"
    event['location'] = "Artist Desk"
    event['attendees'] = sorted(["Damon", "Corey"])
    data[date].append(event)

    event = {}
    event['startTime'] = "11:00"
    event['endTime'] = "12:00"
    event['title'] = "Environment Management for LEI Leads & support"
    event['location'] = "1st Floor Conference Room"
    event['attendees'] = sorted(["Allen", "(Dean)", "(Albert)", "(DanN)", "(DanF)", "RyanC", "Ronald", "(TimB)"])
    data[date].append(event)

    event = {}
    event['startTime'] = "11:30"
    event['endTime'] = "13:00"
    event['title'] = "Meet Connor Gartland"
    event['location'] = "Artist Desk"
    event['attendees'] = sorted(["Damon", "Corey"])
    data[date].append(event)

    event = {}
    event['startTime'] = "12:00"
    event['endTime'] = "13:00"
    event['title'] = "Oz5 Adoption"
    event['location'] = "3rd Floor"
    event['attendees'] = sorted(["Ronald", "(TimB)"])
    data[date].append(event)

    event = {}
    event['startTime'] = "12:00"
    event['endTime'] = "13:00"
    event['title'] = "Publishing Dialog"
    event['location'] = "1st Floor Conference Room"
    event['attendees'] = sorted(["Tim", "(Albert)", "(Dean)", "(DanN)", "(Mitoki)", "Patrick"])
    data[date].append(event)

    event = {}
    event['startTime'] = "13:00"
    event['endTime'] = "14:00"
    event['title'] = "LUNCH"
    event['location'] = ""
    event['attendees'] = sorted(["All Crew"])
    data[date].append(event)

    event = {}
    event['startTime'] = "14:00"
    event['endTime'] = "15:00"
    event['title'] = "Weta team skype call to WGTN"
    event['location'] = "Weta Office (The Locked Room)"
    event['attendees'] = sorted(["Ronald", "Wil", "Allen", "Bex", "Ken",
                                 "Justin R.", "Justin S.", "VPSP", "Patrick"])

    event = {}
    event['startTime'] = "14:00"
    event['endTime'] = "15:00"
    event['title'] = "LAB Issues, High Level"
    event['location'] = "Weta Office (The Locked Room)"
    event['attendees'] = sorted(["Tim", "Justin R.", "(Albert)", "(Dean)", "(Mitoki)"])

    event = {}
    event['startTime'] = "14:00"
    event['endTime'] = "16:00"
    event['title'] = "Meet Christina Hall"
    event['location'] = "Artist Desk"
    event['attendees'] = sorted(["Damon", "Corey"])
    data[date].append(event)

    event = {}
    event['startTime'] = "15:00"
    event['endTime'] = "16:00"
    event['title'] = "QSMQ"
    event['location'] = "1st Floor Conference Room"
    event['attendees'] = sorted(["Christophe", "Ronald", "Wil", "Tim", "(TimB)"])
    data[date].append(event)

    event = {}
    event['startTime'] = "15:00"
    event['endTime'] = "17:00"
    event['title'] = "Ronald with IT"
    event['location'] = "3rd Floor"
    event['attendees'] = sorted(["Ronald"])
    data[date].append(event)

    event = {}
    event['startTime'] = "16:00"
    event['endTime'] = "17:00"
    event['title'] = "Meet Dean Lewandowski"
    event['location'] = "Artist Desk"
    event['attendees'] = sorted(["Corey"])
    data[date].append(event)

    event = {}
    event['startTime'] = "16:00"
    event['endTime'] = "17:00"
    event['title'] = "Athena Plugins"
    event['location'] = "1st Floor Conference Room"
    event['attendees'] = sorted(["Damon", "Tim", "(DanN)", "(Devs)"])
    data[date].append(event)

    event = {}
    event['startTime'] = "17:00"
    event['endTime'] = "18:00"
    event['title'] = "Hydra and Entity Requirements"
    event['location'] = "1st Floor Conference Room"
    event['attendees'] = sorted(["Tim", "Wil", "Ron", "(TimB)"])
    data[date].append(event)

    event = {}
    event['startTime'] = "17:00"
    event['endTime'] = "18:00"
    event['title'] = "Meet Dean Lewandowski"
    event['location'] = "Artist Desk"
    event['attendees'] = sorted(["Corey", "Damon"])
    data[date].append(event)

    event = {}
    event['startTime'] = "18:00"
    event['endTime'] = "19:00"
    event['title'] = "Daily Recap"
    event['location'] = "Weta Office (The Locked Room)"
    event['attendees'] = sorted(["Tim", "Ronald", "Wil", "Allen", "Bex", "Ken",
                                 "Justin R.", "Justin S.", "Damon", "Corey", "Patrick"])
    data[date].append(event)
    return data

def _getThuData(data, date = "11/10/2016"):
    data[date] = []
    event = {}
    event['startTime'] = "9:00"
    event['endTime'] = "10:00"
    event['title'] = "Morning Standup - Weta Crew"
    event['location'] = "Weta Office (The Locked Room)"
    event['attendees'] = sorted(["Tim", "Ronald", "Wil", "Allen", "Bex", "Ken",
                                 "Justin R.", "Justin S.", "Damon", "Corey", "Patrick"])
    data[date].append(event)

    event = {}
    event['startTime'] = "10:00"
    event['endTime'] = "11:00"
    event['title'] = "Damon & Corey go to Stage"
    event['location'] = "Stage 26"
    event['attendees'] = sorted(["Damon", "Corey"])
    data[date].append(event)

    event = {}
    event['startTime'] = "10:00"
    event['endTime'] = "11:00"
    event['title'] = "Picasso"
    event['location'] = "1st Floor Conference Room"
    event['attendees'] = sorted(["Allen", "Patrick", "Tim", "Ken", "(Albert)", "(Dean)", "(Mitoki)", "(DanN)", "Justin R."])
    data[date].append(event)

    event = {}
    event['startTime'] = "10:00"
    event['endTime'] = "13:00"
    event['title'] = "Ronald with IT"
    event['location'] = "3rd Floor"
    event['attendees'] = sorted(["Ronald"])
    data[date].append(event)

    event = {}
    event['startTime'] = "11:00"
    event['endTime'] = "12:00"
    event['title'] = "Action Menu Setup"
    event['location'] = "Stage 26"
    event['attendees'] = sorted(["Corey", "Damon", "Justin R.", "Patrick", "(DanN)", "(Albert)", "(Dean)", "(Mitoki)"])
    data[date].append(event)

    event = {}
    event['startTime'] = "12:00"
    event['endTime'] = "13:00"
    event['title'] = "Damon & Corey on Stage"
    event['location'] = "Stage 26"
    event['attendees'] = sorted(["Damon", "Corey"])
    data[date].append(event)

    event = {}
    event['startTime'] = "12:00"
    event['endTime'] = "13:00"
    event['title'] = "Taxonomic Tagging follow up"
    event['location'] = ""
    event['attendees'] = sorted(["Tim", "(DanN)"])
    data[date].append(event)

    event = {}
    event['startTime'] = "13:00"
    event['endTime'] = "14:00"
    event['title'] = "LUNCH"
    event['location'] = ""
    event['attendees'] = sorted(["All Crew"])
    data[date].append(event)

    event = {}
    event['startTime'] = "14:00"
    event['endTime'] = "15:00"
    event['title'] = "Weta team skype call to WGTN"
    event['location'] = "Weta Office (The Locked Room)"
    event['attendees'] = sorted(["Ronald", "Wil", "Allen", "Bex", "Ken",
                                 "Justin R.", "Justin S.", "VPSP", "Patrick"])

    event = {}
    event['startTime'] = "15:00"
    event['endTime'] = "18:00"
    event['title'] = "Pre Scout in 11.5"
    event['location'] = "Stage 26"
    event['attendees'] = sorted(["Tim", "Ronald", "Wil", "Allen", "Bex", "Ken", "VPSP",
                                 "Justin R.", "Justin S.", "Damon", "Corey", "Patrick"])
    data[date].append(event)

    event = {}
    event['startTime'] = "18:00"
    event['endTime'] = "19:00"
    event['title'] = "Daily Recap"
    event['location'] = "Stage 26"
    event['attendees'] = sorted(["Tim", "Ronald", "Wil", "Allen", "Bex", "Ken",
                                 "Justin R.", "Justin S.", "Damon", "Corey", "Patrick"])
    data[date].append(event)

    event = {}
    event['startTime'] = "19:00"
    event['endTime'] = "23:00"
    event['title'] = "WETA Crew Dinner"
    event['location'] = "Some place delicious"
    event['attendees'] = sorted(["Tim", "Ronald", "Wil", "Allen", "Bex", "Ken",
                                 "Justin R.", "Justin S.", "Damon", "Corey", "Patrick"])
    data[date].append(event)
    return data

def _getFriData(data, date = "11/11/2016"):
    data[date] = []
    event = {}
    event['startTime'] = "9:00"
    event['endTime'] = "10:00"
    event['title'] = "Morning Standup - Weta Crew"
    event['location'] = "Weta Office (The Locked Room)"
    event['attendees'] = sorted(["Tim", "Ronald", "Wil", "Allen", "Bex", "Ken",
                                 "Justin R.", "Justin S.", "Damon", "Corey", "Patrick"])
    data[date].append(event)

    event = {}
    event['startTime'] = "10:00"
    event['endTime'] = "12:00"
    event['title'] = "Split up / Confirm Consolidation for T5 with LEI"
    event['location'] = "Various Locations"
    event['attendees'] = sorted(["Tim", "Ronald", "Wil", "Allen", "Bex", "Ken",
                                 "Justin R.", "Justin S.", "Damon", "Corey", "Patrick"])
    data[date].append(event)

    event = {}
    event['startTime'] = "12:00"
    event['endTime'] = "13:00"
    event['title'] = "Re-consolidate, align on T5"
    event['location'] = "Weta Office (The Locked Room)"
    event['attendees'] = sorted(["Tim", "Ronald", "Wil", "Allen", "Bex", "Ken",
                                 "Justin R.", "Justin S.", "Damon", "Corey", "Patrick"])
    data[date].append(event)

    event = {}
    event['startTime'] = "13:00"
    event['endTime'] = "14:00"
    event['title'] = "LUNCH"
    event['location'] = ""
    event['attendees'] = sorted(["All Crew"])
    data[date].append(event)

    event = {}
    event['startTime'] = "14:00"
    event['endTime'] = "16:00"
    event['title'] = "T5 Confirmation and Prioritization"
    event['location'] = "Stage 26"
    event['attendees'] = sorted(["Tim", "Ronald", "Wil", "Allen", "Bex", "Ken", "VPSP",
                                 "Justin R.", "Justin S.", "Damon", "Corey", "Patrick"])
    data[date].append(event)

    event = {}
    event['startTime'] = "16:00"
    event['endTime'] = "17:00"
    event['title'] = "NZ Crew departs for Airport"
    event['location'] = ""
    event['attendees'] = sorted(["Tim", "Ronald", "Bex", "Ken", "Justin R.", "Justin S.", "Damon", "Corey"])
    data[date].append(event)
    return data

def _getDummyData(data, date = "11/04/2016"):
    data = _getThuData(data, date=date)
    return data
