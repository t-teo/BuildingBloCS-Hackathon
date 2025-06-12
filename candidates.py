import pandas as pd

candidates = {
    'CandidateID': [
        101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115
    ],
    'Name': [
        'John Doe', 'Maria Garcia', 'Alex Chen', 'Sarah Williams', 'Priya Singh',
        'Wei Tan', 'Nurul Aisyah', 'David Lim', 'Siti Rahman', 'Benjamin Lee',
        'Rachel Ng', 'Samuel Ong', 'Mei Chen', 'Arjun Kumar', 'Fiona Goh'
    ],
    'Skills': [
        'Python, Data Analysis', 'Design, Creativity', 'Teaching, Leadership', 'Communication, Teamwork',
        'Project Management, Agile', 'Java, Spring Boot', 'UI/UX, Figma', 'Marketing, SEO',
        'Finance, Excel', 'Customer Service, CRM', 'Javascript, React', 'Copywriting, Editing',
        'Machine Learning, AI', 'Cloud Computing, AWS', 'Business Analysis, Strategy'
    ],
    'Needs': [
        'Wheelchair Access', 'Remote Work', 'Flexible Hours', 'Sign Language Support',
        'Ergonomic Workspace', 'Assistive Technology', 'Visual Aid', 'Quiet Environment',
        'Service Animal Friendly', 'Accessible Restrooms', 'Remote Work', 'Flexible Hours',
        'Wheelchair Access', 'Sign Language Support', 'Ergonomic Workspace'
    ],
    'Location': [
        'Punggol', 'Sengkang', 'Buangkok', 'Hougang', 'Kovan',
        'Serangoon', 'AngMoKio', 'PasirRis', 'Tampines', 'Orchard',
        'ChinaTown', 'LittleIndia', 'Jurong', 'Woodlands', 'Yishun'
    ]
}

pd.DataFrame(candidates).to_csv('candidates.csv', index=False)