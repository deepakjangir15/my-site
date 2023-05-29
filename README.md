# Django Blog Project

This is a Django-based blog project that I developed as part of my learning process with the Django framework. It serves as a demonstration of my understanding and implementation of various concepts and features provided by Django.

## Features

- User registration and authentication: Users can sign up, log in, and log out to access the blog.
- User roles: Users can have different roles, such as admin or regular user, with varying levels of access and privileges.
- Blog posts: Users can create, edit, and delete blog posts.
- Categories and tags: Blog posts can be categorized and tagged for better organization and searchability.
- Comments: Users can leave comments on blog posts to engage in discussions.
- Rich text editor: The blog post creation and editing process includes a rich text editor for easy formatting.
- Deployment: The project has been deployed using PythonAnywhere and is accessible at [http://tdeepak509.pythonanywhere.com/](http://tdeepak509.pythonanywhere.com/).

## Installation

To run this project locally, follow these steps:

1. Clone the repository to your local machine:

```
git clone https://github.com/deepakjangir15/my-site.git
```

2. Navigate to the project directory:

```
cd django-blog-project
```

3. Create a virtual environment and activate it:

```
python3 -m venv myenv
source myenv/bin/activate
```

4. Install the project dependencies:

```
pip install -r requirements.txt
```

5. Run database migrations:

```
python manage.py migrate
```

6. Create a superuser (admin) account:

```
python manage.py createsuperuser
```

7. Start the development server:

```
python manage.py runserver
```

8. Open your web browser and visit [http://localhost:8000](http://localhost:8000) to access the blog.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch with a descriptive name for your feature or bug fix.
3. Make the necessary changes and commit them to your branch.
4. Push your branch to your forked repository.
5. Submit a pull request detailing your changes and explaining the purpose of the pull request.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and use it according to your needs.

## Acknowledgements

I would like to acknowledge the following resources that helped me in learning Django and developing this project:

- The official Django documentation: [https://docs.djangoproject.com/](https://docs.djangoproject.com/)
- Django for Beginners by William S. Vincent: [https://djangoforbeginners.com/](https://djangoforbeginners.com/)
- Django Girls tutorial: [https://tutorial.djangogirls.org/](https://tutorial.djangogirls.org/)
- Stack Overflow and various online forums for providing answers to my questions and helping me troubleshoot issues.
