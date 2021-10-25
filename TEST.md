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
