# DigiCreche

**DigiCreche** is an educational app which also serves as a Milestone Project for the **Software Developer Diploma** programme of **Code Institute**.

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

## Features
  - ### Planned features
    - Single page app (SPA).
    - Mobile-first: sticky/hiding header with always visible menu buttons.
    - Landing on login/register.
    - Timeline-styled day activities.
    - Profile page.
    - Contact page.

## Database
  - ### Entity Relationship Diagram
    ![ER Diagram](https://github.com/pinco227/digicreche/blob/main/docs/db-er.png) 

## Testing

### Encountered issues
  - `django.db.utils.OperationalError: no such table: schools_school` This error was given when trying to migrate or to create migrations. Issue was found during deployment and it revealed that **CustomRegisterSerializer** was creating this issue as it was trying to extract the school list to add it in a choice field before school database was even created.
  - **FIXED**: by following this [StackOverflow answer](https://stackoverflow.com/a/52732608) that is recommending using lazy django utils.

## Credits
- ### Code
  - [This article](https://soshace.com/upload-multiple-images-to-a-django-model-without-plugins/) and [this solution](https://www.py4u.net/discuss/192406) for multiple file upload using admin and API.