# Testing

## Table of Contents
- [Encountered Issues](#encountered-issues)
- [Testing User Stories](#testing-user-stories)
- [Testing Code](#testing-code)
- [Testing Functionality](#testing-functionality)
- [Testing Compatibility](#testing-compatibility)
- [Testing Performance](#testing-performance)
- [Testing Accessibility](#testing-accessibility)
- [Code Validation](#code-validation)
- [Further Testing](#further-testing)
  
## Encountered issues
- ### Issues found during the building process:
  - `django.db.utils.OperationalError: no such table: schools_school` This error was given when trying to migrate or to create migrations. Issue was found during deployment and it revealed that **CustomRegisterSerializer** was creating this issue as it was trying to extract the school list to add it in a choice field before school database was even created.
  - **FIXED**: by following this [StackOverflow answer](https://stackoverflow.com/a/52732608) that is recommending using lazy django utils.
  - `Uncaught (in promise) SyntaxError: Unexpected end of JSON input` This error was thrown when assigning and removing teachers to/from rooms. The assignment was fulfilled, but there was no dynamic change on the page, unless refreshed. This was caused by the fact that teacher assignment endpoints only return status and no json.
  - **FIXED**: by checking if the `content-type` header of the response equals `application/json`, if not, then `response.text()` is called instead. For consistency, the api endpoints for assigning and removing teachers to/from rooms, were edited to return json response, for both 2XX and 4XX status codes.
- ### Issues found while testing:
  - Plan tile not showing on the school subscription page.
  - **FIXED**: this was not a functionality issue. The code was checking if the current subscription's plan has the same primary key as the any of the prices fetched from the `/api/prices/` endpoint, and adds the matching price into the selectedPrice variable that was used as condition for rendering the tile. The issue was with matching, as the prices were fetched from Price djstripe db table, while the foreign key of the subscription for plan was pointing to Plan db table, and they happened to have different primary key. This was not spotted on development environment as the prices on Price table and plans on Plan table had exact same primary keys. This was sorted by extracting prices from Plan table and give them as result to the up-mentioned API endpoint, instead of Price table.

## Testing user stories
  - #### As a user I need to:
    - easily navigate throughout the website on any device/platform.
        > :heavy_check_mark: Top navigation bar is displayed on every page. Navigation flow is quite intuitive and back button is present on every page.
    - quickly understand the design flow.
        > :heavy_check_mark: Once logged in, user is redirected to a landing page specific to its user type. From there, design flow is made intuitive.
  - #### As a parent I need to:
    - see my child's progress.
        > :heavy_check_mark: a parent will land on children page. Clicking on a child, will open its activities timeline, where teachers can keep parents posted of progress.
    - be able to contact the staff.
        > :heavy_check_mark: There are several ways to contact the manager of any of the child's teachers. From the chat window, pressing + button will open a list of available contacts (manager + teachers of own children). From pupil's info page, there are links to contact pupil's teachers. From main menu, under the dropdown, there is a link to contact the manager.
    - be able to update profile details and child details.
        > :heavy_check_mark: User account page allows users to update the user profile, including changing school. From pupil's info page, parents can update personal details, by adding custom fields and values.
  - #### As a childcare staff I need to:
    - be able to log every child activities by using personal device (phone, tablet, computer).
        > :heavy_check_mark: Every staff member can create a teacher account, where if is assigned to a room, will have access to post activities to room pupil's timelines, from own device.
    - upload pictures.
        > :heavy_check_mark: When posting an activity, multiple photos can be uploaded with the activity.
  - #### As a childcare manager I need to:
    - be able to register my childcare(s).
        > :heavy_check_mark: Once registered, a manager can add as many schools as wished. Functionality will be limited until a subscription is purchased for each school.
    - be able to see billing info an pay for subscription.
        > :heavy_check_mark: Once a school is created, anything further will point to the subscription page, where a subscription can be purchased. Once a subscription is purchased, on the same page, subscription and billing details will be displayed instead.
    - be able to add classes(rooms), add children and assign them to rooms, assign children to parent accounts, assign staff to rooms, and revert any of these changes.
        > :heavy_check_mark: Once a subscription is active, a manager can perform any of these actions.
    - be able to contact parents.
        > :heavy_check_mark: On pupil's info page, there is list of pupil's assigned parents and a chat link beside each parent.

## Testing Code
> :heavy_check_mark: Every javascript method was tested for the expected outcome by using the app, in console by using `console.log()` or by manually calling the function.

> :heavy_check_mark: Every python function, django method or API view was tested for the expected outcome by using the app, by accessing the route, in python console, while debug mode was set to on, by using `print()` and by watching for the correct response. 

## Testing Functionality
   - ### Testing links and buttons
        > ### Header (every page except dashboard) :heavy_check_mark:
        > - top navigation fully functional including the brand title.
        > - navigation toggle "burger" working as expecting, opening the dropdown navigation.
        > ### Schools :heavy_check_mark:
        > - clicking on a school opens the school rooms page.
        > - clicking on Add school opens the school editor.
        > ### School Rooms :heavy_check_mark:
        > - clicking on a room opens the room pupils page.
        > - clicking on Edit school opens the school editor.
        > - clicking on Add room opens the room editor.
        > ### School Pupils :heavy_check_mark:
        > - clicking on a pupil opens the pupil's activities page.
        > - clicking on an unassigned pupil opens the pupil's infos page.
        > - clicking on Add pupil opens the pupil editor.
        > ### Room Pupils :heavy_check_mark:
        > - clicking on a pupil opens the pupil's activities page.
        > - clicking on Edit room opens the room editor.
        > - clicking on Add pupil opens the pupil editor.
        > - clicking + teachers opens the unassigned teachers popover, clicking on a teacher in the list, assigns teacher to room. Clicking on red trash beside teacher, opens the confirm dialog and then unassigns teacher.
        > - clicking + Assign pupil opens the unassigned pupils popover, clicking on a pupil in the list, assigns pupil to room.
        > ### Children (parent) :heavy_check_mark:
        > - clicking on a pupil opens the pupil's activities page.
        > ### Pupil Activities :heavy_check_mark:
        > - clicking on a photo, opens the image lightbox.
        > - clicking on + opens the add activity form. Filling the form and submitting it, adds activity to pupil.
        > - clicking on Pupil Info, opens the pupil's info page.
        > ### Pupil Info :heavy_check_mark:
        > - clicking on every pen button and then cancel button, toggles editor forms. These are not available when logged as a teacher or a parent.
        > - uploading a photo, replaces the current pupil's photo.
        > - personal details: add new, save, add new, reset, works as expected.
        > - clicking on teacher's or parent's chat icon, opens chat window.
        > - clicking delete pupil, opens a confirm dialog, then deletes the pupil.
        > ### Account :heavy_check_mark:
        > - clicking on Update, submits the form and validates data. Errors are displayed if data is invalid. Success notification is displayed if data was submitted successfully.
        > ### Manage Subscriptions :heavy_check_mark:
        > - clicking on a school, opens school's subscription page.
        > ### School Subscription :heavy_check_mark:
        > - if no subscription, clicking on a price will display the card form, submitting card info, updates the page with new subscription data.
        > - clicking on cancel subscription, updates the page and Re-activate subscription button appears.
        > - clicking on re-activate button, updates the page and cancel button apperas.

   - ### Testing form validation
        > :heavy_check_mark: **Login** and **Registration** form: this form has built-in validation from all-auth package and backend validation from user model.

        > :heavy_check_mark: **Account** form: was tested while implementing custom validation, by submitting form with empty or invalid fields. There is front-end html form validation and backend validation made by API serializer and django model.

        > :heavy_check_mark: **School editor**, **Room editor** and **Pupil editor**: These forms function the same way as the Account form. If front-end validation fails, serializer and model validation will be sent as response through API and error messages will be displayed beside the invalid fields. Tested.
   - ### Testing for errors
        > :heavy_check_mark: Full app browsing and functionality was tested with browser's console open. Console is clear of errors.

        > :heavy_check_mark: Python console with debug mode on is clear of errors.

## Testing Compatibility
   - ### Responsiveness
        > Using DevTools and different device sizes such as mobile and tablet, the website was tested for any possible screen size combination and orientation. No issues found. **App is size compatible** :heavy_check_mark:.
   - ### OS test
        > #### Desktop
        > The website was tested on Ubuntu 20.04, Windows 7 and Windows 10 systems. Further tests were made using [LambdaTest](https://www.lambdatest.com/), for MacOS Mojave. Result as expected, **desktop system-cross compatible** :heavy_check_mark:.

        > #### Mobile
        > The website was tested on Android 6, Android 9, Android 10 and iOS 14 systems. Further tests were made using [LambdaTest](https://www.lambdatest.com/), for iOS on iPad Pro. Result as expected, **mobile system-cross compatible** :heavy_check_mark:.
   - ### Devices test
        > The website was tested on HP 15" notebook, ASUS 15" notebook, ACER 15" notebook, Huawei P30 PRO, Huawei P20 PRO, Huawei P10, iPhone 11, Samsung Galaxy Note10, Samsung Galaxy A7, Samsung Galaxy TabS6, Lenovo Yoga Tab. Further device tests were made using [LambdaTest](https://www.lambdatest.com/), for iPad Pro (11 inch) and MacOS. The result is consistent, website is **platform-cross compatible** :heavy_check_mark:.
   - ### Browser test
        > The website was tested on Google Chrome, Firefox, Safari, Edge, Samsung Internet, Opera, Vivaldi and Yandex. This website is NOT designed to be compatible with IE. Browsers versions were all up to date. Results were consistent. Conclusion: the website is **browser-cross compatible** :heavy_check_mark:.

## Testing Performance
Performance has been tested using Chrome's **Lighthouse** tool for both desktop and mobile. Mobile tests were made using **remote device** connection and an actual mobile phone. Being a RESTful app, there are more or less API requests for each page, and performance relies more on server responses. Therefore, every test is different, but all tests had performance in a range between 85 and 95.

> :heavy_check_mark:
>
>   ![LightHouse Performance Result for Landing page](https://github.com/digicreche/dev.pi/blob/main/docs/perf.png)  

## Testing Accessibility
  - [a11y Color Contrast Accessibility Validator](https://color.a11y.com/Contrast/) - Login and registration pages only
    > :heavy_check_mark: The only found issue is the contrast between brand logo and background, this is because the validator doesn't see the colour effect applied on text, but just the transparent colour. This is a design choice and it is intentional.
  - Google Chrome Lighthouse
    > :heavy_check_mark: Tested on every page and result was 100% consistent throughout application.

## Code Validation
  - ### HTML :heavy_check_mark:
    > Html was tested and validated with [W3C Validator](https://validator.w3.org/).
    > - Any found errors are part of third-party packages that are compiling or injecting html code.

  - ### CSS :heavy_check_mark:
    > Custom CSS was validated with [W3C CSS](https://jigsaw.w3.org/css-validator/).
    > - No errors found!
  - ### JavaScript :heavy_check_mark:
    > Javascript has been validated during building process by **VSCode** extension **[ESLint](https://eslint.org/)** and by NPM Vue ESLint. **No errors or issues** :heavy_check_mark:.
  - ### Python :heavy_check_mark:
    > Python has been validated during building process by **VSCode** integrated extensions **[Pylint](https://www.pylint.org/)** and **[Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)**, which are in compliance with PEP8 style guide. **No errors or issues**.

## Further Testing
  - ### Overflow :heavy_check_mark:
    > Every page was tested for overflow by using the [Unicorn Revealer](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB) chrome extension to highlight the elements margins. **No issues found**.