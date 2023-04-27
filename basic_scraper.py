from bs4 import BeautifulSoup

with open('website-example/home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')

    course_html_tags = soup.find_all('h5')

    with open('results/course_names.txt', 'w') as names:
        for course in course_html_tags:
            names.write(course.text + '\n')