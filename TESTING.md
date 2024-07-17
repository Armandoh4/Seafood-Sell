# Testing - Filmlab Productions

![Home](assets/readme_img/home.png)

---
## Contents:
  * [W3C Validator](#w3c-html-validaton)
  * [Jigsaw](#jigsaw-css-validation)
  * [Testing User Stories](#testing-user-stories)
---


## Jigsaw CSS Validation
    
| Bug (class)   | Error  | Soloution & Result |
| :------------ |:---------------| :-----|
|.oneByOne|"Too many values or values are not recognized : 20px 1em"| By removing the additional "1em" nothing visible on the page changed |
|.inLine .mainTitle|"Value Error : text-align centre is not a text-align value : centre"|I fixed the typo of "center", however this still does not impact the webpage visually|
|.pcLogo |centre is not a align-items value : centre| This was tghe same issue as above, but once it was resolved, the effect was noticable, as the pc logo now sat in the middle of the nav-bar, as it was intended to|
|.navbar-nav|in is not a transition value : transform 0.4s ease in |I removed this because the code was meant to create a transition between the navbar sidepannel appearing and diappearing, however, it did not function in this way |

![Jigsaw CSS](assets/readme_img/jigsawcssvalidator1.png)

The following 'errors' did not affect my code in any meaningful way, and by removing this code, my website would loose features. For example, code such as "-webkit-tap-highlight-color: transparent;" can have a positive effect on the webpage, such as removing the blue box when a button on a mobile is clicked, improving mobile UX.

![Jigsaw CSS](assets/readme_img/jigsawcssvalidator.png)


## W3C HTML Validation

### *index.html:*

| Error | Soloution & Result | Pass or Fail |
| :-------- | :-----|:- |
|"Element ul not allowed as child of element ul in this context"|I changed the "ul" tag to a "li" tag and the error was resolved in all navigations across all my pages|Pass|
|"An img element must have an alt attribute, except under certain conditions"|I added "alt" tags to each image element, to resolve this error |Pass|
|"Element p6 not allowed as child of element section in this context"|To resolve the issues of "p" child elements not being able to be held in "section" I changed the "p6" element to a "div" |Pass|

### *films.html:*
| Error | Soloution & Result | Pass or Fail |
| :-------- | :-----|:- |
|"a tag not nested correctly"|I used a span to wrap the inner contents of the a attribute|Pass|
|Element summary not allowed as child of element div in this context | I changed the "summary" element to a "section" as it is considered more correct|Pass|
|Element h1 not allowed as child of element span in this context |I changed the h1 element to a div, as the h1 |Pass|
|"Error involving 'p' not being allowed as child of element span in this context"| The "p" element cannot be a child of a "span" element. Instead, I swapped the more semantic elements with "span" elements, to reduce the amount of errors. However, as this caused spacing issues, due to span being a block type element, I switched to using divs, similar to the home page film tiles|Pass|

### *about.html:*
| Error | Soloution & Result | Pass or Fail |
| :-------- | :-----|:- |
|"br not allowed as child of element ul"|I removed all "br" tags which spaced out the "li" tags, instead I added a new class to replace this function|Pass|
|"Element summary not allowed as child of element section"|I changed the semantic element to div|Pass|
|Issues of open tags, for example, the "main" tag was open, and the same was true for "section" tag| I fixed it by finding where these tags opened, and closing them|Pass|


### *bts.html:*
| Error | Soloution & Result | Pass or Fail |
| :-------- | :-----|:- |
| Attribute src not allowed on element button|Since src is not the correct element to apply to a button I applied the img tag instead |Pass|

### *Films section | Kidnapped |Killer Santa | Once Upon a Time:*
| Error | Soloution & Result | Pass or Fail |
| :-------- | :-----|:- |
|"Attribute src not allowed on element button"|Since src is not the correct element to apply to a button I applied the img tag instead |Pass|
|"The frameborder attribute on the iframe element is obsolete"|Since the value of the item was 0, it was unnecesarry to include any further|Pass|
|"Error from using 'p5' as a child element for a 'ul'"|To counteract this I changed the child to "li" and targeted the new list items with the following properties "list-style: none; display: inline;" so they behave as they did before|Pass|
|"Error: No li element in scope but a li end tag seen"|Deleted surplus "li" tag|Pass|

## PEP8 - app.py

  In my code there were no major errors. Only referingto white spaces and and lines being too long. In this regard the code fails these tests. However the end user will not experience any errors due to them.

## Testing User Stories:

### First Time Visitor
| User Story |Pass or Fail |Soloution & Result |
| :---- |:-- |:-------|
|1 - To quickly find out what projects Filmlab is working on|Pass|Finding Filmlab's newest project is easy, it is the first thing that a site visitor will see when they enter the page. When loading the homepage (which is also reached by clicking 'home' or the Filmlab logo), the user will be greeted with a promotional image for said film. This is coupled with a call to action, 'find out more. ' When clicked, the user is transported to a teaser of said film, along with details on the date it will come out (if available), and the cast involved.|
|2 - To find out if filmlab is a legitimate business along with their track record with film making|Pass|On Filmlab finding out if it is a legitimate producer is simple. A user can navigate to a film via the home page, and clicking a film listed below. Once on the film's page, they can view it, along with the details of the director and producers' social media linked to their name. The official Filmlab social media pages are also linked directly through the navbar, and will open a new window, as to not clear the current one.|
|3 - To be able to navigate to the films section and watch the projects, possibly after seeing potential advertisements or anticipation on social media for a new film.|Pass|Viewers have many ways to reach a desired film. This can be done on almost all pages, however is most effective on the home page or film page. Here, all films are presented with a thumbnail, genera, film length, release date & a description of the film's contents. This gives the user a complete overview of the page and its content.|
|4 - To find out information on the team behind filmlab, follow the careers of actors involved, where the company is based, and to contact the company directly.|Pass|An investor would be most interested in the involvement of the producers in each project, along with their corresponding roles. This is easily accessible underneath the description of the film, where it describes who was involved and their social media address'. However, while investors will have an inherent interest in contacting the company directly. To navigate to this section, there is one method. To go to the navigation bar, on the left and it opens the email. However, this may not be the best experience as it takes the user off the page. This is easily accomplished through the "Contact us" hyperlink. However, as this takes the user to another app, this can be seen as less desirable for the user.|
|5 - What the company is about and how they work together to produce films|Pass|This user would be interested in the 'behind the scenes' aspects of Filmlab. As such they will likely use the navigation bar on the left side, and press 'BTS' or its corresponding icon. This will bring them to a slideshow with all the photos of the team together, and an interactive button to change the slides. There is also a video below the 'BTS' image slideshow.|

### Returning Visitor GOAL
| User Story |Pass or Fail |Soloution & Result |
| :---- |:-- |:-------|
|1 - To navigate around and see the newest projects & films, or upcoming projects|Pass|Similar to the first time user, to stay up to date on the newest projects. The user only needs to go as far as the home page, as all promotional contents are displayed there.|
|2 - To be able to see up to new images on the behind the scenes page, with new content about upcoming or completed projects, that they care about|Pass|Filmlab achieves this well, returning visitors will be able to stay up to date with the Behind The Scenes (BTS) page, which can be found by clicking on 'BTS' in the navigation panel. Additionally, the home page photo is always up to date with the newest film, so it is easy to stay up to date with current projects.|
|3 - Actors or producers who want to share their work|Pass|All people involved in each film are mentioned in the credits under each film. To reach this, a user will only need to go as far as to click on the a film to open the corresponding page. They can then share their direct involvement in a project, or their role in the Filmlab team, in the 'about' page, which is found via the navigation menu.|
|4 - Creators would be more interested in publishing their work, rather than watching. These users would demand an admin account where they can upload, edit and delete videos from the database.| PASS|Admins are now able to log in with the admin login and password. This brngs them to a new interface that allows them to edit 'Films.' However, these do not transfer over to other pages yet.|