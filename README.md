# DigiCreche

**DigiCreche** is an educational app which also serves as a Milestone Project for the **Software Developer Diploma** programme of **Code Institute**.

This is an MVP of a child-care management app. It is a RESTful API SPA built using Django REST Framework and VueJS.

## Table of Contents
  - [Demo](#demo)
  - [UX](#ux)
    - [Business Goals](#business-goals)
    - [User Needs](#user-needs)
    - [User Scenarios](#user-scenarios)
    - [Structure](#structure)
    - [Skeleton](#skeleton)
      - [Wireframes](#wireframes)
    - [Design Choices](#design-choices)
  - [Features](#features)
  - [Database](#database)
  - [API endpoints](#api-endpoints)
  - [Technologies used](#technologies-used)
  - [Testing](#testing)
  - [Deployment](#deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)
  - [ToDo](#todo)

## Demo

### [Live App](https://digicreche.herokuapp.com/)

[![Screenshot](https://github.com/pinco227/digicreche/blob/main/docs/mockup.png)](https://digicreche.herokuapp.com/)

## UX
- ### Business Goals
  - Sell subscription service to childcares.
  - Reach as many childcares as possible, from the smallest town-creche to largest business areas chreches, by focusing on quantity over price.
  - Reach to parents, so it can be self-promoting, by word of mouth.
  - Build an app that can help both carers and parents/guardians, keep track of children activities and progress by offering a simple and user-friendly interface.
- ### User Needs
  - Need assurance that their children receives the best care.
  - Need to have access to their children activities and progress at any time.
  - Need a better and simpler communication between both parties (carers and guardians).
  - Need to share logs, activities, photos, progress in a siomple, fast, yet well organised manner.
  - Need to save time by digitizing logging.
- ### User Scenarios
  - #### As a user I need to:
    - easily navigate throughout the website on any device/platform.
    - quickly understand the design flow.
  - #### As a parent I need to:
    - see my child's progress.
    - be able to contact the staff.
    - be able to update profile details and child details.
  - #### As a childcare staff I need to:
    - be able to log every child activities by using personal device (phone, tablet, computer).
    - upload pictures.
  - #### As a childcare manager I need to:
    - be able to register my childcare(s).
    - be able to see billing info an pay for subscription.
    - be able to add classes(rooms), add children and assign them to rooms, assign children to parent accounts, assign staff to rooms, and revert any of these changes.
    - be able to contact parents.
- ### Structure
    The app is designed to be consistent, intuitive and learnable.
  - Interaction design
    - For predictability, the interface interacts with user actions as the user expects. The scroll/swipe actions respond with the normal behaviour and buttons acts instantly on press.
    - For consistency, the interface offers a subtle visual feedback to the user (on hover, focus and press of buttons and fields) which is similar throughout the application and helps the user to quickly learn the functionality.
  - Information architecture
    - The content is organised and prioritised by importance from top to bottom and left to right.
    - For consistency, the information is presented in the rule of 3 on large screens and individual on small screens.
    - The information is structured mostly in nested lists.
  - ### Skeleton
    - ### Wireframes
      - Authentication [mobile](https://github.com/pinco227/digicreche/blob/main/docs/wireframes/auth-mobile.png) / [medium-large](https://github.com/pinco227/digicreche/blob/main/docs/wireframes/auth-md-lg.png)
      - Parent/Guardian landing [mobile](https://github.com/pinco227/digicreche/blob/main/docs/wireframes/parents-landing-mobile.png) / [medium-large](https://github.com/pinco227/digicreche/blob/main/docs/wireframes/parents-landing-md-lg.png)
      - Manager landing [mobile](https://github.com/pinco227/digicreche/blob/main/docs/wireframes/manager-landing-mobile.png) / [medium-large](https://github.com/pinco227/digicreche/blob/main/docs/wireframes/manager-landing-md-lg.png)
      - Rooms [mobile](https://github.com/pinco227/digicreche/blob/main/docs/wireframes/rooms-mobile.png) / [medium-large](https://github.com/pinco227/digicreche/blob/main/docs/wireframes/rooms-md-lg.png)
      - Activities [mobile](https://github.com/pinco227/digicreche/blob/main/docs/wireframes/activities-mobile.png) / [medium-large](https://github.com/pinco227/digicreche/blob/main/docs/wireframes/activities-md-lg.png)
      - Chat [mobile](https://github.com/pinco227/digicreche/blob/main/docs/wireframes/chat-mobile.png) / [medium-large](https://github.com/pinco227/digicreche/blob/main/docs/wireframes/chat-md-lg.png)
      - Profile [mobile](https://github.com/pinco227/digicreche/blob/main/docs/wireframes/profile-mobile.png) / [medium-large](https://github.com/pinco227/digicreche/blob/main/docs/wireframes/profile-md-lg.png)

- ### Design Choices 
  - #### Colours
    - The colour palette consists of two accent colours, orange and green, in different shades (dark, light) and a range of neutral colours, from off-withe to dark grey.
    - According to [The Psychology of Color](https://www.toptal.com/designers/ux/color-in-ux), the chosen colours represent cheerfulness and comfort.
    ![Colour Psychology Wheel](https://github.com/pinco227/dev.pi/blob/main/docs/colour-wheel.jpg)  
    - The 60-30-10 Rule was also taken into consideration when building the project. The light shades which are used mostly for background are considered neutral and makes up to 60% of the palette. The dark shades are complementary and makes up to 30%, while the accent colours completes the remaining 10% of the design.
    - Few other colours we're used to improve UX. E.g.: red was used for errors and delete buttons.
  - #### Typography
    There are two fonts used throughout the project:
    - [Open Sans](https://fonts.google.com/specimen/Open+Sans?query=Open+sans) is used for all the content. This font was preffered for its excellent legibility, especially on mobile devices. Different weights were used to improve UX.
    - [Arima Madurai](https://fonts.google.com/specimen/Arima+Madurai?query=Arima+Madurai) is used brand text only.
  - #### Media
    There are no media assets used in building this project. The images used for demo content are stock images from [Unsplash.com](https://unsplash.com/)
  - #### Iconography
    Icons are used throughout the project to help the user understand more efficiently the meaning of the content. They are a very good asset to improve UX.

## Features
  - ### Planned features
    - Single page app (SPA).
    - Mobile-first: sticky/hiding header with always visible menu buttons.
    - Landing on login/register.
    - Timeline-styled day activities.
    - Profile page.
    - Contact page.
  - ### Extra features
    - Subscription based freemium access for manager users.
    - Pricing page.
    - Live chat built using websockets.
    - Assign pupil to room widget (in two simple clicks).
    - Assign teacher to room widget (in two simple clicks).
    - Room icons.
    - Pupil personal details - custom dynamic fields.
    - Photo lightbox for activities timeline.
    - Custom activity types
## Database
  - ### Entity Relationship Diagram
    ![ER Diagram](https://github.com/pinco227/digicreche/blob/main/docs/db-er.png) 

## API endpoints
  - Auth
    - POST `/api/rest-auth/login/`
    - GET `/api/rest-auth/logout/`
    - POST `/api/rest-auth/password/reset/`
    - POST `/api/rest-auth/password/reset/confirm/`
    - POST `/api/rest-auth/password/change/`
    - POST `/api/rest-auth/registration/`
    - GET|PUT|PATCH `/api/rest-auth/user/`
  - Subscription
    - GET `/api/prices/`
    - POST `/api/create-subscription/`
    - POST `/api/cancel-subscription/`
    - POST `/api/update-subscription/`
    - POST `/api/reactivate-subscription/`
    - POST `/api/retrieve-stripe-subscription/`
    - POST `/api/retrieve-payment-method/`
    - GET `/api/retrieve-subscription/<int:pk>/`
  - Schools
    - GET|POST `/api/schools/`
    - GET|PUT|PATCH|DELETE `/api/schools/<slug:slug>/`
    - GET `/api/my-schools/`
    - GET `/api/schools/<slug:slug>/teachers/`
    - GET `/api/schools/<slug:slug>/teachers/unassigned/`
    - GET `/api/schools/<slug:slug>/parents/`
    - Rooms
      - GET|POST `/api/schools/<slug:slug>/rooms/`
      - GET|PUT|PATCH|DELETE `/api/schools/<slug:slug>/rooms/<int:pk>/`
      - DELETE `/api/schools/<slug:slug>/rooms/<int:pk>/remove-teacher/<int:id>/`
      - POST `/api/schools/<slug:slug>/rooms/<int:pk>/assign-teacher/`
    - Pupils
      - GET|POST `/api/schools/<slug:slug>/pupils/`
      - GET `/api/schools/<slug:slug>/rooms/<int:pk>/pupils/`
      - GET `/api/schools/<slug:slug>/unassigned/`
      - GET|PUT|PATCH|DELETE `/api/schools/<slug:slug>/pupils/<int:pk>/`
      - GET|PUT|PATCH `/api/schools/<slug:slug>/pupils/<int:pk>/photo/`
      - GET|PUT|PATCH `/api/schools/<slug:slug>/pupils/<int:pk>/details/`
      - GET|PUT|PATCH `/api/schools/<slug:slug>/pupils/<int:pk>/room/`
      - GET `/api/children/`
    - Activities
      - GET|POST `/api/activity_types/`
      - GET|PUT|PATCH|DELETE `/api/activity_types/<int:pk>/`
      - GET|POST `/api/schools/<slug:slug>/pupils/<int:pk>/activities/`
      - GET|PUT|PATCH `/api/schools/<slug:slug>/activity/<int:pk>/`
  - Chat
    - GET `/api/chats/`
    - GET|POST `/api/chats/<int:pk>/`
    - GET `/api/contacts/`
  - Helpers
    - GET `/api/countries/`

## Technologies used
- Workspace
  * [Ubuntu20.04](https://ubuntu.com/) as Operating System
  * [Visual Studio Code](https://code.visualstudio.com/) as Integrated Development Environment
- Languages
  * [HTML5](https://en.wikipedia.org/wiki/HTML5)
  * [CSS3](https://en.wikipedia.org/wiki/CSS)
  * [JS](https://en.wikipedia.org/wiki/JavaScript)
  * [Python](https://www.python.org/)
- Frameworks & Libraries
  * [Django](https://www.djangoproject.com/) is used as back-end framework.
  * [Vue.js](https://v3.vuejs.org/) is used as a front-end framework.
  * [Bootstrap5](https://getbootstrap.com/) is used for its great responsiveness, styling classes, icons and its javascript functionality.
  * [Font Awesome](https://fontawesome.com/) icons were used for writing the auto-generated CV.
  * [Google Fonts](https://fonts.google.com/) is used as the main font resource.
  * Main Python and Django packages:
    * [Django REST Framework](https://www.django-rest-framework.org/) is used for creating RESTful API backend.
    * [Channels Redis](https://github.com/django/channels_redis) used for chat implementation.
    * [Daphne](https://github.com/django/daphne) is used to run project on an asynchronous server to support websockets.
    * [Stripe](https://pypi.org/project/stripe/) and [DJ-Stripe](https://github.com/dj-stripe/dj-stripe) for Stripe payment platform implementation.
    * [AllAuth](https://django-allauth.readthedocs.io/en/latest/installation.html) for user authentication.
    * [Storages & S3 boto](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html) for cloud media storage.
    * [WhiteNoise](http://whitenoise.evans.io/en/stable/) for serving own static files without relying on cloud storages.
  * Main NPM and Vue.js packages:
    * [Vue Router](https://router.vuejs.org/) for front-end SPA routing.
    * [VueX](https://next.vuex.vuejs.org/) as a state management library, used in chat websocket implementation.
    * [Moment.js](https://momentjs.com/docs/) and [Vue Timeago3](https://www.npmjs.com/package/vue-timeago3) for time formating.
    * [vue-native-websocket-vue3](https://github.com/likaia/vue-native-websocket-vue3/blob/HEAD/README-EN.md) for websocket implementation.
    * [vue-toast-notification](https://www.npmjs.com/package/vue-toast-notification) for response feedback messages.
    * [vue-tel-input](https://www.npmjs.com/package/vue-tel-input) for phone number field input masking.
    * [vue-easy-lightbox](https://github.com/XiongAmao/vue-easy-lightbox) for photo lightbox.
- Version Control
  * [Git](https://git-scm.com/) as Version Control System.
  * [Github](https://www.github.com) for repository hosting.
  * [Commitizen](https://github.com/commitizen/cz-cli) for commit linting.
- Wireframes
  * [Draw.io](https://app.diagrams.net/) for creating [wireframes](#wireframes).
- Media
  * [Photopea](https://www.photopea.com/) online photo editor tool for creating the demo mockup image.
  * [dbdiagram.io](https://dbdiagram.io/) for database diagram creation.

## Testing
  ### [Click Here for Full Testing Process](https://github.com/pinco227/digicreche/blob/main/TEST.md)

## Deployment
- ### Forking the GitHub Repository
  By forking the GitHub Repository you make a copy of the original repository on your GitHub account to view and/or make changes without affecting the original repository by using the following steps:
  1. Log in to GitHub and locate the [digicreche repository](https://github.com/pinco227/digicreche).
  2. At the top right of the Repository, locate and click the "**Fork**" Button.
  3. You should now have a copy of the original repository in your GitHub account.
- ### Local Machine
  1. Log in to GitHub and locate the [digicreche repository](https://github.com/pinco227/digicreche) (or the forked repo into your profile).
  2. At the top of the Repository just above the list of files, locate and click the "**Code**" dropdown.
  3. To clone the repository using HTTPS, under "**Clone**", make sure "**HTTPS**" is selected and copy the link.
  4. Open Git Bash.
  5. Change the current working directory to the location where you want the cloned directory to be made.
  6. Type ```git clone```, and then paste the URL you copied in Step 3.
      ```bash
      git clone https://github.com/pinco227/digicreche.git
      ```
  7. Press Enter. Your local clone will be created.
      ```bash
      $ git clone https://github.com/pinco227/digicreche.git
      Cloning into 'digicreche'...
      remote: Enumerating objects: XXX, done.
      remote: Counting objects: 100% (XXX/XXX), done.
      remote: Compressing objects: 100% (XXX/XXX), done.
      remote: Total XXX (delta XXX), reused XXX (delta XXX), pack-reused 0
      Receiving objects: 100% (XXX/XXX), XXX MiB | XXX MiB/s, done.
      Resolving deltas: 100% (XXX/XXX), done.
      ```
      > Click [Here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.
  8. I recommend using a virtual environment such as [venv](https://docs.python.org/3/library/venv.html).
  9. Make sure you have python and npm installed on your machine.
  10. Create [Stripe account](https://www.stripe.com/).
  11. Set the following environmental variables into your virtual environment:
      ```bash
      export SECRET_KEY='<secret_key>'
      export DEVELOPMENT=True
      export DJANGO_SETTINGS_MODULE=digicreche.settings
      export STRIPE_TEST_PUBLIC_KEY='<stripe_test_pkey>'
      export STRIPE_TEST_SECRET_KEY='<stripe_test_skey>'
      export STRIPE_WH_SECRET='<stripe_webhook_secret>'
      ```
  12. Install required `python` packages by running the following command into terminal:
      ```bash
      pip install -r requirements.txt
      ```
  13. Change directory to `frontend`
      ```bash
      cd frontend
      ```
  14. Install required node packages by running this command in frontend directory:
      ```bash
      npm install
      ```
  15. Migrate the database by runing following command in terminal at root level:
      ```bash
      python manage.py migrate
      ```
  16. Run app by typing the following into terminal on root folder:
      ```bash
      python manage.py runserver
      ```
      And this command on a separate terminal on frontend directory:
      ```bash
      npm run serve
      ```
  17. Browse app by accessing [127.0.0.1:8000](http://127.0.0.1:8000/) into a browser. At this point, if configured right, the app should run properly and login screen will be displayed
  18. Create a superuser:
      ```bash
      python manage.py createsuperuser
      ```
- ### Heroku
  1. Make sure the `requirements.txt` file is up to date. Type the followings into terminal:
      ```bash
      pip freeze --local > requirements.txt
      ```
  2. Commit and push changes to forked repository.
  3. Create a [Heroku](https://heroku.com) account and click **New** on top right of the dashboard to **Create a new app**.
  4. Create and configure AWS [AWS IAM](https://console.aws.amazon.com/iam/) User (retrieve access keys) and [AWS S3 bucket](https://s3.console.aws.amazon.com/s3).
  5. Within the newly created heroku app go to **Settings** tab and press **Reveal Config Vars**. Add following variables: `HOSTNAME`, `SECRET_KEY`, `STRIPE_TEST_PUBLIC_KEY`, `STRIPE_TEST_SECRET_KEY`, `STRIPE_WH_SECRET`, `USE_AWS`, `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_S3_REGION_NAME`, `AWS_STORAGE_BUCKET_NAME`.
  6. Within heroku app, go to **Resources** tab and add the following add-ons: 
Heroku Postgres and Heroku Redis. These will create the following config vars: `DATABASE_URL`, `REDIS_TLS_URL`, `REDIS_URL`.
  7. Make sure you have heroku-cli installed in your machine. Scale heroku app by typing the following into terminal:
      ```bash
      heroku ps:scale web=1:free worker=1:free
      ```
  8. Go to **Deploy** tab and under the **Deployment method** click on the **Github** icon.
  9.  Right under this section, type the `digicreche` and search for the forked repository into your GitHub account. Select the right repository and click **Connect**.
  10. Under the **Automatic deploys** section, click **Enable Automatic Deploys**. The deployment will be now automatic with every github `push` command.
  11. Under the **Manual deploy** section, click **Deploy Branch** for initial deploy.
  12. Make sure you run `npm run build` before pushing, if any changes were made to frontend.
  13. You can now browse the deployed app by clicking **Open app** button on top right of the dashboard.

## Credits
- [This article](https://soshace.com/upload-multiple-images-to-a-django-model-without-plugins/) and [this solution](https://www.py4u.net/discuss/192406) for multiple file upload using admin and API.
- [Alexandr Ogurtov](https://github.com/aogz) for his [websocket consumer and store mutations](https://github.com/aogz/django-vue-websocket-chat/blob/master/chat/consumers.py) that served as a model in creating DigiCreche's websocket consumer and Vue store mutations.

## Aknowledgements
- [Code Institute](https://codeinstitute.net/) for their awesome **Full Stack Software Development** course.
- [Michele Saba (Udemy)](https://www.udemy.com/user/michele-saba/) for his [Complete Guide to Django REST Framework and Vue JS](https://www.udemy.com/course/the-complete-guide-to-django-rest-framework-and-vue-js/).
- [Connor Lindsey (Scrimba)](https://scrimba.com/learn/vuex) for his Vuex tutorial.
- [Very Academy](https://github.com/veryacademy) for [this video](https://www.youtube.com/watch?v=zizzeE4Obc0) about deploying.
- [Ajmal (Steemit)](https://steemit.com/@ajmaln) for his tutorial about [Creating a Simple Chat App with DjangoRestFramework](https://steemit.com/utopian-io/@ajmaln/part-1-creating-a-simple-chat-app-with-djangorestframework)
- [Hannah (Dev.to)](https://dev.to/earthcomfy) for her [Getting Started With Django Channels](https://dev.to/earthcomfy/getting-started-with-django-channels-a-simple-chat-app-2a7m) helpful tutorial.