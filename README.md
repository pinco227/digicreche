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
    - be notified about new child's activities.
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

### Encountered issues
  - `django.db.utils.OperationalError: no such table: schools_school` This error was given when trying to migrate or to create migrations. Issue was found during deployment and it revealed that **CustomRegisterSerializer** was creating this issue as it was trying to extract the school list to add it in a choice field before school database was even created.
  - **FIXED**: by following this [StackOverflow answer](https://stackoverflow.com/a/52732608) that is recommending using lazy django utils.
  - `Uncaught (in promise) SyntaxError: Unexpected end of JSON input` This error was thrown when assigning and removing teachers to/from rooms. The assignment was fulfilled, but there was no dynamic change on the page, unless refreshed. This was caused by the fact that teacher assignment endpoints only return status and no json.
  - **FIXED**: by checking if the `content-type` header of the response equals `application/json`, if not, then `response.text()` is called instead. For consistency, the api endpoints for assigning and removing teachers to/from rooms, were edited to return json response, for both 2XX and 4XX status codes.

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