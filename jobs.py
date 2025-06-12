import pandas as pd

jobs = {
    'JobID': range(1, 11),
    'Title': [
        'Data Analyst', 'Graphic Designer', 'Teacher', 'Software Engineer', 'Customer Service',
        'Marketing Specialist', 'Finance Executive', 'Project Manager', 'UI/UX Designer', 'Business Analyst'
    ],
    'Skills': [
        'Python, Excel', 'Photoshop, Creativity', 'Teaching, Communication', 'Java, SQL', 'Communication, Patience',
        'SEO, Content Creation', 'Accounting, Excel', 'Agile, Leadership', 'Figma, Prototyping', 'Strategy, Analysis'
    ],
    'Accessibility': [
        'Remote', 'Wheelchair Access', 'Flexible Hours', 'On-site', 'Hybrid',
        'Remote', 'Wheelchair Access', 'Flexible Hours', 'On-site', 'Hybrid'
    ],
    'Location': [
        'Punggol', 'Sengkang', 'Buangkok', 'Hougang', 'Kovan',
        'Serangoon', 'AngMoKio', 'PasirRis', 'Tampines', 'Orchard'
    ],
    'Salary': [
        '$50,000', '$60,000', '$55,000', '$70,000', '$65,000',
        '$58,000', '$62,000', '$75,000', '$68,000', '$72,000'
    ],
    'Description': [
        'Analyze data trends to support business decisions.',
        'Create visual concepts and designs for marketing materials.',
        'Teach and mentor students in a classroom setting.',
        'Develop and maintain software applications.',
        'Assist customers and resolve their inquiries.',
        'Plan and execute marketing campaigns.',
        'Manage financial records and reports.',
        'Oversee project timelines and deliverables.',
        'Design user interfaces and improve user experience.',
        'Analyze business processes and recommend improvements.'
    ]
}

pd.DataFrame(jobs).to_csv('jobs.csv', index=False)

