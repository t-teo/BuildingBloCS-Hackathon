import pandas as pd

candidates = {
    'CandidateID': list(range(101, 126)),
    'Name': [
        'John Doe', 'Maria Garcia', 'Alex Chen', 'Sarah Williams', 'Priya Singh',
        'Wei Tan', 'Nurul Aisyah', 'David Lim', 'Siti Rahman', 'Benjamin Lee',
        'Rachel Ng', 'Samuel Ong', 'Mei Chen', 'Arjun Kumar', 'Fiona Goh',
        'Hannah Lim', 'Daniel Tan', 'Aisha Binte', 'Marcus Teo', 'Jasmine Koh',
        'Zhi Wei', 'Suresh Nair', 'Liyana Ahmad', 'Kelvin Chua', 'Emily Wong'
    ],
    'Skills': [
        'Python, Data Analysis', 'Design, Creativity', 'Teaching, Leadership', 'Communication, Teamwork',
        'Project Management, Agile', 'Java, Spring Boot', 'UI/UX, Figma', 'Marketing, SEO',
        'Finance, Excel', 'Customer Service, CRM', 'Javascript, React', 'Copywriting, Editing',
        'Machine Learning, AI', 'Cloud Computing, AWS', 'Business Analysis, Strategy',
        'SQL, Database', 'Public Speaking, Training', 'Social Media, Branding', 'C++, Embedded Systems',
        'Legal Research, Compliance', 'Event Planning, Coordination', 'Supply Chain, Logistics',
        'Research, Experimentation', 'Technical Support, Troubleshooting', 'Digital Marketing, SEM'
    ],
    'Needs': [
        'Wheelchair Access', 'Remote Work', 'Flexible Hours', 'Sign Language Support',
        'Ergonomic Workspace', 'Assistive Technology', 'Visual Aid', 'Quiet Environment',
        'Service Animal Friendly', 'Accessible Restrooms', 'Remote Work', 'Flexible Hours',
        'Wheelchair Access', 'Sign Language Support', 'Ergonomic Workspace',
        'Assistive Technology', 'Visual Aid', 'Quiet Environment', 'Service Animal Friendly',
        'Accessible Restrooms', 'Remote Work', 'Flexible Hours', 'Wheelchair Access',
        'Sign Language Support', 'Ergonomic Workspace'
    ],
    'Location': [
        'Punggol', 'Sengkang', 'Buangkok', 'Hougang', 'Kovan',
        'Serangoon', 'AngMoKio', 'PasirRis', 'Tampines', 'Orchard',
        'ChinaTown', 'LittleIndia', 'Jurong', 'Woodlands', 'Yishun',
        'Punggol', 'Sengkang', 'Buangkok', 'Hougang', 'Kovan',
        'Serangoon', 'AngMoKio', 'PasirRis', 'Tampines', 'Orchard'
    ]
}

pd.DataFrame(candidates).to_csv('candidates.csv', index=False)