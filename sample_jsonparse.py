import json

with open('sample.json', 'r') as json_file:
    json_data = json.load(json_file)

all_courses = []

certifications = json_data.get('certifications', [])

for certification in certifications:
    courses = certification.get('courses', [])
    all_courses.extend(courses)

print("All Courses:", ', '.join(all_courses))
