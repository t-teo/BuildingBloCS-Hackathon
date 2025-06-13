import pandas as pd

jobs = {
    'JobID': list(range(1, 26)),
    'Title': [
        'Data Analyst', 'Graphic Designer', 'Teacher', 'Software Engineer', 'Customer Service',
        'Marketing Specialist', 'Finance Executive', 'Project Manager', 'UI/UX Designer', 'Business Analyst',
        'HR Manager', 'Operations Lead', 'Content Writer', 'QA Engineer', 'Sales Executive',
        'Network Engineer', 'Product Owner', 'Mobile Developer', 'Legal Advisor', 'Account Manager',
        'Event Planner', 'Supply Chain Analyst', 'Research Scientist', 'Technical Support', 'Digital Marketer'
    ],
    'Skills': [
        'Python, Excel', 'Photoshop, Creativity', 'Teaching, Communication', 'Java, SQL', 'Communication, Patience',
        'SEO, Content Creation', 'Accounting, Excel', 'Agile, Leadership', 'Figma, Prototyping', 'Strategy, Analysis',
        'Recruitment, Onboarding', 'Logistics, Coordination', 'Writing, Editing', 'Testing, Automation', 'Negotiation, CRM',
        'Networking, Security', 'Scrum, Product Management', 'Kotlin, Swift', 'Legal Research, Compliance', 'Client Relations',
        'Event Management, Budgeting', 'Inventory, Forecasting', 'Data Analysis, Experimentation', 'Troubleshooting, Support', 'SEM, Analytics'
    ],
    'Accessibility': [
        'Remote', 'Wheelchair Access', 'Flexible Hours', 'On-site', 'Hybrid',
        'Remote', 'Wheelchair Access', 'Flexible Hours', 'On-site', 'Hybrid',
        'Remote', 'Wheelchair Access', 'Flexible Hours', 'On-site', 'Hybrid',
        'Remote', 'Wheelchair Access', 'Flexible Hours', 'On-site', 'Hybrid',
        'Remote', 'Wheelchair Access', 'Flexible Hours', 'On-site', 'Hybrid'
    ],
    'Location': [
        'Punggol', 'Sengkang', 'Buangkok', 'Hougang', 'Kovan',
        'Serangoon', 'AngMoKio', 'PasirRis', 'Tampines', 'Orchard',
        'ChinaTown', 'LittleIndia', 'Jurong', 'Woodlands', 'Yishun',
        'Punggol', 'Sengkang', 'Buangkok', 'Hougang', 'Kovan',
        'Serangoon', 'AngMoKio', 'PasirRis', 'Tampines', 'Orchard'
    ],
    'Salary': [
        '50,000', '60,000', '55,000', '70,000', '65,000',
        '58,000', '62,000', '75,000', '68,000', '72,000',
        '53,000', '61,000', '57,000', '73,000', '66,000',
        '59,000', '63,000', '76,000', '69,000', '73,000',
        '54,000', '64,000', '56,000', '74,000', '67,000'
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
        'Analyze business processes and recommend improvements.',
        'Manage HR processes and employee relations.',
        'Coordinate daily operations and logistics.',
        'Write and edit content for various platforms.',
        'Test software for bugs and quality assurance.',
        'Drive sales and manage client accounts.',
        'Maintain network infrastructure and security.',
        'Lead product development and scrum teams.',
        'Develop mobile applications for Android and iOS.',
        'Provide legal advice and ensure compliance.',
        'Manage client portfolios and relationships.',
        'Plan and organize events and conferences.',
        'Analyze supply chain and optimize inventory.',
        'Conduct scientific research and experiments.',
        'Provide technical support to end-users.',
        'Develop and execute digital marketing strategies.'
    ]
}

pd.DataFrame(jobs).to_csv('jobs.csv', index=False)

