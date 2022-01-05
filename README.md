<h2 align="center"><img src="https://raw.githubusercontent.com/MarisKX/Code-Institute-Milestone-Project-3/main/static/images/400PngdpiLogoCropped.png"></h2>
<h1 align="center">Car4You BV (C4Y) online car showroom and content management application</h1>


<h2 align="center"><img src="https://raw.githubusercontent.com/MarisKX/Code-Institute-Milestone-Project-3/main/static/images/Presentation.png" width=800></h2>

### Live project:
### [Public side](http://code-institute-milestone-p3.herokuapp.com/)
### [Internal company side](http://code-institute-milestone-p3.herokuapp.com/manager-dashboard)

This project contains 2 parts. One is public part, it serves as an online car showroom and second is internal company side with limited access for car showroom management. While large part of documentation refers to both parts, there are seperate UX/UI sections for [public side](#public-side) and [internal side](#internal-side)

# PUBLIC SIDE

## User Experience (UX)

-   ### User stories

    -   #### First Time Visitor Goals

        1. As a First Time Visitor, I want to easily understand the main purpose of the site and learn more about the company.
        2. As a First Time Visitor, I want to be able to easily navigate throughout the site to find content.
        3. As a First Time Visitor, I want to easily find contact details, locations on map as well as details of cars they offer.

    -   #### Returning Visitor Goals

        1. As a Returning Visitor, I want to find information about new offers.
        2. As a Returning Visitor, I want to find the best way to get in contact with the company with any questions I may have.
        3. As a Returning Visitor, I want to find community links and follow them.

    -   #### Frequent User Goals
        1. As a Frequent User, I want to check to see if there are any newly added cars for rent and/or sell.
        2. As a Frequent User, I want to check to see if there are any new regular customer discounts.

-   ### Design
    -   #### Colour Scheme
        -   The two main colours used are C4Y main colors - green ![#128d32](https://via.placeholder.com/15/128d32/000000?text=+) `#128d32/rgb(46, 125, 50)` and grey ![#424242](https://via.placeholder.com/15/424242/000000?text=+) `#424242/rgb(66, 66, 66)`. These are main colors in C4Y showroom as well as website.
    -   #### Typography
        -   The Josefin Sans font is the main font used throughout the whole website with Sans Serif as the fallback font in case for any reason the font isn't being imported into the site correctly. Josefin Sans is a clean font with a small "twist" so it is both attractive and appropriate.
    -   #### Imagery
        -   Imagery is important. Mid-size car images are randomly generated on the main page, as well as sales page and rental page, layout is made attractive for all screen sizes.

*   ### Wireframes

    -   Landing page wireframe - Desktop-[View](https://github.com/MarisKX/Code-Institute-Milestone-Project-3/blob/main/static/other/wireframes%20public/Home%20page.pdf), 
        Mobile-[View](https://github.com/MarisKX/Code-Institute-Milestone-Project-3/blob/main/static/other/wireframes%20public/Home%20mobile.pdf)

    -   Cars for sale/cars for rent (uses the same structure) - Desktop-[View](https://github.com/MarisKX/Code-Institute-Milestone-Project-3/blob/main/static/other/wireframes%20public/Cars%20for%20sale%20%26%20rent.pdf), 
        Mobile-[View](https://github.com/MarisKX/Code-Institute-Milestone-Project-3/blob/main/static/other/wireframes%20public/Cars%20for%20sale%20%26%20rent%20mobile.pdf)

    -   Contact Us Page Wireframe - Desktop-[View](https://github.com/MarisKX/Code-Institute-Milestone-Project-3/blob/main/static/other/wireframes%20public/Contact.pdf), 
        Mobile-[View](https://github.com/MarisKX/Code-Institute-Milestone-Project-3/blob/main/static/other/wireframes%20public/Contact%20mobile.pdf)

    -   Car detail view (sales and rent uses the same main structure) Wireframe - Desktop-[View](https://github.com/MarisKX/Code-Institute-Milestone-Project-3/blob/main/static/other/wireframes%20public/Car%20detail%20view.pdf), 
        Mobile-[View](https://github.com/MarisKX/Code-Institute-Milestone-Project-3/blob/main/static/other/wireframes%20public/Car%20detail%20view%20mobile.pdf)

## Features

-   Responsive on all device sizes

-   Interactive elements

    - Randomly seleceted cars to choose from for sale and for rent
    - By clicking on car image (or description) opens window, where user can see 4 pictures of car in larger size (depends on the screen)
    - By clicking on car image (or description) opens window, where user can see full description of car, main features are ilustrated with icons
    - In both mainsections there is search bar, so user can easily search for car he/she's interested in (only car makes that are in database will show up, if the car was added, but later deleted, corresponding car make will not show up on search options)
    - Footer sections contains contact details with links - phone number will promt call option on mobile devices, while adress will open google maps app on mobile devices.
    - Company location adreses are linked with google maps too on main page under map as well as on contact page.

- Navigation is made easier by double options - either from standart menu or in landing page itself by clicking on coresponding section names

### Testing User Stories from User Experience (UX) Section

-   #### First Time Visitor Goals

    1. As a First Time Visitor, I want to easily understand the main purpose of the site and learn more about the company.

        1. Upon entering the site, users are automatically greeted with a clean and easily readable navigation bar to go to the page of their choice. Underneath there is a selection of cars for sale, cars for rent and contact section with maps, providing all companies locations.
        2. The main points are made immediately with two sections on main page - cars for sale and cars for rent both in the page itself as well as in navbar
        3. The user has two options, either check one of the cars system randomly generates or go directly to section of their choice (to buy a car or to rent one)

    2. As a First Time Visitor, I want to be able to easily be able to navigate throughout the site to find content.

        1. The site has been designed to be fluid and never to entrap the user. At the top of each page there is a clean navigation bar, each link describes what the page they will end up at clearly.
        2. On the Contact Us Page, there is a large map, indicating locations, which user might be interested in


-   #### Returning Visitor Goals

    1. As a Returning Visitor, I want to find the new cars for rent and/or buy.

        1. These are clearly shown in the front page.
        2. They will be directed to a page to their interest.

    2. As a Returning Visitor, I want to find the best way to get in contact with the company with any questions I may have.

        1. The navigation bar clearly highlights the "Contact Us" Page.
        2. Here they can find a map with all contacts, below that is footer section with phone number, email and socail network links.
        3. Whichever socail media link they click, it will be open up in a new tab to ensure the user can easily get back to the website.

    3. As a Returning Visitor, I want to find the Facebook Group link so that I can join and interact with others in the community.
        1. The Facebook Page can be found at the footer of every page and will open a new tab for the user and more information can be found on the Facebook page.

-   #### Frequent User Goals

    1. As a Frequent User, I want to check to see if there are any newly added cars.

        1. The user would already be comfortable with the website layout and can easily click the navigation button of their choice.

# INTERNAL SIDE

## User Experience (UX)

-   ### User stories

    -   #### Internal site user goals

        1. As an app user, I want to easily navigate management website, with more than just single way to get to option I need
        2. As an app user, I want to be able to easily find manual, if I need to refer to it
        3. As an app user, I want manage car showroom and rental side with as few clicks as possible
        4. As an app user (company), I want to be able to follow all activities from other users (who created car, who edited, who sold etc)
        5. As an app user (company), I want to restrict access to certain sections according to user main role within company

-   ### Design
    -   #### Colour Scheme
        -   Just like external side, internal side uses the same main colors - green ![#128d32](https://via.placeholder.com/15/128d32/000000?text=+) `#128d32/rgb(46, 125, 50)` and grey ![#424242](https://via.placeholder.com/15/424242/000000?text=+) `#424242/rgb(66, 66, 66)`.
    -   #### Typography
        -   The Josefin Sans font is the main font used throughout the whole website with Sans Serif as the fallback font in case for any reason the font isn't being imported into the site correctly. Josefin Sans is a clean font with a small "twist" so it is both attractive and appropriate.
    -   #### Imagery
        -   Management side doesn't contain pictures, as it purpose is to be internal managing website/app. Only exception - there is mid-size pictures in cars description.

*   ### Wireframes

    -   Landing page (Login/Register) wireframe - [View](https://github.com/MarisKX/Code-Institute-Milestone-Project-3/blob/main/static/other/wireframes%20internal/Internal-login.pdf)

    -   Dashboard - [View](https://github.com/MarisKX/Code-Institute-Milestone-Project-3/blob/main/static/other/wireframes%20internal/Internal-dashboard.pdf)

    -   Car List view (sales and rent uses the same structure) - [View](https://github.com/MarisKX/Code-Institute-Milestone-Project-3/blob/main/static/other/wireframes%20internal/Internal-carlistview.pdf)

    -   Settings - [View](https://github.com/MarisKX/Code-Institute-Milestone-Project-3/blob/main/static/other/wireframes%20internal/Internal-settings.pdf)

    -   Add new car/edit car (sales and rent uses the same structure) - [View](https://github.com/MarisKX/Code-Institute-Milestone-Project-3/blob/main/static/other/wireframes%20internal/Internal-addnewcar.pdf)

## Features

-   Responsive on all device sizes, however it's recomended to use it on screens with horizontal width 750px or above.

-   Ability to perform all steps that car showroom/rental company might need:
    1. Add new cars
    2. Edit current cars:
        - Edit car details (description, price, etc)
        - Mark car as sold (only cars for sale)
        - Move cars from available to unavailable (only cars for rent)
        - Move cars to archive
        - Retrieve cars from archive
    3. Delete cars permanently

- Navigation is made as easy as possible with more than just single way to get to option in need
- For more options and features - see [user manual](https://raw.githubusercontent.com/MarisKX/Code-Institute-Milestone-Project-3/main/static/documents/UserManual.pdf).

## Testing User Stories from User Experience (UX) Section

-   #### Internal site user goals

    1. As an app user, I want to easily navigate management website, with more than just single way to get to option in need
        - Sections are accessible from main menu as well as from dashboard, by clicking "more details" under corresponding section
        - Edit car option is available from list view as well as from car details view
    2. As an app user, I want to be able to easily find manual, if I need to refer to it
        - User manual is available from main navbar (opens in new window, format - PDF)
    3. As an app user, I want manage car showroom and rental side with as few clicks as possible
        - To add new car, it requires only 2 clicks to get input window
        - To mark car as available/unavailable or move car to/from archive, it requires just one click on icon from list view
    4. As an app user (company), I want to be able to follow all activities from other users (who created car, who edited, who sold etc)
        - In car details view, at the bottom of page is small section of stats - who and when created car, edited or sold.
    5. As an app user (company), I want to restrict access to certain sections according to user main role within company
        - This app requires login and password to use it
        - Every user can have their specific rights, depending of their role in company (for example - employee working with car sales, cannot access or edit car rental section). Rights are divided in 3 categories - sales, rent and users.




# Technologies Used

-   Initial development was made using [Atom IDE](https://atom.io/). 
-   Python-specific functions was tested and modeled in [PyCharm IDE](https://www.jetbrains.com/pycharm/)

## Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [javaScript](https://en.wikipedia.org/wiki/JavaScript)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

## Frameworks, Libraries & Programs Used

1. [Bootstrap 5.0:](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
1. [Materialize 1.0.0](https://materializecss.com/)
    - Materialize was used to assist with the responsiveness and styling of the website, where there was need for cleaner styling than Bottstrap offers.
1. [Material Design for Bootstrap v5 & v4:](https://mdbootstrap.com/)
    - Material Design was used for some advanced features (like carousel) that has limited options in other used frameworks
1. [Hover.css:](https://ianlunn.github.io/Hover/)
    - Hover.css was used on the main menu items in header to add the float transition while being hovered over.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
1. [jQuery:](https://jquery.com/)
    - jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript.
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes](https://github.com/) during the design process.
1. [Heroku:](https://heroku.com/)
    - Heroku pages was used to deploy project
1. [MongoDB:](https://mongodb.com/)
    - As a database system was used MongoDB
1. [LogoMaker:](https://www.logomaker.com/)
    - Logomaker was used to make company's Logo in different sizes

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C Markup Validator](https://validator.w3.org/) - [Results index page](https://raw.githubusercontent.com/MarisKX/Code-Institute-Milestone-Project-2/main/assets/other/Index%20page%20html.png), [Results cars for sale page](https://raw.githubusercontent.com/MarisKX/Code-Institute-Milestone-Project-2/main/assets/other/Cars%20for%20sale%20page.png), [Results cars for rent page](https://raw.githubusercontent.com/MarisKX/Code-Institute-Milestone-Project-2/main/assets/other/Cars%20for%20rent%20page.png), [Results contact us page](https://raw.githubusercontent.com/MarisKX/Code-Institute-Milestone-Project-2/main/assets/other/Contact%20us%20page.png)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://raw.githubusercontent.com/MarisKX/Code-Institute-Milestone-Project-2/main/assets/other/CSS.png)




## Further Testing

-   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Firefox browsers.
-   The website was viewed on a variety of devices such as Desktop (32" and 24"), Laptop, iPhone7, Samsung S20 and Samsung S20+
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

## Known Bugs

-   On mobile devices, to select car make in dropdown searchbar, You have to hold a little bit on car make instead of just clicking. Partially solved by increasing Z-index for "ul" element - now this bug appears mostly on Android mobile devices and not allways. Complete fix is not know yet.

## Deployment

### Heroku

The project was deployed to Heroku pages using following steps:

1. Log in to [Heroku](https://heroku.com/) 
2. From dashboard locate "New" > "Create new app"
3. Giving app name and select region (Europe or USA)
4. Before deployment, navigate to "Settings" > "Reveal Config Vars"
5. Fill in key - value pairs as they are in env.py file
6. Navigate to "Deploy" > "GitHub - Connect to Github"
7. Select repository You want to deploy and press "Connect"
8. After Heroku performs setup, Your page is available online.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/MarisKX)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/MarisKX)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

### Content

-   All content was written by the developer.

### Media

-    All pictures of cars was taken from Autoscout24.nl website

### Acknowledgements

-   My friends and family for testing this app and UX feedback

-   And, of course, biggest thanks to my wife, without her moral support this project would not gonna be possible!!!
